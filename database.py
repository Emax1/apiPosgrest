import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Obtener la URL de conexión desde las variables de entorno
#DATABASE_URL = "postgresql://postgres:7777@localhost:5432/cadena_suministro"
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:YsWLfjkhhtNyykSOAUlwZycpbBOOcCve@junction.proxy.rlwy.net:15459/railway")

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Configurar sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()
