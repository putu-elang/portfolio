import socket
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="A simple port scanner.")
parser.add_argument("-t", "--target", type=str, required=True, help="Target IP ")
args = parser.parse_args()
target = args.target


print(f"Scanning target: {target}")
print("Time started: " + str(datetime.now()))

try:
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()
except KeyboardInterrupt:
    print("\nExiting program.")

except socket.gaierror:
    print("Hostname could not be resolved. Exiting program.")
except socket.error:
    print("Couldn't connect to server. Exiting program.")