from fastapi import FastAPI, HTTPException
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import psycopg2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurações de conexão ao banco
db_config = {
    'host': 'gluttonously-bountiful-sloth.data-1.use1.tembo.io',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'MeSaIkkB57YSOgLO',
    'port': '5432'
}

# ------------------------------------------------------------------------------------------
# TABELA PRODUTOS
@app.get("/produtos")
def load_database():
    try:
        conn = psycopg2.connect(**db_config)
        query = "SELECT * FROM tembo.tb_integracao;"
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        print("Erro ao carregar os produtos:", e)
        raise HTTPException(status_code=500, detail="Erro ao acessar o banco de dados.")
    finally:
        if conn:
            conn.close()
    return df.to_dict(orient="records")


# ------------------------------------------------------------------------------------------
# TABELA VENDAS
@app.get("/venda")
def load_tbvendas():
    try:
        conn = psycopg2.connect(**db_config)
        query = f"SELECT * FROM tembo.tb_venda WHERE \"EMISSAO\" >= '2024-05-31' LIMIT 10"
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        print("Erro ao carregar as vendas:", e)
        raise HTTPException(status_code=500, detail="Erro ao acessar o banco de dados.")
    finally:
        if conn:
            conn.close()
    return df.to_dict(orient="records")


# ------------------------------------------------------------------------------------------
# MODELO PARA CRIAÇÃO DE PEDIDO

class Item(BaseModel):
    pedido: str
    emissao: str
    entrega: str
    sku_cliente: int
    sku: str
    parent: int
    qtd: int
    vr_unit: float

# Endpoint POST para criar um pedido
@app.post("/pedido/")
async def create_item(item: Item):
    if item.vr_unit <= 0:
        raise HTTPException(status_code=400, detail="O valor unitário deve ser positivo.")
    if item.qtd <= 0:
        raise HTTPException(status_code=400, detail="A quantidade deve ser positiva.")
    
    return {"message": "Pedido criado com sucesso!", "item": item}

# Endpoint para testar com valores fixos
@app.post("/pedido/teste/")
async def create_test_item():
    # Valores preenchidos para o teste
    item = Item(
        pedido="PEDTESTE",
        emissao="2024-10-31",
        entrega="2024-10-31",
        sku_cliente=9999999,
        sku="49-44",
        parent=49,
        qtd=12,
        vr_unit=233.99
    )

    return {"message": "Pedido de teste criado com sucesso!", "item": item}


# uvicorn main:app --reload

# uvicorn main:app --host 0.0.0.0 --port 10000

# fastapi dev main.py rodar no terminal para ver local