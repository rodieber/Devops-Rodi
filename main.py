import random
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool
@app.get("/")
def read_root():
    return {"Ola": "Mundo"}


@app.get("/funcaotest/")
async def funcaotest():
    return {"test": True,"num_aleatorio": random.randint(0,20000)}



@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}