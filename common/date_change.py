import pandas as pd

def date_change(df):
    if 'time' in df :
        df['time'] = pd.to_datetime(df['time'])

    if 'date' in df :
        df['date'] = pd.to_datetime(df['date'])

    if 'date_trunc' in df:
        df['date_trunc'] = pd.to_datetime(df['date_trunc'])
    
    if 'day' in df:
        df['day'] = pd.to_datetime(df['day'])