# filepath: /Users/zhenxing/Documents/playground/dbt_sandbox/dbt/Dockerfile
FROM python:3.9-slim
WORKDIR /usr/app
RUN pip install dbt-postgres==1.5.0
COPY models/ models/
COPY dbt_project.yml dbt_project.yml
COPY profiles.yml profiles.yml