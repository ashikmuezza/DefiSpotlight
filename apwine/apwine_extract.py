from get_data import Aave_pools
import streamlit as st
import plost
import altair as alt
import datetime
from metrics import getdata
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *
from pandas import json_normalize


def apwine_extract():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">APWine is a protocol to trade future yield. DeFi users can deposit their interest bearing tokens of other protocols during defined future periods and trade in advance the future yield that their funds will generate. The APWine Protocol can tokenize the yield generated by interest-bearing tokens. It does this by splitting interest-bearing assets into Principal Tokens and Future Yield Tokens.    </p>'
    
    st.markdown(Defi_title, unsafe_allow_html=True)

    data = connect('db/apwine.db')


    Volume = getdata(749816)

    st.markdown('#')


    st.subheader("Token Metrics on Ethereum")
    st.markdown('#')
    col1, col2 , col3  = st.columns((3,3,3))

    col1.metric(label = "Fully Diluted Market Cap", value = '$ '+  str("{:,}".format(int(Volume["marketcap"]))) )

    col2.metric(label = "Total Token Supply", value = str("{:,}".format(int(Volume["supply"]))) )
    
    col3.metric(label = "Holders on Ethereum", value =  Volume["holders"] )

    st.markdown('#')

    col1, col2 , col3  = st.columns((3,3,3))

    col1.metric(label = "Circulating Supply", value = str("{:,}".format(int(Volume["circ_supply"]))) )

    col2.metric(label = "Total Traded Volume", value = '$ '+   str("{:,}".format(int(Volume["traded_volume"]))) )
    
    col3.metric(label = "$APW Price", value =  '$ '+ "{:.2f}".format(float(Volume["price"])))

    st.markdown('#')
    st.markdown('#')
    line_chart(data, 'Apwine_dex_usage_eth', 'time','swaps', 'Apwine DEX Usage ETH ')

    st.markdown('#') 
    st.markdown('#') 
    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'Apwine_token_daily_buys_sell', 'datex','daily_buy', 'Apwine Token Daily Buy')
        
    with col2:


        line_chart(data, 'Apwine_token_daily_buys_sell', 'datex','daily_sell', 'Apwine Token Daily Buy')

    
    st.markdown('#')
    st.markdown('#')  
    line_chart(data, 'Apwine_user_growth_eth', 'time','users', 'Apwine User Growth ETH ')



    st.markdown('#')
    st.markdown('#')  
    col1, col2 = st.columns((2,2))
    with col1:
        
        line_chart(data, 'Apwine_token_daily_buys_sell', 'datex','cumulative_buy', 'Apwine Token Cumulative Buy')

    with col2:
        line_chart(data, 'Apwine_token_daily_buys_sell', 'datex','cumulative_sell', 'Apwine Token Cumulative Sell')


    st.markdown('#')
    st.markdown('#')  
    col1, col2 = st.columns((2,2))
    with col1:
        st.markdown('#') 
        st.subheader("Aave Token Distribution ETH")
        st.dataframe(table(data,'Apwine_token_distribution_eth'))

    with col2:
        st.markdown('#') 
        st.subheader("Aave DEX Volume ETH")
        st.dataframe(table(data,'Apwine_dex_volume_eth'))

   



    Volume = getdata(750026)

    print(Volume)

    st.markdown('#') 
    st.markdown('#') 

    st.subheader("Token Metrics on Polygon")
    st.markdown('#')
    col1, col2 , col3  = st.columns((3,3,3))

    col1.metric(label = "Fully Diluted Market Cap", value = '$ '+  str("{:,}".format(int(Volume["marketcap"]))) )

    col2.metric(label = "Total Token Supply", value = str("{:,}".format(int(Volume["total_supply"]))) )
    
    col3.metric(label = "Holders on Ethereum", value =  Volume["holders"] )

    st.markdown('#')

    col1, col2 , col3  = st.columns((3,3,3))

    col1.metric(label = "Circulating Supply", value = str("{:,}".format(int(Volume["circ_supply"]))) )

    col2.metric(label = "Total Traded Volume", value = '$ '+   str("{:,}".format(int(Volume["traded_volume"]))) )
    
    col3.metric(label = "$APW Price", value =  '$ '+ "{:.2f}".format(float(Volume["price"])))


    st.markdown('#')
    st.markdown('#')
    line_chart(data, 'Apwine_dex_usage_polygon', 'time','swaps', 'Apwine DEX Usage Polygon ')


    st.markdown('#') 
    st.markdown('#') 

    
    line_chart(data, 'Apwine_user_growth_polygon', 'time','users', 'Apwine User Growth Polygon ')


    st.markdown('#')
    st.markdown('#')

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'Apwine_total_transaction', 'datex','deposit_txns' , 'Aave Total Transaction Deposit')
    with col2:
        line_chart(data, 'Apwine_total_transaction', 'datex','withdraw_txns' , 'Aave Total Transaction Withdraw')
    
    

    st.markdown('#')
    st.markdown('#')  
    col1, col2 = st.columns((2,2))
    with col1:
        st.markdown('#') 
        st.subheader("Aave Token Distribution Polygon")
        st.dataframe(table(data,'Apwine_token_distribution_poly'))

    with col2:
        st.markdown('#') 
        st.subheader("Aave DEX Volume Polygon")
        st.dataframe(table(data,'Apwine_dex_volume_poly'))

    
