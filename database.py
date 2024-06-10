from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config

Base = declarative_base()

def get_engine():
    config = Config()
    return create_engine(f'postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}')

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()