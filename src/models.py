from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float, Text, DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime




class Base(DeclarativeBase):
    pass


class RegORM(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)



class DonateRb(Base):
    __tablename__ = "donate_rb"
    id = Column(Integer, primary_key=True, index=True)
    RB_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cardnumber = Column(String, nullable=False)
    donate = Column(Integer, nullable=False)



class DonateSteam(Base):
    __tablename__ = "donate_steam"
    id = Column(Integer, primary_key=True, index=True)
    steam_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cardnumber = Column(String, nullable=False)
    donate = Column(Integer, nullable=False)


class DonateBrawl(Base):
    __tablename__ = "donate_brawl"
    id = Column(Integer, primary_key=True, index=True)
    brawl_id = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cardnumber = Column(String, nullable=False)
    donate = Column(Integer, nullable=False)

