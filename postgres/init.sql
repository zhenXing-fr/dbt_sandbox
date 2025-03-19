CREATE TABLE public.raw_orders (
  id INT PRIMARY KEY,
  customer_name VARCHAR(50),
  order_date DATE
);

INSERT INTO public.raw_orders (id, customer_name, order_date) VALUES
(1, 'John Doe', '2023-01-01'),
(2, 'Jane Smith', '2023-01-02');

CREATE DATABASE airflow_db;
CREATE USER airflow WITH PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow;