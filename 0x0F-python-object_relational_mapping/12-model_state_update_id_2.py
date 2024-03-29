#!/usr/bin/python3
"""
changes the name of the State object where id=2 to New Mexico from a database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))

    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()

