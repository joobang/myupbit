# myupbit

프로세스

1.업비트 api 일봉 데이터 '비트코인'
         -> mongo db AND postgres db
             (airflow) 배치 생성

mongo db / postgres 설치 완료.

- docker-compose postgres / mongon db 환경 세팅하기

- 업비트 일봉 API호출 및 INSERT 하기 DAG 생성하기

2.통계성 데이터 spark로 mart 생성 (airflow)

3.태블로로 데이터 시각화