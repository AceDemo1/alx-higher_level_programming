#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch and print state with id = 2
    state = session.query(State).filter(State.id == 2).first()
    if state:
        print(f"Original state name: {state.name}")
        state.name = "New Mexico"
        session.commit()
    session.close()

