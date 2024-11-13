import sys
import socket
from datetime import datetime

# Define the target
TARGET = str(input("Enter the IP address to scan: "))
targetIP = socket.gethostbyname(TARGET)

try:
    # Add a pretty banner
    print("Scanning target " + targetIP)
    print("Time started: " + str(datetime.now()))
    print("-" * 50)

    # Scan the target
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((targetIP, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
