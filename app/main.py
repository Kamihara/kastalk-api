from typing import Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# from app.model import NormalLang

from pydantic import BaseModel


class NormalLang(BaseModel):
    word: str
    pronounce: Optional[str] = None


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/healthcheck")
def healthcheck():
    return JSONResponse(content="OK", status_code=200)

@app.post("/answer")
def get_answer(n: NormalLang):
    answer = {"answer": n.word}
    return JSONResponse(status_code=200, content=answer)