# dbt_sandbox
play ground for learning dbt and testing new features

## Setup Instructions

### 1. Clean up existing containers
Stop and remove all containers, networks, and volumes:
```bash
docker-compose down -v
```

### 2. Create the required Docker network
Manually create the `dbt-network` if it doesn't already exist:
```bash
docker network create dbt-network
```

### 3. Start all services
Build and start the services defined in the `docker-compose.yml` file:
```bash
docker-compose up -d --build
```

### 4. Initialize Airflow
Run the following commands to set up Airflow:

1. Create an admin user:
   ```bash
   docker-compose run --rm airflow-webserver airflow users create \
       --username admin \
       --password admin \
       --firstname Admin \
       --lastname User \
       --role Admin \
       --email admin@example.com
   ```

2. Initialize the Airflow database:
   ```bash
   docker-compose run --rm airflow-webserver airflow db init
   ```

### 5. Verify service status
Check the status of all running containers:
```bash
docker-compose ps
```

## Notes
- The `dbt-builder` service is configured to run in idle mode (`tail -f /dev/null`) and can be used for interactive debugging or running dbt commands.
- Ensure that the `dbt-network` is created before starting the services to avoid network-related issues.


```mermaid
sequenceDiagram
    participant User as User
    participant DockerCompose as docker-compose
    participant AirflowWebserver as airflow-webserver
    participant AirflowScheduler as airflow-scheduler
    participant DBTBuilder as dbt-builder
    participant Postgres as postgres

    %% Setup Phase
    User->>DockerCompose: docker-compose up -d --build
    DockerCompose->>Postgres: Start postgres container
    DockerCompose->>AirflowWebserver: Start airflow-webserver container
    DockerCompose->>AirflowScheduler: Start airflow-scheduler container
    DockerCompose->>DBTBuilder: Start dbt-builder container

    %% Airflow Initialization
    User->>AirflowWebserver: airflow db init
    AirflowWebserver->>Postgres: Initialize Airflow metadata database

    User->>AirflowWebserver: airflow users create
    AirflowWebserver->>Postgres: Create admin user

    %% DAG Execution
    User->>AirflowWebserver: Trigger dbt_pipeline DAG
    AirflowWebserver->>AirflowScheduler: Schedule dbt_pipeline DAG
    AirflowScheduler->>DBTBuilder: Execute dbt run
    DBTBuilder->>Postgres: Query database for dbt models
    DBTBuilder->>AirflowScheduler: Return dbt run results

    AirflowScheduler->>DBTBuilder: Execute dbt test
    DBTBuilder->>Postgres: Query database for dbt tests
    DBTBuilder->>AirflowScheduler: Return dbt test results
    AirflowScheduler->>AirflowWebserver: Update DAG status



