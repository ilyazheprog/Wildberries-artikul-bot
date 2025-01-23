from sqlalchemy import BIGINT, VARCHAR, Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..core import Base


class Subscribe(Base):
    __tablename__ = "subscribes"

    id = Column(Integer, primary_key=True, index=True)
    artikul = Column(ForeignKey("products.artikul"), nullable=False)
    last_update = Column(DateTime, nullable=False, default=func.now())

    product = relationship("Product", back_populates="subscribes")
