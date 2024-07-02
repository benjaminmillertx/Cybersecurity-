Credit Benjamin Hunter Miller. Here is a simple wireless network monitoring tool that you can build in Python using the scapy library. This tool will scan for all nearby wireless access points and display their SSIDs, signal strengths, and encryption types.

First, you will need to install the scapy library if you haven't already. You can do this by running the following command:

```
pip install scapy
```

Here is the code for the wireless network monitoring tool:

```
from scapy.all import *

def scan_wireless():
    # Define the interface to use for scanning (e.g. wlan0)
    interface = 'wlan0'

    # Define the packet to send
    packet = Dot11(type=0, subtype=4, addr1="ff:ff:ff:ff:ff:ff", addr2="00:00:00:00:00:00") / Dot11Beacon()

    # Send the packet and listen for responses
    responses, unanswered = srp(packet, timeout=2, iface=interface, inter=0.1)

    # Display the results
    print("SSID\t\t\tSignal\tEncryption")
    print("------------------------------------------")
    for response in responses:
        if response[1].haslayer(Dot11Elt):
            if response[1].getlayer(Dot11Elt).ID == 0:
                ssid = response[1].getlayer(Dot11Elt).info
                signal = response[1].getlayer(Dot11Beacon).signal
                encryption = ""
                if response[1].getlayer(Dot11Elt, 2).ID == 30:
                    encryption = "WPA"
                elif response[1].getlayer(Dot11Elt, 2).ID == 43:
                    encryption = "WPA2"
                elif response[1].getlayer(Dot11Elt, 2).ID == 221:
                    encryption = "WEP"
                print(f"{ssid}\t{signal}\t{encryption}")

if __name__ == '__main__':
    scan_wireless()
```

To use this tool, simply run the script. It will scan for nearby wireless access points and display their SSIDs, signal strengths, and encryption types.

Note: This tool may not work on some systems due to restrictions on accessing the wireless interface. You may need to run the script with administrator privileges in order to access the wireless interface.
