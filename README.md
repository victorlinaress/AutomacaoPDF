Automação de Relatórios em PDF com Python

Este projeto foi desenvolvido como prática de automação de processos utilizando Python.

A ideia é simples: ler uma base de dados em CSV contendo informações de funcionários e gerar automaticamente relatórios individuais em PDF para cada registro da base.

Esse tipo de automação pode ser muito útil para empresas que precisam gerar relatórios repetitivos, economizando tempo e reduzindo tarefas manuais.

Tecnologias utilizadas

Python

Pandas (leitura e manipulação de dados)

ReportLab (geração de PDF)

Como funciona

O script realiza os seguintes passos:

Lê uma base de dados em formato CSV

Processa as informações de cada funcionário

Cria automaticamente um relatório em PDF para cada pessoa

Organiza os arquivos gerados em uma pasta chamada relatorios

Cada relatório contém:

Nome do funcionário

Departamento

Quantidade de horas extras

Mês de referência

Estrutura do projeto
automacaopdf
│
├── horas_extras.csv
├── main.py
├── relatorios/
│   ├── relatorio_horas_extras_Ana_Souza.pdf
│   ├── relatorio_horas_extras_Carlos_Lima.pdf
│   └── ...
Como executar o projeto

Clone o repositório

git clone https://github.com/seuusuario/automacaopdf.git

Instale as dependências

pip install pandas reportlab

Execute o script

python main.py

Após executar, os relatórios serão gerados automaticamente na pasta relatorios.

Objetivo do projeto

Este projeto foi desenvolvido com foco em:

Praticar automação com Python

Trabalhar com manipulação de dados

Gerar documentos automaticamente

Resolver problemas do mundo real com programação
