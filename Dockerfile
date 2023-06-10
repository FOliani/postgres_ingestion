FROM apache/airflow:2.6.1

USER airflow

RUN python -m pip install pandas
RUN python -m pip install faker
