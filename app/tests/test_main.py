
from fastapi.testclient import TestClient
from inventario.main import app

client = TestClient(app)


def test_inicio():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["estado"] == "ok"


def test_version():
    response = client.get("/")
    assert response.json()["version"] == "1.0.0"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["estado"] == "ok"


def test_listar_productos():
    response = client.get("/productos")
    assert response.status_code == 200
    assert response.json()["productos"] == []


def test_total_productos():
    response = client.get("/productos")
    assert response.json()["total"] == 0


def test_obtener_producto():
    response = client.get("/productos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_producto_disponible():
    response = client.get("/productos/1")
    assert response.json()["estado"] == "disponible"
