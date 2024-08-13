from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Cliente, Servicio
from db import clientes_collection
from bson import ObjectId
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/clientes/", response_model=Cliente)
async def create_cliente(cliente: Cliente):
    cliente_dict = cliente.dict()
    clientes_collection.insert_one(cliente_dict)
    return cliente

@app.get("/clientes/", response_model=List[Cliente])
async def read_clientes():
    clientes = []
    for cliente in clientes_collection.find():
        clientes.append(Cliente(**cliente))
    return clientes

@app.get("/clientes/{identificacion}", response_model=Cliente)
async def read_cliente_by_id(identificacion: str):
    cliente = clientes_collection.find_one({"identificacion": identificacion})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return Cliente(**cliente)


@app.put("/clientes/{identificacion}", response_model=Cliente)

async def update_cliente_by_id(identificacion: str, updated_cliente: Cliente):
    updated_cliente_dict = updated_cliente.dict(exclude_unset=True)
    result = clientes_collection.update_one(
        {"identificacion": identificacion}, {"$set": updated_cliente_dict}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return read_cliente_by_id(identificacion)

@app.delete("/clientes/{identificacion}")

async def delete_cliente_by_id(identificacion: str):
    result = clientes_collection.delete_one({"identificacion": identificacion})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return {"detail": "Cliente deleted"}

@app.post("/clientes/{identificacion}/servicios/", response_model=Cliente)
async def add_servicio_to_cliente(identificacion: str, servicio: Servicio):
    cliente = clientes_collection.find_one({"identificacion": identificacion})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    
    cliente_obj = Cliente(**cliente)
    cliente_obj.servicios.append(servicio)

    clientes_collection.update_one(
        {"identificacion": identificacion},
        {"$set": {"servicios": [s.dict() for s in cliente_obj.servicios]}}
    )

    return cliente_obj