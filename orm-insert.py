from sqlalchemy import create_engine, DDL, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from clickhouse_sqlalchemy import engines
from datetime import date

conn_str = 'clickhouse://username:password@hostname:8123/default'
engine = create_engine(conn_str)
session = sessionmaker(bind=engine)()

database = 'test'

engine.execute(DDL(f'CREATE DATABASE IF NOT EXISTS {database}'))

tablename = 'new_table'

Base = declarative_base()
class NewTable(Base):
	__tablename__ = tablename
	__table_args__ = (
		engines.MergeTree(order_by=['id']),
		{'schema': database},
	)
	id = Column(Integer, primary_key=True)
	var1 = Column(String)
	var2 = Column(Date)

NewTable.__table__.create(bind=engine, checkfirst=True)

for i in range(1000):
	row = NewTable(id=i, var1=f'test_str_{i}', var2=date(2021, 5, 3))
	session.add(row)
session.commit()

