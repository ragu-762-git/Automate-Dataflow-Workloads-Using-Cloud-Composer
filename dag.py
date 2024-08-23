# manipulate dates and times
from datetime import datetime, timedelta

# core class for defining Airflow DAGs
from airflow import DAG

#define tasks that run bash commands
from airflow.operators.bash_operator import BashOperator

#utility fn to calculate dates in the past relative to the current date
from airflow.utils.dates import days_ago

#establish a connection with dcp dataflow pipelines
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator

#define commonly used arguments for all tasks within the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 4),
    'depends_on_past': False,
    'email': ['me22m2002@iiitdm.ac.in'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

#create a new Airflow DAG named employee_data
dag = DAG('employee_data',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@daily',
          catchup=False)


#assign tasks for the DAG
with dag:
    run_script_task = BashOperator(
        task_id='extract_data',
        bash_command='python /home/airflow/gcs/dags/scripts/extract.py',
    )

    start_pipeline = CloudDataFusionStartPipelineOperator(
    location="us-central1",
    pipeline_name="etl-pipeline",
    instance_name="datafusion-dev",
    task_id="start_datafusion_pipeline",
    )

    run_script_task >> start_pipeline



#with DAG - creates a context manager that ensures the tasks defined within the blocks are associated with the created DAG
#run_script_task - this defines a task named extract_data that uses the Bash Operator
# task_id - unique identifier for the task within the DAG
# bash_command - the bash command to be executed by the task
