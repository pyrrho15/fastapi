from sqlalchemy import create_engne
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL="sqlite:///./test.db"

engine = create_engne(DB_URL, connect_args={"check_same_thred":False})

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()