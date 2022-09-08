import socket

ip = input("IP a ser escaneado: ")
port1 = int(input("Porta 1: "))
port2 = int(input("Porta 2 (até 65535): "))
print(f"Começando Scan em {ip}, da porta {port1} até a porta {port2}:\n\n")

for i in range(port1, port2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, i)) == 0:
        service = socket.getservbyport(i, "tcp")
        print(f"A Porta {i} está aberta, rodando o serviço {service}")
	

s.close()