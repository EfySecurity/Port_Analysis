<div align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="python-logo-generic.svg">
</div>

# Análise de Portas na rede.
Este é um projeto de ferramenta de análise de portas desenvolvido para ajudar na avaliação da segurança da rede de uma empresa. A ferramenta verifica as portas em um intervalo específico em um host alvo, identifica os serviços associados e tenta obter o banner (resposta) desses serviços.

## Funcionalidades

- Análise de Portas: Verifica se as portas em um intervalo estão abertas ou fechadas em um host alvo.
- Detecção de Serviços: Identifica o nome do serviço associado a portas abertas.
- Banner do Serviço: Tenta obter o banner (resposta) do serviço em portas abertas.

## Pré-requisitos

Certifique-se de ter o Python instalado.

## Como Usar

1. Clone este repositório para sua máquina local. 

```bash
git clone https://github.com/EfySecurity/Port_Analysis
```

2. Navegue até o diretório

```bash
cd Port_Analysis
```

3. Execute o script `port_analysis.py` utilizando o comando `python port_analysis.py`.

4. Siga as instruções no terminal para fornecer o endereço IP do host alvo e o intervalo de portas.

## Exemplo de Saída

```plaintext
Análise de Portas para Melhorar a Segurança da Empresa

Digite o endereço IP do host alvo: 192.168.1.1
Digite a porta inicial do intervalo: 80
Digite a porta final do intervalo: 100

Iniciando análise de portas...

[+] Porta 80 está aberta. Serviço: http
   Banner: Apache HTTP Server
[-] Porta 81 está fechada.
[+] Porta 82 está aberta. Serviço: ssh
   Banner: OpenSSH 8.2p1 Ubuntu
```

## Contribuição
Contribuições para melhorias e novas funcionalidades são bem-vindas. Crie um fork deste repositório, faça suas alterações e envie um pull request.

## Licença
Este projeto está sob a proteção da licença [MIT](LICENSE)

## **AVISO:**
Use esta ferramenta apenas de maneira ética e responsável. A análise de portas sem permissão pode violar a política de segurança da empresa ou leis locais.

## Autor
Nome: Efy Security

Email: efy.security@proton.me
