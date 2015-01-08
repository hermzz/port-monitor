Port Monitor
============

    usage: portmon.py [-h] [--timeout TIMEOUT] [--sleep SLEEP] host port
    
    Monitor a port for open/closedness
    
    positional arguments:
      host               Host to monitor
      port               Port to monitor
    
    optional arguments:
      -h, --help         show this help message and exit
      --timeout TIMEOUT  Timeout (seconds)
      --sleep SLEEP      Time to sleep between checks (seconds)

## Example

Monitor port 1234 at example.com with a timeout of 2 seconds and waiting 2 minutes between tries.

    $ ./portmon.py --timeout=2 -sleep=120 example.com 1234