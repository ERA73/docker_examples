# comandos docker
``` bash
docker network create my_network
```
``` bash
docker build -t origin ./docker_origin/. && docker run -e POSTGRES_DB=postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=postgres -p 5433:5432 --cpus=1 --memory=0.5g -it origin
```

``` bash
docker build -t destination ./docker_destination/. && docker run -e POSTGRES_DB=postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=postgres -p 5434:5432 --cpus=1 --memory=0.5g -it destination
```

``` bash
docker build -t etl_app . && docker run --cpus=1 --memory=0.5g -p 8000:8000 -it etl_app
```