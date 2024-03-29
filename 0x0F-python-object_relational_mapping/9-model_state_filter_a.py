#!/usr/bin/python3
"""Lists all State Objects from database hbtn_0e_6_usa
that contain the letter a
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

    for instance in session.query(State).\
            filter(State.name.like('%a%')).order_by(State.id):
        print(f"{instance.id}: {instance.name}")
