FROM postgres:14
ENV POSTGRES_USER=dbt_user
ENV POSTGRES_PASSWORD=dbt_pass
ENV POSTGRES_DB=dbt_db
COPY init.sql /docker-entrypoint-initdb.d/