import streamlit as st
import plost
import datetime
from dune import getdata_fromdune
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def dydx_extract():
    st.markdown('#') 
    top_trend = '<p style="font-family:Courier; color:violet; font-size: 25px;">dYdX (DYDX) is a decentralized exchange platform for cryptocurrency margin trading for assets like BTC, ETH, SOL, DOT, and more. The bulk of dYdX crypto margin trading products reside atop the Ethereum blockchain. However, the exchange recently rolled out on Layer 2 for instantly settled, inexpensive trades..</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('#') 

    st.header('DYDX STATS')

    st.markdown('#') 

    grater_then_zero = getdata_fromdune(427692)
    grater_then_thousand = getdata_fromdune(427694)
    grater_then_hun_thousand = getdata_fromdune(427697)
    
    col1, col2, col3 = st.columns((3,3,3))
    col1.metric(label = "Wallets with > 0 Address (DYDX)", value = str(int(grater_then_zero.values)) )
    col2.metric(label = "Wallets with > 1000 Address (DYDX)", value = str(int(grater_then_thousand.values )) )
    col3.metric(label = "Wallets with > 100,000 Address (DYDX)", value = str(int(grater_then_hun_thousand.values)))

    st.markdown('#') 
    data = connect('db/DYDX.db')

    line_chart(data, 'DYDX_daily_user', 'date', 'daily_users', 'DYDX Daily New Users')
    st.markdown("#")
    line_chart(data, 'DYDX_daily_volume', 'date', 'usd_volume', 'DYDX Daily Volume')
    st.markdown("#")
    line_chart(data, 'DYDX_daily_transcation_count', 'date_trunc', 'count', 'DYDX_daily_transaction_count')

    

    st.title("Staking Stats")
    unique = getdata_fromdune(233667)
    unique_value = unique['unique_stakers'].iloc[0]

    st.markdown('#') 

    col1, col2= st.columns((2,2))
    col1.metric(label = "dydx_USDC Unique Stakers", value = str(int(unique_value)) )
    col2.metric(label = "dydx_USDC Staked Current Balance", value = "$"+str(int(getdata_fromdune(233683).values )) )

    st.markdown('#') 

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'DYDX_usdc_stacked', 'day', 'usdc_staked', 'DYDX_USDC_Staked')
    with col2:
        bar_chart_vertical(data, 'DYDX_amount_of_withdraw', 'day', 'staked_requested_withdraw', 'DYDX_Amount_Requested_Withdraw')

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'DYDX_daily_stakers', 'day', 'stakers', 'DYDX Daily Stakers')
    with col2:
        pie_chart(data, 'DYDX_staked_usdc', 'sum', 'staker', 'DYDX_Staking_Wallets')

    st.title("Token Stats")

    st.markdown('#') 

    col1, col2 = st.columns((2,2))
    with col1:
        st.dataframe(table(data, 'DYDY_token_holders'))
    with col2:
        line_chart(data, 'DYDX_token_price', 'minute', 'price', 'Token Price')
    
    st.markdown('#') 
    line_chart(data, 'DYDX_daily_buy_on_dex', 'date', 'unique_wallet_count', 'Unique Wallet Counts')
    line_chart(data, 'DYDX_daily_buy_on_dex', 'date', 'trade_count', 'Trade_counts')
    st.markdown('#') 
    line_chart(data, 'DYDX_active_users', 'time', 'New', 'Active New Users')


    