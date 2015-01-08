#!/bin/env python3

import argparse
import socket
import time

parser = argparse.ArgumentParser(description="Monitor a port for open/closedness")

parser.add_argument('host', type=str, help="Host to monitor")
parser.add_argument('port', type=int, help="Port to monitor")

parser.add_argument('--timeout', type=int, help="Timeout (seconds)", default=5)
parser.add_argument('--sleep', type=int, help="Time to sleep between checks (seconds)", default=30)

args = parser.parse_args()

while True:
    print("[%s] %s:%d is " % (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), args.host, args.port), end="")

    try:
        connection = socket.create_connection(
            (args.host, args.port),
            args.timeout
        )

        print("open")
    except Exception as e:
        print("closed")

    time.sleep(args.sleep)