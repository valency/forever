import argparse
import asyncio
import logging
import sys
from asyncio.subprocess import PIPE


class Forever:
    LOG = logging.getLogger('forever')

    def __init__(self, prog_args, timeout=5, interval=3):
        self._prog_args = prog_args
        self._timeout = timeout
        self._interval = interval

    @property
    def prog_args(self):
        return self._prog_args

    @property
    def timeout(self):
        return self._timeout

    @property
    def interval(self):
        return self._interval

    def run(self):
        self.LOG.info('Auto restart: prog_args={}, timeout={}.'.format(self.prog_args, self.timeout))
        loop = asyncio.get_event_loop()
        try:
            ret = loop.run_until_complete(self.repeat())
        except KeyboardInterrupt:
            self.LOG.info('Auto restart stopped by CTRL+C.')
            ret = -1
        loop.close()
        return ret

    async def repeat(self):
        while True:
            await self.run_prog()
            self.LOG.info('Waiting {} seconds before restart...'.format(self.interval))
            await asyncio.sleep(self.interval)

    async def run_prog(self):
        self.LOG.info('Process created: timeout={}.'.format(self.timeout, self.prog_args))
        proc = await asyncio.create_subprocess_exec(*self.prog_args, stdout=PIPE)
        while True:
            try:
                line = await asyncio.wait_for(proc.stdout.readline(), self.timeout)
            except asyncio.TimeoutError:
                proc.kill()
                break
            else:
                if not line:
                    break
                sys.stdout.buffer.write(line)
                sys.stdout.buffer.flush()
        retcode = await proc.wait()
        self.LOG.info('Process killed: retcode={}.'.format(retcode, self.prog_args))
        return retcode


if __name__ == '__main__':
    FORMAT = '[%(asctime)s] %(levelname)s:%(module)s:%(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    parser = argparse.ArgumentParser(usage='python -m forever.run [OPTIONS] SCRIPT [SCRIPT_ARGS]'.format(sys.argv[0]), )
    parser.add_argument('-t', '--timeout', type=int, default=5, help='timeout in seconds')
    parser.add_argument('-i', '--interval', type=int, default=3, help='waiting interval in seconds')
    args, prog_args = parser.parse_known_args()
    if not prog_args:
        parser.print_help(file=sys.stderr)
        sys.exit(127)
    sys.exit(Forever(prog_args, args.timeout, args.interval).run())
