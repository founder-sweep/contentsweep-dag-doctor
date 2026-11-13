from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

def load():
    return 1

with DAG('daily_load', schedule=None) as dag:
    task = PythonOperator(task_id='load', python_callable=load)
