import os
from dotenv import load_dotenv

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DB = os.getenv("PG_DB")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")

PG_DSN = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"


engine = create_async_engine(PG_DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class SwapiPeople(Base):
    __tablename__ = "swapi_people"
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(60))
    eye_color = Column(String(60))
    films = Column(String(300))
    gender = Column(String(60))
    hair_color = Column(String(60))
    height = Column(String(60))
    homeworld = Column(String(60))
    mass = Column(String(60))
    name = Column(String(60))
    skin_color = Column(String(60))
    species = Column(String(300))
    starships = Column(String(300))
    vehicles = Column(String(300))













