<div align="center">
  <img src="project_logo.png" alt="Project Logo">
</div>

# Análise de Portas para Melhorar a Segurança da Empresa

Este é um projeto de ferramenta de análise de portas desenvolvido para ajudar na avaliação da segurança da rede de uma empresa. A ferramenta verifica as portas em um intervalo específico em um host alvo e informa se as portas estão abertas ou fechadas.

## Funcionalidades

- Análise de Portas: Verifica se as portas em um intervalo estão abertas ou fechadas em um host alvo.
- Detecção de Serviços: Futuramente será adicionada a funcionalidade de detecção de serviços associados a portas abertas.

## Pré-requisitos

Certifique-se de ter o Python instalado.

## Como Usar

1. Clone este repositório para sua máquina local.
2. Abra um terminal e navegue até o diretório do projeto.
3. Execute o script `port_analysis.py` utilizando o comando `python port_analysis.py`.
4. Siga as instruções no terminal para fornecer o endereço IP do host alvo e o intervalo de portas.

## Exemplo de Saída

```plaintext
Análise de Portas para Melhorar a Segurança da Empresa

Digite o endereço IP do host alvo: 192.168.1.1
Digite a porta inicial do intervalo: 80
Digite a porta final do intervalo: 100

Iniciando análise de portas...

[+] Porta 80 está aberta.
[-] Porta 81 está fechada.
[+] Porta 82 está aberta.
...
