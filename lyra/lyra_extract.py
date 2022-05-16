import streamlit as st
import plost
import datetime
from dune import getdata_fromdune
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def lyra_home():
    st.markdown('#')

    Lyra_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">Lyra is an options trading protocol accessing the scalability of Layer 2 Ethereum to provide a robust, lightning-fast and reliable trading experience.</p>'
    st.markdown(Lyra_title, unsafe_allow_html=True)

    st.markdown('#')

    st.header("Why is Lyra important?")

    top_trend = '<p style="font-family:Courier; color:violet; font-size: 20px;">Lyra is designed and coded from the ground up, which allows to include most recent achievements in blockchain technologies. Those new technologies in turn allow to implement features that prevent mass adoption of most existing blockchains by mainstream: very high scalability, instant authorizations and settlements, super light clients, no chargebacks, no locked balances, native multi-token (i.e. multi currency) support, built-in decentralized exchange, and more.</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('#')

    st.header('Lyra Overall Metrics')

    st.markdown('#') 
    

    NotionalVolume = getdata_fromdune(257373)
    PremiumTraded = getdata_fromdune(163118)

    
    col1, col2 , col3, col4  = st.columns((4,4,4,4))

    col1.metric(label = "Notional Volume", value = '$'+ str(  int(NotionalVolume["totalnotional"])) + "M")
    col2.metric(label = "Premium Traded", value = '$'+ str( "{:,}".format(int(PremiumTraded["total_susd_volume"] )) ))
    
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
        line_chart(data, 'Lyra_unique_users', 'times','UniqueTraders', 'Daily Unique Traders')
    with col2:
        bar_chart_vertical(data, 'Lyra_unique_users', 'times', 'cumUniqueTraders', 'Lyra Total Users')

    
   
    st.markdown('#')
    line_chart_multi(data, 'Lyra_trade_history', 'evt_block_time','totalCost','market' , 'Daily Unique Traders')


    st.markdown('#') 
    col1, col2 = st.columns((2,2))
    with col1:
         pie_chart(data, 'lyra_top_50_traders_profit', 'totalrealizedprofit', 'trader', 'Lyra Top 50 traders profit')
    with col2:
        pie_chart(data, 'lyra_top_50_traders_volume', 'premiums', 'trader', 'Lyra Top 50 traders volume')


    st.markdown('#') 

    col1, col2 = st.columns((2,2))

    df = table(data,'lyra_btc_marketpool')
    col1.header('Lyra BTC Marketpool')
    with col1:

        st.dataframe(df,500, 300)

    df = table(data,'lyra_eth_marketpool')
    col2.header('Lyra ETH Marketpool')
    with col2:
        st.dataframe(df,500, 300)

    df = table(data,'lyra_link_marketpool')
    st.header('Lyra Link Marketpool')
    st.dataframe(df,500, 300)    

    # st.markdown('#') 
    # line_chart(data, 'lyra_btc_marketpool', 'evt_block_time','Price', 'lyra_btc_marketpool')