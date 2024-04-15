# Usa una imagen base que contenga Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el código Python al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000 (puerto por defecto de FastAPI)
EXPOSE 8000

# Comando para ejecutar la aplicación usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]