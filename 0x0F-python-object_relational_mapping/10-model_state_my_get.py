#!/usr/bin/python3
"""Print  State Object with name passed as an argument
from database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, pwrd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]
    path = f'mysql+mysqldb://{user}:{pwrd}@localhost/{db}'
    engine = create_engine(path, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(State.name == state_name).first()
    if instance:
        print(instance.id)
    else:
        print("Not found")
