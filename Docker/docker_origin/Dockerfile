FROM postgres:latest

# Copiar el archivo init_1.sql al directorio de inicialización de la base de datos
COPY ./init_1.sql /docker-entrypoint-initdb.d/init.sql

# Configurar la opción log_statement en PostgreSQL
RUN echo "log_statement='all'" >> /etc/postgresql/postgresql.conf