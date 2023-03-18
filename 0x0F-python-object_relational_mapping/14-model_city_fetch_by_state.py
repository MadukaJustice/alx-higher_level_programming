#!/usr/bin/python3
"""
     lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(City, State).filter(City.state_id == State.id)\
                    .order_by(City.id).all()

    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
