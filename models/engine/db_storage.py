#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage():
    user = os.environ["HBNB_MYSQL_USER"]
    passwd = os.environ["HBNB_MYSQL_PWD"]
    host = os.environ["HBNB_MYSQL_HOST"]
    db_name = os.environ["HBNB_MYSQL_DB"]

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, pwd, host, db_name))

    if os.environ("HBNB_ENV") == 'test':
        City.__table__.drop()
        print("")
