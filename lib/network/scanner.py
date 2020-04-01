from scapy.all import ARP, Ether, srp
import socket
import requests


class Scanner:
    TARGET_GATEWAY = "192.168.43.1/24"

    PINGBACK_PORT = 5800

    def find_network_devices(self):
        # IP Address for the destination
        # create ARP packet
        arp = ARP(pdst=self.TARGET_GATEWAY)
        # create the Ether broadcast packet
        # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        # stack them
        packet = ether / arp

        result = srp(packet, timeout=3, verbose=0)[0]

        # a list of clients, we will fill this in the upcoming loop
        clients = []

        for sent, received in result:
            # for each response, append ip and mac address to `clients` list
            clients.append({'ip': received.psrc, 'mac': received.hwsrc})

        return clients

    def find_all_peers(self):
        peers = []

        clients = self.find_network_devices()

        for client in clients:
            if self.is_device_peer(client):
                peers.append(client)

        print(peers)

        return peers

    def is_device_peer(self, client):
        # Check if ping port is open
        ip_address = client['ip']

        if not self.__is_port_open(ip_address, self.PINGBACK_PORT):
            return False

        # Construct pingback URL
        url = str.format('http://{}:{}', ip_address, self.PINGBACK_PORT)

        try:
            # Send HTTP request
            response = requests.get(url)

            # Check if device is part of network
            rdata = response.json()

            if not rdata['client'] or rdata['client'] is not "TrentonZW":
                raise Exception("Invalid client name")

            return True
        except:
            return False

    def __is_port_open(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return True
        except:
            return False
