from fastapi import FastAPI
import pandas as pd



url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR1r12cssSXouQMRpdh3SDWVnffV5NvapPJ0ln6gjv-8s9eiXQ04d6kmV4TjUpxqdVGbvGHua9EsVDx/pub?gid=1081596630&single=true&output=csv"

    



app = FastAPI()

@app.get("/")  # Definindo uma rota para a função
def load_data():  # Corrigi o nome da função para algo mais claro
    df = pd.read_csv(url)
    return df.to_dict(orient="records")

# uvicorn main:app --reload



