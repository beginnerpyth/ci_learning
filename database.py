from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class base(BaseModel):
    pass


class tablemaker(DeclarativeBase):
    pass


class Settings(BaseSettings):
    database: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

db_connector = create_engine(settings.database)
db_creator = sessionmaker(bind=db_connector)


def db():
    db_created = db_creator()  # so when user calls it gets it own isolated connection
    try:
        yield db_created
    finally:
        db_created.close()


# haha
