import streamlit as st
import plost
import datetime
from metrics import getdata
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def olympus_extract():
    st.markdown('#') 
    top_trend = '<p style="font-family:Courier; color:violet; font-size: 25px;">Olympus DAOs decentralized reserve OHM currency is intended to wean crypto markets off their unhealthy addiction to US dollars. The point of OHM is to act as a store of value, not pegged to the $1 mark as are USDT, USDC, and others..</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    data = connect("db/olympus.db")

    supply = getdata(28599)
    marketcap = getdata(28707)

    col1, col2 = st.columns((2,2))
    col1.metric(label = "Marketcap (OHM)", value ='$'+str(int(marketcap['Market Cap'].iloc[0])) )
    col2.metric(label = "Circulating Supply / Total Supply (OHM)", value = supply['Circulating Supply / Total Supply'].iloc[0] )

    line_chart(data,'OlympusDAO_total_wallet_count', 'Date', 'Number of Wallets', 'OlympusDAO_total_wallet_count')
    line_chart(data,'OlympusDAO_total_wallet_count', 'Date', '# of New Users', 'OlympusDAO_new_users_count')

    col1, col2 =st.columns((2,2))
    with col1:
        line_chart(data, 'OHM_price_marketcap', 'date', 'price', 'OHM_Price')
        line_chart(data, 'OHM_wallet_distribution', 'Date', '# of Active Users', 'OHM Active Users')
        line_chart(data, 'OHM_holders_over_time', 'Date', 'OHM Holders', 'OHM Holders Over Time')
    with col2:
        line_chart(data, 'OHM_price_marketcap', 'date', 'Market Cap', 'OHM_Market Cap')
        line_chart(data, 'OHM_wallet_distribution', 'Date','# of Transactions', 'OHM Transcation_counts')
        pie_chart(data,'Active_Ohm_Stakers','# of Active Users', 'Event', 'Active_Ohm_Stakers')
    
    line_chart_multi(data,'OHM_liqudity_owned', 'date', 'liquidity', 'symbol', 'OHM Liqudity Owned')

    st.subheader('OHM_Treasury_Breakdown_By_Asset_Type')
    st.dataframe(table(data,'OHM_Treasury_Breakdown_By_Asset_Type'))

    line_chart(data, 'OHM_Treasury_Breakdown_By_Asset_Type', 'date', 'weth', 'weth')