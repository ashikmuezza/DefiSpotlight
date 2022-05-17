import streamlit as st
import plost
import datetime
from dune import getdata_fromdune
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def badger_extract():
    st.markdown('#') 
    top_trend = '<p style="font-family:Courier; color:violet; font-size: 25px;">Badger DAO is a decentralized autonomous organization (DAO) that enables bitcoin to be used as collateral across decentralized finance (DeFi) applications..</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('#') 

    st.header('Badger STATS')

    st.markdown('#') 
    col1, col2, col3 = st.columns((3,3,3))
    col1.metric(label = "wallet > 0 (Badger)", value = str(int(getdata_fromdune(501694).values)) )
    col2.metric(label = "wallet > 1000 (Badger)", value = str(int(getdata_fromdune(501701).values)) )
    col3.metric(label = "wallet > 100,000 (Badger)", value = str(int(getdata_fromdune(501703).values)))

    st.subheader("Badger Token")
    data = connect('db/badger.db')

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'Badger_token_daily_active_users', 'time', 'New', "Badger_token_daily_active_users")
    with col2:
        line_chart(data, 'Badger_token_daily_new_account', 'Date', 'new', 'Badger_token_daily_new_account')

    st.markdown("#")
    line_chart_multi(data, 'Badger_token_daily_buys', 'day', 'volume','project', "Badger_token_daily_buys")
    st.markdown("#")

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data,'Badger_token_total_users','date', 'total_users', 'Badger_token_total_users')
        
    with col2:
        pie_chart(data, 'Badger_token_dex_volume', 'seven', 'Project', 'Badger_token_dex_volume')

    line_chart(data, 'Badger_token_transactions','date_trunc', 'count','Badger_token_transactions')

    st.markdown("#")

    st.subheader("DIGG")

    line_chart_multi(data,'Digg_trading_volume','day', 'usd_volume','project', 'Digg_trading_volume')

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data,'Digg_uniswap_users_over_time', 'date','diggunilp_sett_users','Digg_uniswap_users_over_time')
   
    with col2:
        line_chart(data, 'Digg_susi_users_over_time', 'date', 'diggsushilp_sett_users', 'Digg_susi_users_over_time')

    line_chart(data, 'Digg_users_over_time', 'date', 'digg_users', 'Digg_users_over_time')

    st.markdown("#")
    st.subheader("ibBTC")
    line_chart(data, 'ibBTC_supply', 'hour', 'max_total_supply_ibbtc', 'ibBTC_supply')

    st.markdown("#")
    st.subheader("Gas Fee")

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data,'weekly_gas_usage', 'week','gas_spent_eth','weekly_gas_usage')
   
    with col2:
        line_chart_multi(data, 'weekly_gas_usage_per_type', 'week', 'sum','wallet_type' ,'weekly_gas_usage_per_type')

    st.markdown("#")
    st.subheader("Badger_Sett_TVL")
    st.dataframe(table(data,'Badger_Sett_TVL'))



    