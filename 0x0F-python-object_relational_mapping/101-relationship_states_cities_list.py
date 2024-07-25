#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
import sys
from sqlalchemy import create_engine
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    k = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                      .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(k)
    sess = sessionmaker(bind=k)
    m = sess()
    row = m.query(State).all()
    for j in row:
        print(j.id, j.name, sep=': ')
        for k in j.cities:
            print('\t' + j.k.id + ': ' + k.name)
    m.close()
