from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///meetings.sqlite3', echo = True)
meta = MetaData()

Base = declarative_base()
meeting = Table(
    'meeting', meta,
    Column("id",Integer, primary_key=True, index=True),
    Column("title",String, index=True),
    Column("date",String, index=True),
    Column("start_time",String, index=True),
    Column("end_time",String, index=True),
    Column('attendees',String, index=True),
)

meta.create_all(engine)