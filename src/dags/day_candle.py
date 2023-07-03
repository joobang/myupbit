from __future__ import annotations

from datetime import datetime
from datetime import timedelta
from typing import Any, Dict
from utils.dag import DAG_DEFAULT_ARGS
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests

"""dag_default_args: Dict[str, Any] = {
    **DAG_DEFAULT_ARGS,
    'start_date': datetime(2023, 1, 1),
    'max_active_tis_per_dag': 2,
}"""

dag_default_args: Dict[str, Any] = {
    'weight_rule': 'absolute',
    'owner': 'myupbit',
    'depends_on_past': False,
    'retry_delay': timedelta(minutes=5),
    'retries': 1,
    'start_date': datetime(2023, 1, 1),
    'max_active_tis_per_dag': 2,
}

with DAG(
    dag_id='day_candle_api',
    default_args=dag_default_args,
    description='get KRW-BTC day candle',
    schedule_interval='@once'
) as dag:
    
    def get_day_candle():
        url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&to=2023-01-01 00:00:00&count=100"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        print(response.text)
    
    t1 = PythonOperator(
        task_id='day_candle_api',
        python_callable=get_day_candle
    )
    
    t1