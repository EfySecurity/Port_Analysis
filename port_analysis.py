import socket

# Cores ANSI
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    ENDC = "\033[0m"

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        return False

def main():
    print(f"{Colors.GREEN}Análise de Portas na rede{Colors.ENDC}\n")

    host = input("Digite o endereço IP do host alvo: ")
    start_port = int(input("Digite a porta inicial do intervalo: "))
    end_port = int(input("Digite a porta final do intervalo: "))
    print("\nIniciando análise de portas...\n")

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"{Colors.GREEN}[+] Porta {port} está aberta.{Colors.ENDC}")
        else:
            print(f"{Colors.RED}[-] Porta {port} está fechada.{Colors.ENDC}")

if __name__ == "__main__":
    main()
