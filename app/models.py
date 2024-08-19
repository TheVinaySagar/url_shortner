from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class URLModel(Base):
    __tablename__ = 'urls'
    
    id = Column(Integer, primary_key=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, nullable=False)

# Other models can be defined here
