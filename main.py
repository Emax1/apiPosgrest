from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas
import os

# Crear la base de datos al iniciar la aplicación
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rutas de la API
@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/registros/", response_model=schemas.Registro)
def create_registro(registro: schemas.RegistroCreate, db: Session = Depends(get_db)):
    db_registro = models.RegistroDeIngreso(**registro.dict())
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro

@app.get("/registros/", response_model=list[schemas.Registro])
def get_registros(db: Session = Depends(get_db)):
    return db.query(models.RegistroDeIngreso).all()

@app.get("/registros/{registro_id}", response_model=schemas.Registro)
def get_registro(registro_id: int, db: Session = Depends(get_db)):
    registro = db.query(models.RegistroDeIngreso).filter(models.RegistroDeIngreso.idregistro == registro_id).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro

@app.put("/registros/{registro_id}", response_model=schemas.Registro)
def update_registro(registro_id: int, registro_update: schemas.RegistroCreate, db: Session = Depends(get_db)):
    registro = db.query(models.RegistroDeIngreso).filter(models.RegistroDeIngreso.idregistro == registro_id).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    for key, value in registro_update.dict().items():
        setattr(registro, key, value)
    db.commit()
    db.refresh(registro)
    return registro

@app.delete("/registros/{registro_id}", response_model=dict)
def delete_registro(registro_id: int, db: Session = Depends(get_db)):
    registro = db.query(models.RegistroDeIngreso).filter(models.RegistroDeIngreso.idregistro == registro_id).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    db.delete(registro)
    db.commit()
    return {"message": "Registro eliminado exitosamente"}

# 🚀 Configuración para Railway
port = int(os.environ.get("PORT", 8080))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
