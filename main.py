from fastapi import FastAPI
import pandas as pd




url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQAEct5jF2nnOSaqoR7i6Fcz2pOLXN4oifn5G2CeO3k7N3uU0C3-B-exrtzS5Ufjul32tAZ1R8KcS8N/pub?gid=0&single=true&output=csv"

# df = pd.read_csv(url)





app = FastAPI()

@app.get("/")
def load_data():
    df = pd.read_csv(url)
    return df.to_dict(orient="records")

# uvicorn main:app --reload

# fastapi dev main.py rodar no terminal para ver local

