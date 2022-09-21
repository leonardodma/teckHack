import os


class Host():
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name


devices = []
for device in os.popen('arp-scan -l'):
    device = device.split('\t')
    if len(device) > 1:
        devices.append(Host(device[0], device[1], device[2]))
