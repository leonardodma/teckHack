import sys
import socket


def get_tcp_service(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, port)) == 0:
        try:
            service_tcp = socket.getservbyport(port, "tcp")
            print(
                f"A Porta {port} está aberta, rodando o Serviço TCP: {service_tcp}")
        except:
            pass


def get_udp_service(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, port)) == 0:
        try:
            service_udp = socket.getservbyport(port, "udp")
            print(
                f"Porta aberta no IP {ip}, rodando o Serviço UDP: {service_udp}")
        except:
            pass


def main(argv, argc):
    ports_list = []
    ip = None

    for arg in argv[1:]:
        if arg.startswith('-p'):
            ports_list = arg.replace('-p', '').split(',')

        if arg.startswith('-ip'):
            ip = arg.replace('-ip', '')

    # Check if the user passed the ip and ports to scan
    if len(ports_list) > 2:
        raise Exception("Você só pode passar 2 portas")
    elif len(ports_list) == 0:
        raise Exception(
            "Você precisa passar uma porta com o argumento -p")
    if ip is None:
        raise Exception("Você precisa passar um IP com o argumento -ip")

    # Run the scan
    if len(ports_list) == 1:
        get_tcp_service(ip, int(ports_list[0]))
        get_udp_service(ip, int(ports_list[0]))
    else:
        for i in range(int(ports_list[0]), int(ports_list[1])):
            get_tcp_service(ip, i)
            get_udp_service(ip, i)


if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
