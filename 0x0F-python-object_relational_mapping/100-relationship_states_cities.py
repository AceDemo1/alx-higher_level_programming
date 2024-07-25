#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == '__main__':
    k = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                      .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(k)
    sess = sessionmaker(bind=k)
    m = sess()
    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)
    m.add(state)
    m.commit()
    m.close()
