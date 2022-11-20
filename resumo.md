### Important Network Concepts

- Network:
- Wireless Access Point: switch without cables
- Switch: device
- Gateway:
- Broadcast:
-
- Socket: combination of IP + port number (ex.: 192.168.0.11:3389)

- Three Way Handshake

#### ARP

- Address Resolution Protocol (ARP)
- Protocol or procedure that **connects an IP address to a fixed physical machine address (MAC address)**

## Scanning Network

### Finding IPs

Options:

1. Having the host's IP and the netmask:

```
nmap -sn '<first_3_octets.*>'
```

2. Without any other infos:

```
ping -b <broadcast_addr> &
arp -a
```

3. With the target interface:

```
sudo arp-scan --interface=<tgt_interface> --localnet
```

### Intercepting packages

1. TCPDUMP

- **Capturing packages**

- Capturing packages without associating IP with name

```
tcpdump -n -i eth0
```

- Capturing packages from specific source host and destination port

```
tcpdump -i eth0 src host <src_host> and dst port <dst_port>
```

- Capturing packages associated with a specific protocol

```
tcpdump -i eth0 <protocol>
```

- **Saving tcpdump to file**

```
tcpdump -i eth0 -w <filename>.pcap
```

---

### ENUMERATION

PROBLEM: nmap gets nmap well-known ports
SOLUTION: `nmap -p 0-65535 <IP>

NMAP: Checking for open ports and services running (s)ervice and (v)ersion:

```
nmap -sV <target_IP>
```

**-s -> Only sends SYN flag - windows (blocks ICMP)**
Good practice: finds open port -> run telnet on the port`

ARPING and FPING:

```
arping [-s <source>] -l interface <destination>
fping
```

HTTP -> banner -> TCP connection -> Sends back a lor of info about the request

#### Telnet

Telnet (old protocol for remote connections):
TELNET -> safe (doesn´t raise red flags -> normal TCP connection

```
telnet <targetIP>
```

```
telnet <targetIP> <port>
```

### WEB SERVICES

- We can use web browsers in the format `aula.avelinux.com:88`
- We can use telnet followed by (dummy header -> returns banner):

```
HTTP1.0
```

#### Nikto

- Web server info (version, programming language,e tc)
- Usually a good idea to use nikto on web servers

```
nikto -h <IP/domain>
```

Script to put ports in list -> telnet on all of the,

Qual servićo na porta 3306 -> mySQL
Qual versão do php (nikto, nmap)
ulnerabilidade anti click jacking -> nikto

### mySQL

Connection:

```
mysql -h {target_IP} -u root
```

Commands:

```
SHOW databases;
USE {database_name}
SHOW tables;
SELECT * FROM {table_name}*
```

### Fingerprinting

Stealth Scan (sends SYN flag to target):

```
nmap -O -sV -T4 -d -Pn <target_IP>
```

Ping

```
ping <target_IP>
```

_Ping response:_

- ttl 255 -> UNIX distros
- ttl 128 -> WIN
- ttl 64 -> LINUX distros

Telnet (gets service version and SO version)

```
telnet <IP> 22
```

Telnet Web

```
telnet <domain> 80 HTTP 100
```

- Provides dummy header, responds with server used (can expose firewalls)

### DNS

https://ipok.com.br/
https://dnschecker.org/

MX -> Mail Exchange
Servidor de e-mails -> Phishing, Regras de Bloqueio

---

# Attacks - Theory

## Worm

## Spyware

## Payload

## Exploit

## DOS and DDOS

## IP Spoofing

## Ransomwares

# Attacks - practice

## **Arpspoofing**:

- Adds entry to ARP table -> "target IP has attackers MAC address"
- Intercepts information between two devices

```
arpspoof -i <target_interface> -t <target_IP> <gateway_IP>
```

## **Credential attacks:**

- SO password storage
  - Windows:
    - c:\windows\system32\config\SAM
    - c:\windows\system32\config\SYSTEM
  - Linux:
    - /etc/passwd (usernames)
    - /etc/shadow (passwd hashes)

### Creating wordlists

- ceWL

```
cewl -w <dest_file>.txt -d <n_links_to_follow> -m <min_passwd_len> <tgt_ip/domain>
```

- crunch

```
crunch <min_chars> <max_chars> <pass_chars> > <dest_file>.txt
```

- Cupp

```
python3 cupp.py -i
```

- Ready to use wordlists:

```
cd /usr/share/worlists
```

```
	cd /usr/share/<username>/password.lst
```

- Common username lists
- admin, root, user, test

### Nmap scripts for bruteforce attacks

DNS:

```
nmap -p 80 --script dns-brute.nse <host>
```

SAMBA:

```
nmap --script smb-brute.nse -p445 <host>
```

HTTP:

```
nmap --script http-brute -p 80 <host>
```

FTP:

```
nmap --script ftp-brute -p 21 <host>
```

WORDPRESS:

```
nmap -sV --script http-wordpress-brute <target>
```

### Hydra username and password discovery

With two lists:

```
hydra -L <list_users>.txt -P <passwords>.txt <targetIP> <protocol>
```

With a username and a list:

```
hydra -l <username> -P <passwds>.txt <tgtIP> <protocol>
```

### Getting hashes from SAM

```
samdump2 -o hashes SYSTEM SAM
```

### Password cracking with John the Riper

```
cp /etc/shadow pass.txt &
john pass.txt
```

/etc/services -> well-known ports
SAMBA -> important (SMB) -> ARQUIVOS -> PORTA 445

```
smb://<IP>
```

```
rdesktop-vrdp <IP>
```

3389 (RDP) -> acesso à tela de login

cronjob
