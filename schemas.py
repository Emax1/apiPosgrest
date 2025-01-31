# schemas.py
from pydantic import BaseModel
from typing import List

class RegistroBase(BaseModel):
    documentoingre: List[str]
    nombrepersona: List[str]

class RegistroCreate(RegistroBase):
    pass

class Registro(RegistroBase):
    idregistro: int

    class Config:
        from_attributes = True  # Cambiar de 'orm_mode'



