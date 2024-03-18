#!/usr/bin/python3
"""Delete all State objects with name containing letter a
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

    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    session.commit()
    session.close()
