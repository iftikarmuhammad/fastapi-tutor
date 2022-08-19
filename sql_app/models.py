from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .database import Base


class Shortener(Base):
    __tablename__ = "shortener"

    # id = Column(Integer, primary_key=True, index=True)
    shortId = Column(String, unique=True, primary_key=True, index=True)
    url = Column(String)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())