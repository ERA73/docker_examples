# 1 Introducción Teórica

## ¿Qué es Docker?:
Una plataforma de contenedores que permite empaquetar una aplicación y sus dependencias en un contenedor virtual que puede correr en cualquier sistema operativo Linux o Windows que soporte Docker.
Destaca la importancia de Docker en el desarrollo y la operación de aplicaciones modernas, facilitando la portabilidad y escalabilidad.

## ¿Qué es Docker Compose?:
Una herramienta para definir y correr aplicaciones Docker multi-contenedor. Utiliza un archivo YAML para configurar los servicios de la aplicación.
Menciona cómo Docker Compose simplifica el proceso de manejo de contenedores interconectados, manejo de volumenes, redes, y configuraciones específicas.


## Diferencias Clave

### Docker
* #### Nivel de operación: 
    Docker opera a nivel de contenedores. Permite crear, ejecutar, detener y gestionar contenedores de manera individual o en grupos pequeños.
* #### Uso principal: 
    Se utiliza para crear imágenes de contenedores y gestionar el ciclo de vida de los contenedores. Permite a los usuarios empaquetar aplicaciones y sus dependencias en un contenedor que puede ser transportado y ejecutado en cualquier sistema que tenga Docker instalado.
* #### Comandos: 
    Incluye comandos para construir imágenes (docker build), iniciar contenedores (docker run), listar contenedores (docker ps), entre otros.
* #### Archivo de configuración: 
    Los contenedores son configurados y gestionados mediante comandos en la línea de comandos o archivos Dockerfile para construir imágenes.
### Docker Compose
* #### Nivel de operación: 
    Docker Compose opera a nivel de servicios, donde un servicio puede estar compuesto por uno o varios contenedores que funcionan juntos.
* #### Uso principal: 
    Diseñado para definir y compartir aplicaciones multi-contenedor. Permite a los desarrolladores definir un conjunto de contenedores y sus relaciones en un solo archivo YAML, simplificando el proceso de despliegue de aplicaciones complejas.
* #### Comandos: 
    Utiliza comandos específicos de Compose como docker-compose up para iniciar toda la aplicación, docker-compose down para detenerla, docker-compose build para construir las imágenes definidas en el archivo de Compose, etc.
* #### Archivo de configuración: 
    Utiliza un archivo docker-compose.yml para definir los servicios, redes y volúmenes necesarios para la aplicación. Esto permite una gestión más fácil y declarativa de aplicaciones compuestas por múltiples contenedores.
### En Resumen
Docker es una herramienta de contenerización que permite a los desarrolladores empaquetar aplicaciones en contenedores, haciéndolas portátiles y fáciles de desplegar.
Docker Compose es una herramienta para definir y ejecutar aplicaciones multi-contenedor con Docker, facilitando la gestión de aplicaciones compuestas por varios contenedores interconectados

# 2 Demostración Práctica
Setup de un Proyecto con Docker (10 minutos)
Setup de un Proyecto con Docker Compose (10 minutos)

Muestra cómo crear un Dockerfile para una aplicación web sencilla (puede ser un servidor web básico como un "Hola Mundo" en Node.js o Python Flask).
Construye la imagen con Docker y corre el contenedor, mostrando cómo acceder a la aplicación desde un navegador.
Integración con Docker Compose (15 minutos)


# 3 Sesión de Preguntas y Respuestas