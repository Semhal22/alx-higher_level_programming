#!/usr/bin/python3
"""Change name of a State object
from database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, pwrd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    path = f'mysql+mysqldb://{user}:{pwrd}@localhost/{db}'
    engine = create_engine(path, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter_by(id=2).first()
    instance.name = 'New Mexico'

    session.commit()
