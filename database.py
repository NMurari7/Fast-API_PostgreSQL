
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgresql_url = 'postgresql+psycopg2://postgres:admin@localhost/mydb' # replace your username password over here
engine = create_engine(postgresql_url, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

