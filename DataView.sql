-- Databricks notebook source
-- Setando qual catalogo será usado neste notebook
USE CATALOG kpuudata;

-- COMMAND ----------

-- Criando schema analytics

CREATE SCHEMA IF NOT EXISTS analytics_api

-- COMMAND ----------

-- Criando view com agregações a partir da tabela bronze

CREATE OR REPLACE VIEW analytics_api.vw_cotacoes_resumo AS
SELECT
  ticker,
  MAX(data) AS ultima_data,
  MAX(alta) AS maior_alta_no_periodo,
  MIN(baixa) AS menor_baixa_no_periodo,
  AVG(fechamento) AS preco_medio_fechamento,
  SUM(volume) AS volume_total,
  MAX(data_injestao) AS ultima_injestao
  FROM alphavantage_bronze.cotacoes_alpha
  GROUP BY ticker;

-- COMMAND ----------

--Verificando dados analiticos criados.

SELECT * FROM analytics_api.vw_cotacoes_resumo
ORDER BY ticker;
