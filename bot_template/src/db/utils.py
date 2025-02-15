from sqlalchemy import create_engine
import pandas as pd
from loguru import logger
import json
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker


with open('config.json', 'r') as f:
    config = json.load(f)['postgres']

engine = create_engine("postgresql://{user}:{password}@{host}:{port}/{db}".format(
    host=config['host'],
    db=config['db'],
    user=config['user'],
    port=config['port'],
    password=config['password']
), client_encoding='utf8')
Session = sessionmaker(bind=engine)


def fetch_df_by_query(conn, query):
    res = conn.execute(text(query))
    data = res.fetchall()
    return pd.DataFrame(data, columns=res.keys())


def get_connection():
    return engine.connect()


def get_session():
    return Session()


if __name__ == '__main__':
    conn = get_connection()
