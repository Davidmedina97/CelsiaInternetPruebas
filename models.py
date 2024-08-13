from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import date

class Servicio(BaseModel):
    servicio: str
    fechaInicio: str
    ultimaFacturacion: str
    ultimoPago: int

class Cliente(BaseModel):
    identificacion: str = Field(max_length=20)
    nombres: str = Field(max_length=80)
    apellidos: str = Field(max_length=80)
    tipoIdentificacion: str = Field(max_length=2)
    fechaNacimiento: str
    numeroCelular: str = Field(max_length=20)
    correoElectronico: EmailStr
    servicios: Optional[List[Servicio]] = []

    class Config:
        schema_extra = {
            "example": {
                "identificacion": "1234567890",
                "nombres": "Juan",
                "apellidos": "Pérez",
                "tipoIdentificacion": "CC",
                "fechaNacimiento": "1980-01-01",
                "numeroCelular": "3001234567",
                "correoElectronico": "juan.perez@example.com",
                "servicios": [
                    {
                        "servicio": "Internet",
                        "fechaInicio": "2023-01-01",
                        "ultimaFacturacion": "2023-07-01",
                        "ultimoPago": 50000
                    },
                    {
                        "servicio": "TV",
                        "fechaInicio": "2023-02-01",
                        "ultimaFacturacion": "2023-07-01",
                        "ultimoPago": 30000
                    }
                ]
            }
        }