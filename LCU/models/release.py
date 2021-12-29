from sqlalchemy import Column, Integer, String, Text

from base import Base, engine


class Release(Base):
    __tablename__ = 'release'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    version = Column(String, nullable=False)
    note = Column(Text)


Base.metadata.create_all(engine)
