# Databricks notebook source
# MAGIC %sql
# MAGIC -- Setando qual catalogo será usado neste notebook
# MAGIC USE CATALOG kpuudata;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Criando schema analytics
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS analytics_api

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Criando view com agregações a partir da tabela bronze
# MAGIC
# MAGIC CREATE OR REPLACE VIEW analytics_api.vw_cotacoes_resumo AS
# MAGIC SELECT
# MAGIC   ticker,
# MAGIC   MAX(data) AS ultima_data,
# MAGIC   MAX(alta) AS maior_alta_no_periodo,
# MAGIC   MIN(baixa) AS menor_baixa_no_periodo,
# MAGIC   AVG(fechamento) AS preco_medio_fechamento,
# MAGIC   SUM(volume) AS volume_total,
# MAGIC   MAX(data_injestao) AS ultima_injestao
# MAGIC   FROM alphavantage_bronze.cotacoes_alpha
# MAGIC   GROUP BY ticker;

# COMMAND ----------

# MAGIC %sql
# MAGIC --Verificando dados analiticos criados.
# MAGIC
# MAGIC SELECT * FROM analytics_api.vw_cotacoes_resumo
# MAGIC ORDER BY ticker;
