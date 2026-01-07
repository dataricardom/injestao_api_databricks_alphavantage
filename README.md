# Ingestão de Dados Financeiros com Alpha Vantage no Databricks

Este projeto implementa um **pipeline de ingestão e análise de dados financeiros** utilizando a API **Alpha Vantage** e a plataforma **Databricks**, com armazenamento em **Delta Lake** e governança via **Unity Catalog**.

O objetivo é coletar cotações diárias de ações da B3, armazenar os dados na camada **Bronze** e disponibilizar uma **view analítica** para consumo posterior.

---

## 📌 Visão Geral do Projeto

O projeto realiza:

1. Ingestão de dados diários de ações via **API Alpha Vantage**
2. Tratamento e padronização dos dados em Python
3. Persistência em tabela **Delta** (camada Bronze)
4. Criação de **view analítica** com agregações por ticker

Arquitetura baseada no padrão **Bronze → Analytics (Gold)**.

---

## 🗂 Estrutura do Repositório

├── api.py # Pipeline de ingestão da API

├── config.py # Configurações do projeto

├── DataView.sql # View analítica em SQL

├── README.md

---

## ⚙️ Descrição dos Arquivos

### 📄 `config.py`
Arquivo responsável pelas **configurações globais do projeto**.

Contém:
- Definição do **Unity Catalog**
- Chave da API Alpha Vantage
- URL base da API
- Lista de tickers a serem ingeridos
- Schema e tabela da camada Bronze

Exemplo:
```python
CATALOG = "kpuudata"
TICKERS = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBDC4.SA", "ABEV3.SA"]
```

Também cria automaticamente o schema Bronze caso não exista.

📄 api.py

Notebook/script responsável pela ingestão dos dados.

Principais etapas:

1- Importa as configurações via:
```
# MAGIC %run "/Workspace/Projeto_Pos_Databricks/injestao_api_databricks/config"
```
2- Consulta a API Alpha Vantage usando a função:
```

buscar_cotacoes_diarias(symbol)
```
3- Trata erros comuns da API:

- Ticker inválido

- Limite de requisições

- Respostas inesperadas

4- Padroniza os dados:

- Conversão de tipos

- Renomeação de colunas

- Inclusão de ticker e data_injestao

5- Consolida todos os tickers em um único DataFrame

6- Grava os dados em Delta Lake (append):
```
df_spark.write.format("delta").mode("append").saveAsTable(full_table)
```
📌 Observação:
Foi adicionado time.sleep(2) entre as chamadas para respeitar o limite da API gratuita.


📄 DataView.sql

Script SQL responsável pela camada analítica.

Funcionalidades:

Define o catálogo correto

Cria o schema analytics_api

Cria uma view agregada por ticker

View criada:
```sql
analytics_api.vw_cotacoes_resumo
```

Agregações disponíveis:

- Última data disponível

- Maior alta do período

- Menor baixa do período

- Preço médio de fechamento

- Volume total negociado

- Última data de ingestão

🔄 Fluxo do Pipeline

Configuração

- Definição do catálogo, schema e tickers (config.py)

Ingestão

- Coleta de dados da Alpha Vantage (api.py)

- Gravação na tabela Bronze:

kpuudata.alphavantage_bronze.cotacoes_alpha


Transformação Analítica

- Criação da view resumida (DataView.sql)

Consumo

- Consultas SQL

- Dashboards

- APIs

- BI

🧠 Tecnologias Utilizadas

Databricks

Apache Spark

Delta Lake

Unity Catalog

Python

SQL

API Alpha Vantage

📋 Pré-requisitos

Workspace Databricks ativo

Cluster Spark em execução

Chave de API da Alpha Vantage
👉 https://www.alphavantage.co

Permissões para criar schemas e tabelas no Unity Catalog

▶️ Como Executar o Projeto

Clone ou importe o repositório no Databricks Repos

Atualize sua API_KEY no config.py

Execute o notebook api.py para ingestão dos dados

Execute o script DataView.sql para criar a view analítica

Consulte os dados: