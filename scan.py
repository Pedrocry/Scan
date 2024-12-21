import nmap
import os
import subprocess
import webbrowser

# Inicializa o scanner
scanner = nmap.PortScanner()

def varrer(alvo):
    print(f"\n[*] Iniciando varredura em: {alvo}\n")

    # varredura basica
    resultado = scanner.scan(alvo, arguments=" -A -sS -sV -O -T4")

    # ve e entrega os host ativo
    for host in scanner.all_hosts():
        print(f"Host: {host} | Status: {scanner[host].state()}")

        # fala as porta aberta
        print("Portas abertas:")
    try:
        for porta in scanner[host]['tcp']:
            print(f" - Porta {porta}: {scanner[host]['tcp'][porta]['name']} ({scanner[host]['tcp'][porta]['state']})")
           # if(porta==80 or porta==8080):
                # print('PORTA 80 ou 8080 ABERTA')
            service=(scanner[host]['tcp'][porta]['name'])

            if(service=='http' or service=='https'):
                #os.system('ping '+host)

                #Comandos do termial
                cmd = ['gnome-terminal'] # Se estiver usando o GNOME
                cmd.extend(['-x', 'bash', '-c', 'ls -l; exec $SHELL' ])
                subprocess.Popen(cmd, stdout=subprocess.PIPE)
                #Comandos do termial

                url=service+'://'+host+':'+str(porta)
                webbrowser.open(url)
    except KeyError:
        print(f"Não foram encontrados serviços TCP para o host {host}")

        # sistema op
        if 'os' in scanner[host]:
            print(f" Sistema Operacional: {scanner[host]['osmatch'][0]['name']}")

    print("\n[*] Varredura concluída.")

#if __name__ == "_main_":
    # pede o ip
alvo = input("Digite o IP ou subrede para escanear: ")
varrer(alvo)
