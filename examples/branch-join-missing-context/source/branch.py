from airflow import DAG
from airflow.providers.standard.operators.python import BranchPythonOperator, PythonOperator
dag = DAG("branch_example")
branch = BranchPythonOperator(task_id="choose")
a = PythonOperator(task_id="a")
b = PythonOperator(task_id="b")
join = PythonOperator(task_id="join", trigger_rule="all_success")
branch >> [a, b] >> join
