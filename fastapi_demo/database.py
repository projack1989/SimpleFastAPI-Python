# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "mysql+pymysql://debian-sys-maint:yIyZ7p37Gum5tikJ@localhost/fastapi_demo"

engine = create_engine(
    DATABASE_URL, 
    #connect_args={"check_same_thread": False}
    echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
