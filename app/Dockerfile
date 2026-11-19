
FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY src/ ./src/

# Puerto de la aplicación
EXPOSE 8000

# Iniciar la aplicación
CMD ["python", "-m", "inventario.main"]
