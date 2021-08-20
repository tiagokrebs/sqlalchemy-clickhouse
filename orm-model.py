from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from clickhouse_sqlalchemy import engines

conn_str = 'clickhouse://username:password@hostname:8123/default'
engine = create_engine(conn_str)
session = sessionmaker(bind=engine)()

database = 'test'

Base = declarative_base()
class NewTable(Base):
    __tablename__ = 'new_table'
    __table_args__ = (
        engines.MergeTree(order_by=['id']),
        {'schema': database},
    )
    id = Column(Integer, primary_key=True)
    var1 = Column(String)
    var2 = Column(Date)

NewTable.__table__.create(engine)

