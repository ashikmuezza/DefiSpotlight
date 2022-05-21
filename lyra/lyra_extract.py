import streamlit as st
import plost
import datetime
from dune import getdata
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def lyra_home():
    st.markdown('#')

    Lyra_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">Lyra is an open protocol for trading options built on Ethereum. Lyra allows traders to buy and sell options that are accurately priced with the first market-based, skew adjusted pricing model..</p>'
    st.markdown(Lyra_title, unsafe_allow_html=True)

    st.markdown('#')

    st.header('Lyra Overall Metrics')

    st.markdown('#') 
    

    NotionalVolume = getdata(257373)
    PremiumTraded = getdata(163118)

    
    col1, col2 , col3, col4  = st.columns((4,4,4,4))

    col1.metric(label = "Notional Volume", value = '$'+ str(  int(NotionalVolume["totalnotional"])) + "M")
    col2.metric(label = "Premium Volume", value = '$'+ str( "{:,}".format(int(PremiumTraded["total_susd_volume"] )) ))
    
    col3.metric(label = "Total Trades", value = str("{:,}".format(int(PremiumTraded["total_trades"]))))
    col4.metric(label = "Unique Trades", value = str("{:,}".format(int(PremiumTraded["unique_traders"]))))

    data = connect('db/lyra.db')

    st.markdown('#')
    st.markdown('#')

    line_chart_multi(data, 'Lyra_notational_volume_by_assets', 'times','totalCost','market' , 'Lyra notational volume by assets')

   
    st.markdown('#')

    st.markdown('#') 
    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'unique_traders', 'times','UniqueTraders', 'Daily Unique Traders')
    with col2:
        line_chart(data, 'unique_traders', 'times', 'totalTrades', 'Total Traders By Day')

    line_chart(data, 'unique_traders', 'times', 'avgTrades', 'AVG Traders')
   
    


    st.markdown('#') 
    col1, col2 = st.columns((2,2))
    with col1:
         pie_chart(data, 'lyra_top_50_traders_profit', 'totalrealizedprofit', 'trader', 'Lyra Top 50 traders profit')
    with col2:
        pie_chart(data, 'lyra_top_50_traders_volume', 'premiums', 'trader', 'Lyra Top 50 traders volume')


    st.markdown('#') 

    col1, col2 = st.columns((2,2))

    with col1:

        line_chart(data, 'Lyra_btc_marketpool', 'evt_block_time', 'Price', 'Lyra_btc_marketpool_price')
   
    with col2:

        line_chart(data, 'Lyra_btc_marketpool', 'evt_block_time', 'pool_value', 'Lyra_btc_marketpool_price')

    st.markdown('#') 
    col1, col2 = st.columns((2,2))

    with col1:

        line_chart(data, 'Lyra_eth_marketpool', 'evt_block_time', 'Price', 'Lyra_eth_marketpool_price')
   
    with col2:

        line_chart(data, 'Lyra_eth_marketpool', 'evt_block_time', 'pool_value', 'Lyra_eth_marketpool_pool_value')

    st.markdown('#') 
    col1, col2 = st.columns((2,2))

    with col1:

        line_chart(data, 'Lyra_link_marketpool', 'evt_block_time', 'Price', 'Lyra_link_marketpool_price')
   
    with col2:

        line_chart(data, 'Lyra_link_marketpool', 'evt_block_time', 'pool_value', 'Lyra_link_marketpool_pool_value')

    st.markdown('#') 
    st.subheader("Lyra Recent Trade History")
    st.dataframe(table(data,'Lyra_trade_history'))

    st.markdown('#') 

    line_chart(data, 'lyra_susd_volume', 'day', 'total_susd_volume', 'Lyra sUSD Volume')

    pie_chart(data, 'lyra_profitable_traders', 'trader', 'totalrealizedprofit', 'Lyra Profitable Traders')

    pie_chart(data, 'lyra_high_volume_traders', 'trader', 'notional', 'Lyra High Volume Traders')

