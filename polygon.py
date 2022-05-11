import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

db_path_polygon = "db/polygon.db"

@st.cache(allow_output_mutation=True)
def get_connection(path: str):
    return sqlite3.connect(path, check_same_thread=False)

def get_data(table_name,table_type,title,chart_type):
    conn = get_connection(db_path_polygon)
    query = "SELECT * from "+table_name
    df = pd.read_sql(query, con=conn)

    if chart_type == 'Line':
        if table_type == 'Project':
            dff = pd.DataFrame({'date':df['time'].to_list(),'data':df['volume'],'project':df['project']},columns=['date','data','project'])
            color = alt.Color("project:N")
        else:
            dff = pd.DataFrame({'date':df['time'].to_list(),'data':df['volume']},columns=['date','data'])  
            color = alt.Color(legend=None)
        
        basic_chart = alt.Chart(dff).mark_line(color="Yellowgreen").encode(
        x=alt.X('date:T', axis=alt.Axis(titleFontSize=12, title='Time →', labelColor='#999999', titleColor='#999999', titleAlign='right', titleAnchor='end', titleY=45)),
        y=alt.Y('data:Q', axis=alt.Axis(format="$s", tickCount=3, titleFontSize=12, title='Volume →'   , labelColor='#999999', titleColor='#999999', titleAnchor='end')),
        color=color
        ).properties(    title = title,
        width=1100,
        height=400).interactive()

        return basic_chart
    
    elif chart_type == 'Donut':
        if table_type == 'Project':
            dff = pd.DataFrame({'volume':df['volume'],'project':df['project'],'time':df['time']},columns=['volume','project','time'])
            dff = dff.groupby(by=["project"])['volume'].sum().reset_index() 
            fig = go.Figure(    
            go.Pie(
            labels = dff['project'].tolist(),
            values = dff['volume'].tolist(),
            hoverinfo = "label+percent",
            hole = 0.2,
            textinfo = "value",))

            fig.update_layout(title="DEX Marketshare based on Trading Volume",height=400,width = 570)
            return fig

        else:
            dff = pd.DataFrame({'Marketshare':df['Marketshare'],'Project':df['Project']},columns=['Marketshare','Project'])        
            fig = go.Figure(
            go.Pie(
            labels = dff['Project'].tolist(),
            values = dff['Marketshare'].tolist(),
            hoverinfo = "label+percent",
            hole = 0.2,
            textinfo = "value",))

            fig.update_layout(title="DEX Marketshare by Volume Past week",height=400,width = 570)
            return fig
        
    elif chart_type == 'Table':
        if table_type == 'Project':
            dataframe = df
            dataframe = dataframe.groupby(by=["project"])['volume'].sum().reset_index() 
            return dataframe
        else:
            dataframe = df
            return dataframe


