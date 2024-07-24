#!/usr/bin/python3
""" Prints the State object with the name passed as argument from the database,
or updates the State object with id 2 to 'New Mexico'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Update state with id 2
    state_id = 2
    new_name = 'New Mexico'
    state_to_update = session.query(State).filter_by(id=state_id).first()
    if state_to_update:
        state_to_update.name = new_name
        session.commit()
        print(f"State updated: {state_to_update.id}: {state_to_update.name}")
    else:
        print("State not found.")

    # Alternatively, find a state by name
    if len(sys.argv) > 4:
        state_name = sys.argv[4]
        state = session.query(State).filter_by(name=state_name).first()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Not found")
    
    session.close()

