from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG(
    dag_id='dbt_pipeline',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:
    
    dbt_run = DockerOperator(
        task_id='dbt_run',
        image='dbt-project',
        command='dbt run',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='dbt-network'
    )

    dbt_test = DockerOperator(
        task_id='dbt_test',
        image='dbt-project',
        command='dbt test',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='dbt-network'
    )

    dbt_run >> dbt_test