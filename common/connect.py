import sqlite3
from sqlite3 import Connection
import pandas as pd
import plost



def connect(db_link):
    data = sqlite3.connect(db_link, check_same_thread=False)
    return data
    
def line_chart(data, table, x, y, title):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)

    if 'time' in df:
        df['time'] = pd.to_datetime(df['time'])
    # df['time'] = df['time'].dt.date
    plost.line_chart(
        df,
        x=x,
        y=y,width=500, height=400, title=title)

def line_chart_multi(data, table, x, y, project, title):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)

    if 'time' in df:
        df['time'] = pd.to_datetime(df['time'])
   
    plost.line_chart(
        df,
        x=x,
        y=y,
        color=project,
        width=500, height=400, title=title)

def bar_chart(data, table, x, y):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)
    plost.bar_chart(
    data=df,
    bar=x,
    value=y, direction='horizontal')

def pie_chart(data, table, x, y, title):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)
    plost.pie_chart(
    data=df,
    theta=x,
    color=y, width=500, height=400, title=title)

def table(data, table):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)
    return df
    
