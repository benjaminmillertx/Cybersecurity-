Python to capture IP addresses when someone hacks your computer on a Chrome OS environment:

import socket

def capture_ip_addresses():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific IP address and port
    s.bind(('0.0.0.0', 12345))

    print("Listening for incoming connections...")

    while True:
        # Receive data from the socket
        data, addr = s.recvfrom(1024)
        ip_address = addr[0]
        print("IP Address:", ip_address)

        # Add your logic here to handle the captured IP address
        # You can save it to a file, send an alert, or take any other necessary action

if __name__ == '__main__':
    capture_ip_addresses()

This code creates a UDP socket and binds it to a specific IP address and port. It then listens for incoming connections and captures the IP addresses of the connecting devices. You can add your own logic to handle the captured IP addresses, such as saving them to a file or sending an alert.

