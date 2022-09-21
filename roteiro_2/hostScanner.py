import sys
import os
import nmap
import requests
import socket
from contextlib import closing
nm = nmap.PortScanner()


class Host():
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name


def getHosts():
    hosts = []
    for device in os.popen('arp-scan -l'):
        device = device.replace("\n", "").split('\t')
        if len(device) > 1:
            hosts.append(Host(device[0], device[1], device[2]))

    return hosts


def get_os(ip):
    try:
        return nm.scan(ip, arguments='-O')['scan'][ip]['osmatch'][0]['name']
    except:
        return "Unknown"


def get_mac_details(mac_address):

    # We will use an API to get the vendor details
    url = "https://api.macvendors.com/"

    # Use get method to fetch details
    response = requests.get(url+mac_address)
    if response.status_code != 200:
        return "Unknown"
    return response.content.decode()


def get_ports_open(ip):
    num_open_ports = 0
    for i in range(1, 1000):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(1)
            if sock.connect_ex((ip, i)) == 0:
                num_open_ports += 1
            sock.settimeout(None)

    return num_open_ports


def main(argv, argc):
    hosts = getHosts()
    for host in hosts:
        print(f"IP: {host.ip} MAC: {host.mac} Name: {host.name}")
        #print(f"OS: {get_os(host.ip)}")
        print(f"Fabricante: {get_mac_details(host.mac)}")
        print(f"Número de Portas abertas: {get_ports_open(host.ip)}")
        print("---------------------------------------------------")


if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
