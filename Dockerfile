FROM apache/airflow:2.6.2-python3.9 AS base

# Change root user to use 'apt-get'
USER root
RUN sudo apt-get update && \
apt-get install -y libpq-dev gcc build-essential wget

RUN mkdir -p /opt/spark/jars/ && wget -O /opt/spark/jars/postgresql-42.2.16.jar https://jdbc.postgresql.org/download/postgresql-42.2.16.jar

USER airflow
RUN pip install --upgrade pip
RUN pip install --upgrade typing_extensions
RUN pip install --upgrade attrs
RUN pip install --upgrade psycopg2
# Created from apache/airflow image
ENV AIRFLOW_HOME=/opt/airflow

ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}"

COPY requirements.txt .

RUN pip install -r requirements.txt --use-deprecated=legacy-resolver

# src에 있는 소스들로 dag 적용하기 위해
COPY --chown=airflow:root src/. .

COPY --chown=airflow:root . .

# logs의 권한에러 발생하여 추가
RUN chmod -R 777 /opt/airflow/logs