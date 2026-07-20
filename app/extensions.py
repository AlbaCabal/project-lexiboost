from datamuse import Datamuse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Create db instance globally, but do not bind to app yet
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

api = Datamuse()