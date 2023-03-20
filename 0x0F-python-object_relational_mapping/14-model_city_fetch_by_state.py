#!/usr/bin/python3

""" 7-model_state_fetch_all module """

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State
    from model_city import City

    inp = sys.argv
    if len(inp) < 4:
        exit(1)
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    output = session.query(State.name, City.id, City.name) \
                    .join(City, State.id == City.state_id) \
                    .order_by(City.id).all()

    for city in output:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    session.close()
