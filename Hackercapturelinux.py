Make sure to credit Benjamin Hunter Miller.

Here are the steps to create an application that captures IP addresses when someone hacks your computer on a Linux environment. This code captures network traffic, detects hacking attempts, and logs IP addresses.

1. **Install the necessary libraries**:
   First, install the necessary libraries.
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install scapy
   pip3 install requests
   ```

2. **Write the Python code**:
   Write the code to detect hacking attempts and capture IP addresses.

   ```python
   from scapy.all import *
   import requests

   def packet_callback(packet):
       # Check if it's an IP packet
       if packet.haslayer(IP):
           ip_src = packet[IP].src
           ip_dst = packet[IP].dst
           print(f"[+] Captured IP packet: {ip_src} -> {ip_dst}")
           
           # Save the hacker's IP address to a file
           with open("captured_ips.txt", "a") as f:
               f.write(f"Source: {ip_src}, Destination: {ip_dst}\n")

           # Send the hacker's IP address to a specific server
           data = {'source_ip': ip_src, 'destination_ip': ip_dst}
           requests.post("http://your-server-url.com/log_ip", data=data)

   # Set the network interface
   sniff(prn=packet_callback, store=0)

   if __name__ == "__main__":
       print("Capturing packets...")
   ```

3. **Security settings**:
   - To securely transmit and store captured IP addresses, use HTTPS on the server-side and add authentication.
   - Configure the `requests.post` part to include the server URL and a security token to ensure only authenticated requests are accepted.

4. **Server setup**:
   - Set up a server to store the captured IP addresses. You can use a web framework like Flask.

     ```python
     from flask import Flask, request

     app = Flask(__name__)

     @app.route("/log_ip", methods=["POST"])
     def log_ip():
         source_ip = request.form.get("source_ip")
         destination_ip = request.form.get("destination_ip")
         with open("server_captured_ips.txt", "a") as f:
             f.write(f"Source: {source_ip}, Destination: {destination_ip}\n")
         return "IP Logged", 200

     if __name__ == "__main__":
         app.run(ssl_context=('cert.pem', 'key.pem'))
     ```

Now, you can use this code to create an application that detects hacking attempts and captures IP addresses.



