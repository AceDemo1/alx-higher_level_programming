#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        return

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and session
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_password}@localhost:3306/{database_name}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Update State with id = 2
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State with id 2 not found.")

    # Close session
    session.close()

if __name__ == "__main__":
    main()

