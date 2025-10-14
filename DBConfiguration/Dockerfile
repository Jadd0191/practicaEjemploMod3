FROM postgres:latest
# Copia el script SQL al directorio de inicialización de PostgreSQL
#(se ejecutan automáticamente al crear el volumen de datos por primera vez)
COPY init.sql /docker-entrypoint-initdb.d/01_init.sql
COPY save_data.sql /docker-entrypoint-initdb.d/02_save_data.sql