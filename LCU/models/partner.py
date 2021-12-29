from sqlalchemy import Column, Integer, String, Text
from base import Base, engine

class Partner(Base):
    __tablename__ = 'partner'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

Base.metadata.create_all(engine)
