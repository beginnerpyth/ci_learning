from sqlalchemy import Table,Integer,Column,String,create_engine
from sqlalchemy.orm import sessionmaker,Session,DeclarativeBase
from pydantic_settings import BaseSettings
from pydantic import BaseModel


class base(BaseModel):
    pass 

class tablemaker(DeclarativeBase):
    pass

class Settings(BaseSettings):
    database:str

    class Config():
        env_file='.env'
settings=Settings()

db_connector=create_engine(settings.database)
db_creator=sessionmaker(bind=db_connector)
def db():
    db_created=db_creator()
    try:
        yield db_created
    finally:
        db_created.close()





