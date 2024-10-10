from database.database import Base
import sys
import os

from sqlalchemy import Column, Integer, String

# 프로젝트 루트 디렉토리를 sys.path에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Beverage(Base):
    __tablename__ = "beverage"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Beverage(id={self.id}, name={self.name}, quantity={self.quantity})>"


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    storage = Column(bool, nullable=False)

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, storage={self.storage})>"
