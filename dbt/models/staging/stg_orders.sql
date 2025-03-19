{{ config(materialized='table') }}

SELECT
  id AS order_id,
  customer_name,
  order_date
FROM {{ source('public', 'raw_orders') }}