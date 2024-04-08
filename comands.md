# Comandos de Docker
## Crea y arranca un contenedor a partir de una imagen.
``` bash
docker run -d -p 8080:80 myimage
-d para ejecutar en modo detached (fondo), -p para mapear puertos.
```
## Construye una imagen Docker a partir de un Dockerfile.
``` bash
docker build -t myimage .
-t para etiquetar la imagen.
```
## Lista todas las imágenes locales.
``` bash
docker images
```
## Muestra los contenedores en ejecución. Usar docker ps -a para ver todos los contenedores, incluso los detenidos.
``` bash
docker ps
```
## Detiene uno o más contenedores en ejecución.
``` bash
docker stop container_name
```
## Elimina uno o más contenedores.
``` bash
docker rm container_name
Usar -f para forzar la eliminación de contenedores en ejecución.
```
## Elimina una o más imágenes.
``` bash
docker rmi image_name
Usar -f para forzar la eliminación.
```
## Obtiene los logs de un contenedor.
``` bash
docker logs container_name
```
## Ejecuta un comando dentro de un contenedor en ejecución.
``` bash
docker exec -it container_name bash
-it para una interacción interactiva a través de una terminal.
```

# Comandos de Docker Compose
## Crea e inicia los contenedores definidos en el docker-compose.yml.
``` bash
docker-compose up
Usar -d para ejecutar en modo detached.
```
## Detiene y elimina los recursos definidos en el docker-compose.yml.
``` bash
docker-compose down
```
## Construye o reconstruye servicios especificados en el docker-compose.yml.
``` bash
docker-compose build
```
## Visualiza los logs de los servicios.
``` bash
docker-compose logs
```
## Lista los contenedores relacionados con el proyecto.
``` bash
docker-compose ps
```
## Ejecuta un comando en un servicio.
``` bash
docker-compose exec service_name bash
```
## Detiene los servicios en ejecución sin eliminarlos.
``` bash
docker-compose stop
```
## Reinicia todos los contenedores o servicios específicos.
``` bash
docker-compose restart
```
