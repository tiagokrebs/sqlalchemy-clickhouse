from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DDL

conn_str = 'clickhouse://username:password@hostname:8123/default'
engine = create_engine(conn_str)
session = sessionmaker(bind=engine)()

database = 'test'
engine.execute(DDL(f'CREATE DATABASE IF NOT EXISTS {database}'))

