#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    k = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                      .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(k)
    sess = sessionmaker(bind=k)
    m = sess()
    row = m.query(State.name, City.id, City.name)\
         .filter(State.id == City.state_id).order_by(City.id).all()
    for i, j, k in row:
        print(i + ': (' + str(j) + ') ' + k)
    m.close()
