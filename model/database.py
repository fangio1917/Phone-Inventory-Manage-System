from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import sql_dsn

Base = declarative_base()

# 数据库连接
engine = create_engine(sql_dsn)


def get_session():
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session
