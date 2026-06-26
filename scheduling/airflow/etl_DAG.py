from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="etl_print",
    start_date=datetime.now(),
    schedule="*/2 * * * *",
    catchup=False,
) as dag:

    print_employee = BashOperator(
        task_id="print_employee",
        bash_command="bash /mnt/d/code/python/learning\ py/scheduling/airflow/run_etl.sh ",
    )
