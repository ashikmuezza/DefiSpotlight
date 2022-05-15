import pandas as pd

def date_change(df):
    if 'time' in df :
        df['time'] = pd.to_datetime(df['time'])
    
    if 'hour' in df :
        df['hour'] = pd.to_datetime(df['hour'])

    if 'date' in df :
        df['date'] = pd.to_datetime(df['date'])
    
    if 'Date' in df :
        df['Date'] = pd.to_datetime(df['Date'])

    if 'date_trunc' in df:
        df['date_trunc'] = pd.to_datetime(df['date_trunc'])
    
    if 'day' in df:
        df['day'] = pd.to_datetime(df['day'])
    
    if 'minute' in df:
        df['minute'] = pd.to_datetime(df['minute'])
    
    if 'dt' in df:
        df['dt'] = pd.to_datetime(df['dt'])