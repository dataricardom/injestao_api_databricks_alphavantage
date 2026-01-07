# Databricks notebook source
# MAGIC %sql
# MAGIC -- Verificando Catalogos
# MAGIC SHOW CATALOGS;

# COMMAND ----------


# === 1) CATÁLOGO (Unity Catalog) ===


CATALOG = "kpuudata"   # definindo catalogo


# Define o catálogo atual

spark.sql(f"USE CATALOG {CATALOG}")


# ===2) API KEY + URL ===

API_KEY = "sua api key"

BASE_URL = "https://www.alphavantage.co/query"


# === 3) LISTA DE AÇÕES ===
# Alpha Vantage exige .SA para B3

TICKERS = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBDC4.SA", "ABEV3.SA"]


# ===4) SCHEMA/TABELA BRONZE ===

BRONZE_SCHEMA = "alphavantage_bronze"
BRONZE_TABLE = "cotacoes_alpha"

# Criar schema no catálogo UC

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{BRONZE_SCHEMA}")



# ===5) PRINTS DE DEBUG ===

print("=== CONFIG CARREGADA ===")
print(f"CATALOG............: {CATALOG}")
print(f"SCHEMA BRONZE......: {CATALOG}.{BRONZE_SCHEMA}")
print(f"TABELA BRONZE......: {CATALOG}.{BRONZE_SCHEMA}.{BRONZE_TABLE}")
print(f"TICKERS............: {TICKERS}")
print("===============================================================")
