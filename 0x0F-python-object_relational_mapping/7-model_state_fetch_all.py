#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
import sys
from sqlalchemy import create_engine
from model_state import State, base
from sqlalchemy.orm import sessionmaker


k = create_engine('mysql=mysqldb://{}:{}@localhost:2206/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
l = sessionmaker(bind=engine)
m = l()
i = l.query(State).all()
for j in i:
    print(j.id, j.name, sep=': ')
