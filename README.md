# Ingestão de Cotações Financeiras com Alpha Vantage no Databricks

Projeto de ingestão de dados financeiros utilizando a API **Alpha Vantage** e a plataforma **Databricks**, com armazenamento em **Delta Lake** e governança via **Unity Catalog**.

---

## 📌 Objetivo

Coletar cotações diárias de ações da B3, armazenar os dados na **camada Bronze** e disponibilizar uma **view analítica** para consultas e análises.

---

## 🗂 Estrutura do Projeto

├── api.py # Ingestão dos dados via API

├── config.py # Configurações do projeto

├── DataView.sql # View analítica

└── README.md



---

## ⚙️ O que foi implementado

- Ingestão de dados da API Alpha Vantage
- Tratamento e padronização dos dados em Python
- Persistência em tabela Delta (append)
- Uso de Unity Catalog
- Criação de view analítica com agregações por ticker

---

## 🔄 Fluxo do Pipeline

1. `config.py`  
   Define catálogo, API, tickers e tabela Bronze

2. `api.py`  
   Consulta a API, trata erros e grava os dados em:
kpuudata.alphavantage_bronze.cotacoes_alpha

3. `DataView.sql`  
Cria a view:

analytics_api.vw_cotacoes_resumo


---

## 📊 View Analítica

A view `vw_cotacoes_resumo` fornece:
- Última data disponível
- Maior alta e menor baixa
- Preço médio de fechamento
- Volume total negociado
- Última data de ingestão

---

## 🧠 Tecnologias

- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog
- Python
- SQL
- Alpha Vantage API

---

## ▶️ Como Executar

1. Atualize a `API_KEY` em `config.py`
2. Execute `api.py` no Databricks
3. Execute `DataView.sql`
4. Consulte os dados via SQL

---


