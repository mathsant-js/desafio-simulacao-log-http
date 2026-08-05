# 📊 Monitoramento de Saúde de Endpoints com Python

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Licença](https://img.shields.io/badge/Licença-MIT-green)
![Projeto Acadêmico](https://img.shields.io/badge/Projeto-Acadêmico-orange)

## Índice

- [📊 Monitoramento de Saúde de Endpoints com Python](#-monitoramento-de-saúde-de-endpoints-com-python)
  - [Índice](#índice)
  - [Descrição do Projeto](#descrição-do-projeto)
  - [Status do Projeto](#status-do-projeto)
  - [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
    - [Funcionalidades](#funcionalidades)
    - [Demonstração](#demonstração)
  - [Acesso ao Projeto](#acesso-ao-projeto)
  - [Tecnologias utilizadas](#tecnologias-utilizadas)
  - [Pessoas Contribuidoras](#pessoas-contribuidoras)
  - [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras-do-projeto)
  - [Licença](#licença)

## Descrição do Projeto

Este projeto foi desenvolvido como parte de um desafio de volta às aulas da disciplina **Pensamento Computacional e Automação com Python**.

A proposta consiste em simular o monitoramento de requisições realizadas para diferentes endpoints de uma API. A partir de uma sequência de códigos de status HTTP, o programa identifica requisições bem-sucedidas, contabiliza erros, calcula a taxa de sucesso de cada endpoint e determina sua classificação de estabilidade.

Além da prática com estruturas de dados e funções, o projeto exercita conceitos importantes de lógica de programação, como percorrer listas, realizar cálculos, organizar responsabilidades em funções e gerar relatórios a partir dos dados processados.

## Status do Projeto

✅ Projeto concluído.

O desafio foi desenvolvido com todos os requisitos propostos, realizando a análise das requisições, classificação dos endpoints e identificação daquele que apresentou a maior quantidade de erros.

## Funcionalidades e Demonstração da Aplicação

### Funcionalidades

* Analisar requisições de múltiplos endpoints.
* Identificar requisições bem-sucedidas utilizando códigos HTTP.
* Contabilizar erros por endpoint.
* Calcular a porcentagem de sucesso.
* Detectar endpoints com erros consecutivos.
* Classificar endpoints como:

  * **ESTÁVEL**
  * **INSTÁVEL**
  * **CRÍTICO**
* Exibir o endpoint com maior quantidade de erros.

### Demonstração

Ao executar o programa, é exibido um relatório semelhante ao seguinte:

```text
==== LOG ENDPOINTS ====

ENDPOINT '/login'
Erros: 2
Erros consecutivos: SIM
Porcentagem de sucesso: 60.0%
Classificação do Endpoint: CRÍTICO

ENDPOINT '/produtos'
Erros: 0
Erros consecutivos: NÃO
Porcentagem de sucesso: 100.0%
Classificação do Endpoint: ESTÁVEL

ENDPOINT '/pedidos'
Erros: 3
Erros consecutivos: SIM
Porcentagem de sucesso: 40.0%
Classificação do Endpoint: CRÍTICO

==== ENDPOINT COM MAIS ERROS ====

ENDPOINT: '/pedidos'
Quantidade de erros: 3
```

## Acesso ao Projeto

Clone o repositório utilizando o Git:

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
```

Acesse a pasta do projeto:

```bash
cd NOME-DO-REPOSITORIO
```

Execute o programa:

```bash
python main.py
```

## Tecnologias utilizadas

* Python 3
* Estruturas de dados (Listas)
* Funções
* Condicionais
* Laços de repetição
* Type Hints
* Docstrings

## Pessoas Contribuidoras

Até o momento, este projeto não possui contribuições externas.

Contribuições futuras são bem-vindas por meio da abertura de *Issues* ou envio de *Pull Requests*.

## Pessoas Desenvolvedoras do Projeto

**Matheus Jorge Santana**

Desenvolvimento da lógica, implementação das funcionalidades, organização do código e documentação do projeto.

## Licença

Este projeto está disponível sob a Licença MIT.

Sinta-se à vontade para estudar o código, utilizá-lo como referência e adaptá-lo para fins educacionais.
