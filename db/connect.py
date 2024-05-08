import sqlalchemy.orm
import sqlalchemy.ext.declarative
import sqlalchemy_utils

from project.db import config
from project.db import tables

DATABASE_URL = config.settings.DATABASE_URL
engine = sqlalchemy.create_engine(DATABASE_URL)

is_database = sqlalchemy_utils.database_exists(engine.url)
if not is_database:
    sqlalchemy_utils.create_database(engine.url)

tables.metadata.create_all(engine)

SessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.orm.declarative_base()

