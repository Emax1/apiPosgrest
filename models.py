from sqlalchemy import Column, BigInteger, ARRAY, String
from database import Base

class RegistroDeIngreso(Base):
    __tablename__ = "registrosdeingreso"

    idregistro = Column(BigInteger, primary_key=True, index=True)
    documentoingre = Column(ARRAY(String))  # Cambiar CHAR a String
    nombrepersona = Column(ARRAY(String))  # Cambiar CHAR a String
