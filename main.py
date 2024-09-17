from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware



url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQAEct5jF2nnOSaqoR7i6Fcz2pOLXN4oifn5G2CeO3k7N3uU0C3-B-exrtzS5Ufjul32tAZ1R8KcS8N/pub?gid=0&single=true&output=csv"

# df = pd.read_csv(url)





app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (modifique conforme necessário)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)


@app.get("/")
def load_data():
    df = pd.read_csv(url)
    return df.to_dict(orient="records")



# uvicorn main:app --reload

# uvicorn main:app --host 0.0.0.0 --port 10000

# fastapi dev main.py rodar no terminal para ver local

