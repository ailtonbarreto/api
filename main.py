from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import psycopg2


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# segunda consulta
# SELECT * FROM tembo.tb_vendas

# ------------------------------------------------------------------------------------------
# TABELA PRODUTOS
@app.get("/produtos")
def load_database():
    host = 'gluttonously-bountiful-sloth.data-1.use1.tembo.io'
    database = 'postgres'
    user = 'postgres'
    password = 'MeSaIkkB57YSOgLO'
    port = '5432'

    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )        
        query = "SELECT * FROM tembo.tb_integracao;"
        df = pd.read_sql_query(query, conn)
    except Exception as e:
  
    

     if conn:
        conn.close()
    return df.to_dict(orient="records")


# ------------------------------------------------------------------------------------------
# TABELA VENDAS

@app.get("/vendas")
def load_tbvendas():
    host = 'gluttonously-bountiful-sloth.data-1.use1.tembo.io'
    database = 'postgres'
    user = 'postgres'
    password = 'MeSaIkkB57YSOgLO'
    port = '5432'

    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )        
        query = "SELECT * FROM tembo.tb_vendas;"
        df = pd.read_sql_query(query, conn)
    except Exception as e:
  
    

     if conn:
        conn.close()
    return df.to_dict(orient="records")

# ------------------------------------------------------------------------------------------

# uvicorn main:app --reload

# uvicorn main:app --host 0.0.0.0 --port 10000

# fastapi dev main.py rodar no terminal para ver local
