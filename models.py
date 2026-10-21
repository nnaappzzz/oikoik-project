from sqlalchemy import Column, Integer, String, Float, DateTime, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from enum import Enum


class NamaBarangEnum(str, Enum):
    BARANG_A = "Telur Pack A"
    BARANG_B = "Telur Pack B"

# [SALES]

class SalesModel(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    item_name = Column(SQLEnum(NamaBarangEnum), index=True)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)

class AreaModel(Base):
    # {nama tabel}
    __tablename__ = 'AREA'
    # {stuktur tabel}
    id = Column(Integer, primary_key=True, index=True)
    AREA = Column(String, nullable=True)
    # {relasi tabel}
    TOKO = relationship("TokoModel",back_populates="AREA")

class TokoModel(Base):
    # {nama tabel}
    __tablename__ = 'TOKO'
    # {stuktur tabel}
    id = Column(Integer, primary_key=True, index= True)
    NAMA = Column(String, nullable=False)
    LONGITUDE = Column(Float, nullable=False)
    LATITUDE = Column(Float, nullable=False)
    CREATED_AT = Column(DateTime, default=datetime.utcnow)
    UPDATED_AT = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # {relationship}
    AREA_ID = Column(Integer, ForeignKey("AREA.id"))
    AREA = relationship("AreaModel", back_populates="TOKO")