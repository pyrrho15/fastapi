from sqlalchemy import column, create_engne, Column, Integer, String, true
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL="sqlite:///./test.db"

engine = create_engine(DB_URL, connect_args={"check_same_thread":False})

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__="todos"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    completed=Column(String)

Base.metadata.create_all(bind=engine) 