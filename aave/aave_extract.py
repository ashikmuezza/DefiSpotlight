import streamlit as st
import plost
import altair as alt
import datetime
from dune import getdata
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def aave_extract():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">Aave is a decentralized lending system that allows users to lend, borrow and earn interest on crypto assets, all without middlemen. It is a fully decentralized, community governed protocol with 110,597 token holders.  Aave currently supports several cryptocurrencies built on top of the Ethereum blockchain, and the range of services is constantly growing.</p>'
    
    st.markdown(Defi_title, unsafe_allow_html=True)

    data = connect('db/aave.db')

    st.markdown('#')
    st.markdown('#')

    line_chart_multi(data, 'Aave_polygon_one_day_transaction_count', 'dt','transactions','account' , 'Aave Polygon Transcation details')
    
    st.markdown('#') 

    col1, col2 = st.columns((2,2))
    with col1:
        bar_chart_vertical(data, 'Aave_polygon_active_users', 'dt', 'cumulative_total', 'Aave Users Cummulative')
    with col2:
        line_chart(data, 'Aave_polygon_active_users', 'dt', 'total_users', 'Aave Daily Users')
   

    st.markdown('#')
    st.markdown('#')

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart_multi(data, 'Aave_polygon_borrow_volume', 'dt','volume','symbol' , 'Aave Polygon Borrow Volume')
    with col2:
        line_chart_multi(data, 'Aave_polygon_deposit_volume', 'dt','volume','symbol' , 'Aave Polygon Deposit Volume')
   
    
    st.markdown('#')
    st.markdown('#')

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart_multi(data, 'Aave_polygon_flash_loan_volume', 'dt','volume','symbol' , 'Aave Polygon Flash Loan Volume')
    with col2:
        line_chart_multi(data, 'Aave_polygon_liqudation_volume', 'dt','volume','symbol' , 'Aave Polygon Liqudation Volume')
    
    
    
    st.markdown('#')
    st.markdown('#')

    line_chart_multi(data, 'Aave_polygon_repay_volume', 'dt','volume','symbol' , 'Aave Polygon Repay Volume')


    st.markdown('#')
    st.markdown('#')

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart_multi(data, 'Aave_polygon_transaction_volume', 'dt','volume','symbol' , 'Aave Polygon Transaction Volume')
    with col2:
        line_chart_multi(data, 'Aave_polygon_withdraw_volume', 'dt','volume','symbol' , 'Aave Polygon Withdraw Volume')
    
    

    st.markdown('#') 
    st.subheader("Aave Polygon Financial Statements")
    st.dataframe(table(data,'Aave_v3_Polygon_Financial_Statements'))

    
   



