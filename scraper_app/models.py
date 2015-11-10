from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_entries_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Entries(DeclarativeBase):
    """Sqlalchemy entries model"""
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    rooms = Column('rooms', Integer)
    entry_date = Column('posted_on',DateTime,nullable=True)
    price = Column('price', String, nullable=True)
    size = Column('size', String, nullable=True)
    district = Column('district', String, nullable=True)
    start_date = Column('free_from', DateTime, nullable=True)
    end_date = Column('free_to', DateTime, nullable=True)
    link = Column('link', String, nullable=True)