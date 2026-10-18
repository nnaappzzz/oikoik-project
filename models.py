from sqlalchemy import Column, Integer, String, Float, DateTime, Enum as SQLEnum
from datetime import datetime
from database import Base
from enum import Enum

class NamaBarangEnum(str, Enum):
    BARANG_A = "Telur Pack A"
    BARANG_B = "Telur Pack B"

class SalesModel(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    item_name = Column(SQLEnum(NamaBarangEnum), index=True)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)