#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base  # Ensure 'Base' is imported correctly

if __name__ == '__main__':
    # Create engine and connect to the MySQL server
    k = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                      .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create all tables in the database
    Base.metadata.create_all(k)

    # Create a configured "Session" class
    l = sessionmaker(bind=k)

    # Create a session
    m = l()

    # Query all State objects
    i = m.query(State).all()  # Use the session instance 'm'

    # Print the states
    for j in i:
        print(f"{j.id}: {j.name}")

    # Close the session
    m.close()

