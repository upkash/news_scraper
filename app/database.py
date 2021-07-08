
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import base

engine = create_engine('sqlite:///storage.db')

base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session() 