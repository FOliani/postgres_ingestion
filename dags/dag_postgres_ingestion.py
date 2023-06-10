import os
import sys
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
from postgres_ingestion_modules.tasks.fake_dataset import create_fake_data

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

DAG_ID = 'postgres-ingestion'

with DAG(
    dag_id=DAG_ID,
    start_date=datetime(2023, 6, 9),
    catchup=False,
    tags=['postgre-ingestion'],
    dagrun_timeout=timedelta(minutes=40),
    schedule_interval=None
) as dag:

    tasks_init = EmptyOperator(
        task_id='tasks_init'
    )

    create_fake_dataset = PythonOperator(
        task_id='create_fake_dataset',
        python_callable=create_fake_data,
    )

    tasks_init >> create_fake_dataset
