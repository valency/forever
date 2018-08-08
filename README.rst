==============================
Forever
==============================
Auto restart any script if it stops printing.

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

    python -m forever bash forever_example.sh
    python -m forever -t 3 -i 3 python -u -m forever_example
