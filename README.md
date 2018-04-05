# Forever
Auto restart any script if it stops printing.

## Usage

```bash
python -m forever [OPTIONS] SCRIPT [SCRIPT_ARGS]
```

Required arguments:

- `SCRIPT [SCRIPT_ARGS]`: Script and its arguments

Optional arguments:

- `-h`, `--help`: Show help message and exit
- `-t TIMEOUT`, `--timeout TIMEOUT`: Timeout in seconds
- `-i INTERVAL`, `--interval INTERVAL`: Waiting interval in seconds

## Examples

```bash
python -m forever bash forever_example.sh
python -m forever -t 3 -i 3 python -u -m forever_example
```