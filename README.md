# Tecnologias Hacker - Resumo

Roteiros e Resumo da disciplina Tecnologias Hacker

## Coletar informações do Alvo

- Encontrar ip de boradcast

```console
ifconfig
```

- Comunicar com todos que estão na mesma rede

```console
ping {ip_broadcast}
```

- Descobrir todos os IPs que estão na mesma rede

```console
arp-scan -l
```

- Descobrir qual serviço está rodando no alvo em alguma porta específica

```console
netcat -z -n -v {ip} {port}
```

```console
nmap {ip} -p{port}
```

- Descobrir quais serviços estão rodando nas portas do computador

Utilizando o script, é possível verificar um ip específico, ou passar um intervalo de ip para realizar a análise. O mesmo raciocínio é feito para as portas.

```console
python3 portScanner.py -ip{ip1, ip2} -p{port1,port2}
```

Utilizando o Nmap

```console
nmap {ip}
```

- Obter informações do sistema operacional

```console
telnet {ip} 22
```

```console
nmap -O {ip}
```

## Listar Vulnerabilidades do alvo

- Vulnerabilidades (CVE - Common Vulnerabilities and Exposures)

```console
nmap -sV --script vuln {ip} -p{port1},{port2}
```

- Encontrar um **exploit** (maneira de explorar as vulnerabilidades)

```console
nmap -sV --script malware {ip} -p{port1},{port2}
```

## Encontrar Informações de um domínio

- Obter endereço de IP associado

```console
nslookup {dominio}
```

```console
dig {dominio}
```

- Servidor DNS

```console
host -t ns {dominio}
```

- Servidor de Email associado

https://dnschecker.org/mx-lookup.php

- Obter outros domínios no mesmo IP

https://hackertarget.com/reverse-ip-lookup/

- Sistema operacional do servidor

```console
ping {dominio}
```

A partir desse comando, com o resultado do TTL, é possível inferir o sistema opeacional, usando a tabela desse [link](https://www.yeahhub.com/identify-operating-system-using-ping-command/)

- Tecnologias Utilizadas no site:

Utilizar extesão **Wappalyzer**

- Identificação de WAF (Web Application Firewall)

```console
wafw00f -a -v {dominio}
```

## Processos e permissões

- **Processos:**

Em sistemas operacionais Unix, existe sistema de processos pais e filhos, em que o processo pais de todos é o `systemd`.

Listando processos

```console
pstree
```

Lista processos ativos

```console
ps
```

Lista processos em forma dinâmica

```console
top
```

Finalizar processos

```console
kill -9 {process_id}
```

- **Permissões**

Obter tipos de permição dos arquivos:

```console
ls -l
```

![permissões](./img/permissions_commands.jpg)

Alterar permissões

![permissões](./img/permissions.png)

```console
chmod {permission} {filename}
```

Na permissão, são colocados uma sequência de 3 números que fazem referências as permissões de Owner, Group e Other Users, respectiviamente. Esses números são calculados pela das permissões, em que:

4 - Permissão de leitura (r)
2 - Permissão de escrita (w)
1 - Permissão de execução (x)

Assim, a permissão **777** concede leitura, escrita e execução para todos os grupos.

## Comandos importantes

- **Arp spoofing:** Este ataque consiste em adicionar ou substituir na tabela arp da `maquina alvo` uma entrada que aponte um IP do Alvo para o MAC Address do Atacante na tabela ARP da vítima.

  É o método mais rápido de se estabelecer no meio da comunicação entre duas máquinas e interceptar as informações enviadas entre ambas

```console
arpspoof -i {INTERFACE_REDE} -t {IP_DO_ALVO} {IP_DO_GATEWAY}
```

- **TCP Dump:** É uma ferramenta utilizada para monitorar os pacotes trafegados numa rede de computadores. Ela mostra os cabeçalhos dos pacotes que passam pela interface de rede.

  Argumetos:

  - -i: Seleciona a interface
  - -v: Saída detalhada
  - -vv: Saída Extremamente Detalhada
  - -w: Saída para algum arquivo
  - -r: acessar saída gerada

```console
tcpdump -i eth0 -w resultadodacaptura.pcap
```

```console
tcpdump -r resultadodacaptura.pcap
```
