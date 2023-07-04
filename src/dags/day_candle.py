from __future__ import annotations

from datetime import datetime
from datetime import timedelta
from typing import Any, Dict
from utils.dag import DAG_DEFAULT_ARGS
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests

dag_default_args: Dict[str, Any] = {
    **DAG_DEFAULT_ARGS,
    'start_date': datetime(2020, 1, 1),
    'max_active_tis_per_dag': 2,
}

# dag_default_args: Dict[str, Any] = {
#     'weight_rule': 'absolute',
#     'owner': 'myupbit',
#     'depends_on_past': False,
#     'retry_delay': timedelta(minutes=5),
#     'retries': 1,
#     'start_date': datetime(2023, 1, 1),
#     'max_active_tis_per_dag': 2,
# }

with DAG(
    dag_id='day_candle_api',
    default_args=dag_default_args,
    description='get KRW-BTC day candle',
    schedule_interval='@once'
) as dag:
    
    def get_day_candle():
        url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&to=2020-01-01 00:00:00&count=1"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        return response.text
    
    t1 = PythonOperator(
        task_id='day_candle_api',
        python_callable=get_day_candle,
        dag=dag
    )
    
    def save_to_postgres(**context):
        response_text = context['task_instance'].xcom_pull(task_ids='day_candle_api')
        print(response_text)
    
    t2 = PythonOperator(
        task_id='save_to_postgres',
        python_callable=save_to_postgres,
        provide_context=True,  # 이를 설정하면, callable 함수에 context를 전달
        dag=dag
    )
    t1 >> t2