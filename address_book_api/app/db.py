from sqlalchemy import create_engine, MetaData
from databases import Database

SQLALCHAMY_DATABASE_URL = 'sqlite:///./addressbook.db'

# SQLAlchemy
engine = create_engine(SQLALCHAMY_DATABASE_URL)
metadata = MetaData()

# database query builder
database = Database(SQLALCHAMY_DATABASE_URL)
