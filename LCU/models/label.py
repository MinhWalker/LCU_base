from sqlalchemy import Column, Integer, String
from base import Base, engine


class Label(Base):
    __tablename__ = 'label'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)


Base.metadata.create_all(engine)
