from models import db
from sqlalchemy.orm import sessionmaker


def pegar_sessao():
    Session = sessionmaker(bind=db) 
    session = Session()
    yield session
    session.close()