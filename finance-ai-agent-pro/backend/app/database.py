from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./finance.db")
SessionLocal = sessionmaker(bind=engine)
