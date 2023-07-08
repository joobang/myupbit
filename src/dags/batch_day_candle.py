from __future__ import annotations

from datetime import datetime
from datetime import timedelta
from typing import Any, Dict
from utils.dag import DAG_DEFAULT_ARGS
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import requests
import json

dag_default_args: Dict[str, Any] = {
    **DAG_DEFAULT_ARGS,
    'start_date': datetime(2023,7,7),
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
    dag_id='day_candle_default_bulk',
    default_args=dag_default_args,
    description='get KRW-BTC day candle first data bulk',
    schedule_interval='@once'
) as dag:
    
    # def get_day_candle_bulk(**context):
    #     #url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&to="+"2020-01-01 00:00:00"+"&count=1"
    #     now_date = datetime.now()
    #     print(now_date)
    #     formatted_execution_date = now_date.strftime("%Y-%m-%d %H:%M:%S")
    #     url = f"https://api.upbit.com/v1/candles/days?market=KRW-BTC&to={formatted_execution_date}&count=200"
    #     headers = {"accept": "application/json"}
    #     response = requests.get(url, headers=headers)
    #     #print(response.text)
    #     #diff = datetime.now() - datetime(2023,6,27)
    #     #print(diff.days)
                
    #     return response.text
    
    # t1 = PythonOperator(
    #     task_id='get_bulk_data',
    #     python_callable=get_day_candle_bulk,
    #     dag=dag
    # )
    def get_execution_date(**context):
        execution_date = context['execution_date']
        print(f"Execution date is {execution_date}")
    
    base_date = datetime.now()
    
    for i in range(11):
        task_date = base_date - timedelta(days=200 * i)
        t1 = PythonOperator(
            task_id='test get bulk data',
            python_callable=get_execution_date,
            provide_context=True,
            execution_date=task_date,  # use the dynamic date here
            dag=dag
        )
    
    t1