
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="API Inventario",
    description="Sistema de gestión de inventario",
    version="1.0.0"
)

# Información de la aplicación
VERSION = "1.0.0"


@app.get("/")
def inicio():
    return {
        "estado": "ok",
        "version": VERSION
    }


@app.get("/health")
def health():
    return {
        "estado": "ok",
        "servicio": "inventario",
        "version": VERSION
    }


@app.get("/productos")
def listar_productos():
    return {
        "productos": [],
        "total": 0
    }


@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    return {
        "id": producto_id,
        "nombre": "Producto de ejemplo",
        "estado": "disponible"
    }


@app.get("/info")
def informacion():
    return {
        "aplicacion": "Inventario",
        "version": VERSION,
        "fecha": datetime.now().isoformat()
    }
