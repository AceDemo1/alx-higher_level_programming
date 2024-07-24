#!/usr/bin/python3
"""Change the name of the State object with id = 2 to New Mexico in the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class and a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State with id = 2
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    session.close()
