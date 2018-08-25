==============================
Forever
==============================
Auto restart any script if it stops printing.

Install
-----

.. code:: bash

    pip install forever

Usage
-----

.. code:: bash

    python -m forever [OPTIONS] SCRIPT [SCRIPT_ARGS]

Options:

-h, --help  show help message and exit
-t TIMEOUT, --timeout TIMEOUT  timeout in seconds
-i INTERVAL, --interval INTERVAL  checking frequency in seconds

Examples
--------

.. code:: bash

    python -m forever.run bash `curl https://raw.githubusercontent.com/valency/forever/master/forever/example.sh`
    python -u -m forever.run -t 3 -i 3 python -u -m forever.example
