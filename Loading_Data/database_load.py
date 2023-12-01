from sqlalchemy import create_engine
import pymysql
import pandas as pd

db_connection = 'mysql+pymysql://mysql_user:mysql_password@mysql_host/mysql_db'
conn = create_engine(db_connection)

df = pd.read_sql("select * from table", conn)
