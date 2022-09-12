import socket

ip = input("IP a ser escaneado: ")
port1 = int(input("Porta 1: "))
port2 = int(input("Porta 2 (A maior existente é a 65535): "))
print(f"Começando Scan em {ip}, da porta {port1} até a porta {port2}:\n")

for port in range(port1, port2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, port)) == 0:
        print(f"A Porta {port} está aberta:")
        try:
            service_tcp = socket.getservbyport(port, "tcp")
            print(f"Rodando o Serviço TCP: {service_tcp}")
        except:
            pass

        try:
            service_udp = socket.getservbyport(port, "udp")
            print(f"Rodando o Serviço UDP: {service_udp}")
        except:
            pass

        print("=======================================================")

    s.close()
