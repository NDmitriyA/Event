from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text



SW_DNS = f'postgresql+asyncpg://postgres:12345@127.0.0.1:5431/db_swapi'
engine = create_async_engine(SW_DNS)
Base = declarative_base(sbind=engine)
Session = sessionmaker(engine, class_=AsyncSession,expire_on_commit=False)


class PersonalModel(Base):
    __tablename__ = 'swapi'

    id = Column(Integer, primary_key=True)
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(Text)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(Text)
    starships = Column(Text)
    vehicles = Column(Text)