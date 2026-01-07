# Databricks notebook source
# MAGIC %run "/Workspace/Projeto_Pos_Databricks/injestao_api_databricks/config"

# COMMAND ----------


import requests
import pandas as pd
from datetime import datetime
import time

# COMMAND ----------

#Função para obter dados da API

def buscar_cotacoes_diarias(symbol: str) -> pd.DataFrame:
  params = {
      'function': 'TIME_SERIES_DAILY',
      'symbol': symbol,
      'apikey': 'API_KEY',
      'outputsize': 'compact'
  }

  response = requests.get(BASE_URL, params=params)
  response.raise_for_status()
  data = response.json()

    #Tratamento de Erros:

  if "Error Message" in data:
      raise ValueError(f"Error API para {symbol}: {data['Error Message']}")

  if "Note" in data:
      raise ValueError(f"Limite diário atingido ou aviso:{data['Note']}")
  
  if "Time Series (Daily)" not in data:
      raise ValueError(f"Resposta inesperada para {symbol}: {data}")
  
  ts = data["Time Series (Daily)"]
  
  df = (
      pd.DataFrame.from_dict(ts, orient='index')
      .reset_index()
      .rename(columns={
          "index": "data",
          "1. open": "abertura",
          "2. high": "alta",
          "3. low": "baixa",
          "4. close": "fechamento",
          "5. volume": "volume",
      })
  )


  df["data"] = pd.to_datetime(df["data"]).dt.date
  df["abertura"] = df["abertura"].astype(float)
  df["alta"] = df["alta"].astype(float)
  df["baixa"] = df["baixa"].astype(float)
  df["fechamento"] = df["fechamento"].astype(float)
  df["volume"] = df["volume"].astype(float)
  df["ticker"] = symbol
  df["data_injestao"] = datetime.utcnow()

  return df

# COMMAND ----------

#Executando pipeline

dfs = []
for ticker in TICKERS:
    print(f"Ingerindo {ticker}...")
    dfs.append(buscar_cotacoes_diarias(ticker))
    time.sleep(2)

df_final = pd.concat(dfs, ignore_index=True)
print(f"Total de linhas carregadas: {len(df_final)}")




# COMMAND ----------

df_final.display()

# COMMAND ----------

#Gravando dados no Delta{Unity Catalog}
df_spark = spark.createDataFrame(df_final)
full_table = f"{CATALOG}.{BRONZE_SCHEMA}.{BRONZE_TABLE}"

df_spark.write.format("delta").mode("append").saveAsTable(full_table)

print(f"Ingestão concluída com sucesso em: {full_table}")
      
display(spark.table(full_table).orderBy("data", "ticker"))
