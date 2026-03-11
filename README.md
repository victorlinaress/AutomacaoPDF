# Automação de Relatórios em PDF com Python

Este é um pequeno projeto que desenvolvi para praticar **automação de tarefas utilizando Python**.

A ideia surgiu ao pensar em algo comum dentro de empresas: gerar relatórios repetitivos para várias pessoas.  
Em vez de fazer isso manualmente, pensei em automatizar todo o processo utilizando programação.

Nesse projeto, o script lê uma base de dados em **CSV** contendo informações de funcionários e gera automaticamente **um relatório em PDF para cada pessoa**.

Assim, em poucos segundos, vários relatórios são criados automaticamente.

---

## O que o projeto faz

O programa realiza algumas etapas simples, mas muito úteis:

- Lê uma base de dados contendo funcionários e horas extras
- Processa cada registro da base
- Gera automaticamente um **relatório individual em PDF**
- Organiza todos os relatórios em uma pasta

Cada relatório contém informações como:

- Nome do funcionário
- Departamento
- Quantidade de horas extras
- Mês de referência

Tudo isso é gerado automaticamente a partir dos dados da planilha.

---

## Tecnologias utilizadas

Para desenvolver esse projeto utilizei:

- Python
- Pandas (leitura e manipulação de dados)
- ReportLab (geração de PDF)

