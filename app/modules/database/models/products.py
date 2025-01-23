from sqlalchemy import BIGINT, VARCHAR, Column, Float, Integer
from sqlalchemy.orm import relationship

from ..core import Base


class Product(Base):
    __tablename__ = "products"

    artikul = Column(BIGINT, primary_key=True, index=True)
    name = Column(VARCHAR(255), nullable=False)
    price_in_copecs = Column(Integer, nullable=False)
    rate = Column(Float, nullable=False)
    total_quantity = Column(Integer, nullable=False)

    subscribes = relationship("Subscribe", back_populates="product")
