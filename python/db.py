from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_ADDRESS = '172.17.0.2'
DB_PORT = '3306'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'bourse'

engine = create_engine(f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}:{DB_PORT}/{DB_NAME}?charset=utf8mb4&binary_prefix=true")
Session = sessionmaker(bind=engine)

Base = declarative_base()
