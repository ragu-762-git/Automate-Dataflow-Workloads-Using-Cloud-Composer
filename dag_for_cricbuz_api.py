from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 26),
    'depends_on_past': False,
    'email': ['me22m2002@iiitdm.ac.in'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
   # 'retry_delay': timedelta(minutes=5),
}

dag = DAG('fetch_cricket_stats_from_api',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@daily',
          catchup=False)

with dag:
    #1st task
    run_script_task = BashOperator(
        task_id='run_script',
        bash_command='python /home/airflow/gcs/dags/scripts/extract_and_push_gcs.py',
    )
