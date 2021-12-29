import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import cx_Oracle
import sys
import os

try:
    if sys.platform.startswith("darwin"):
        lib_dir = os.path.join(os.environ.get("HOME"), "Downloads",
                               "instantclient_19_8")
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    elif sys.platform.startswith("win32"):
        lib_dir = r"$HOME/Downloads/instantclient_19_8"
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
except Exception as err:
    print("Whoops!")
    print(err);
    sys.exit(1);

engine = sa.create_engine('oracle://minhdt:minhdt123@localhost:1521/ORCLCDB', echo=True)
session = sa.orm.scoped_session(sa.orm.sessionmaker(bind=engine))

Base = declarative_base()
Base.query = session.query_property()
