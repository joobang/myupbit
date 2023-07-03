FROM apache/airflow:2.6.2-python3.9 AS base

# Change root user to use 'apt-get'
USER root
RUN sudo apt-get update && \
apt-get install -y libpq-dev gcc build-essential


USER airflow
RUN pip install --upgrade pip
RUN pip install --upgrade typing_extensions
RUN pip install --upgrade attrs
# Created from apache/airflow image
ENV AIRFLOW_HOME=/opt/airflow

ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}"

COPY requirements.txt .

RUN pip install -r requirements.txt --use-deprecated=legacy-resolver

COPY --chown=airflow:root src/. .

COPY --chown=airflow:root . .
