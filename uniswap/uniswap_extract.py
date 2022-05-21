import streamlit as st
import plost
import altair as alt
import datetime
from dune import getdata_fromdune
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def uniswap_extract():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">Uniswap is a cryptocurrency exchange which uses a decentralized network protocol. Uniswap is also the name of the company that initially built the Uniswap protocol. The protocol facilitates automated transactions between cryptocurrency tokens on the Ethereum blockchain through the use of smart.</p>'
    
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')

    st.header('Uniswap Overall Metrics')

    st.markdown('#') 

    Volume = getdata_fromdune(44614)

    print(Volume)

    
    col1, col2 , col3, col4  = st.columns((4,4,4,4))

    col1.metric(label = "Total Trading Volume (All Pairs)", value = '$ '+ "{:.2f}".format(float(Volume["bil_usd_volume"]))  + " B")


    col2.metric(label = "Trading Volume in Top 15 Pairs", value = '$ '+ "{:.2f}".format(float(Volume["bil_usd_volume_top15"]))  + " B")
    
    col3.metric(label = "Total LP Fees (All Pairs)", value = '$ '+ "{:.2f}".format(float(Volume["mil_usd_fees"]))  + " M")
    col4.metric(label = "LP Fees in Top 15 Pairs", value = '$ '+ "{:.2f}".format(float(Volume["mil_usd_fees_top15"]))  + " M")



    data = connect('db/uniswap.db')


    st.markdown('#')
    st.markdown('#')

    line_chart(data, 'Uniswap_daily_txns_volume', 'Date','usd_amount', 'Uniswap daily transactions by volume (USD)')

    st.markdown('#')

    line_chart_multi(data, 'Uniswap_vs_Sushi_pools', 'hour','val','protocol' , 'Uniswap vs Sushi pools')

    st.markdown('#') 
    col1, col2 = st.columns((2,2))
    with col1:
        
        line_chart(data, 'Uniswap_polygon_daily_txns', 'date_trunc','count', 'Uniswap polygon daily transaction count ')
    with col2:
        
        line_chart(data, 'Uniswap_polygon_daily_unique_address', 'date_trunc','count', 'Uniswap polygon daily unique address ')

    

    st.markdown('#')

    st.markdown('#') 
    col1, col2 = st.columns((2,2))
    with col1:
        
        line_chart(data, 'Uniswap_polygon_weekly_txns', 'date_trunc','count', 'Uniswap polygon weekly transaction count ')
    with col2:
        line_chart(data, 'Uniswap_polygon_weekly_unique_address', 'date_trunc','count', 'Uniswap polygon weekly unique address ')

    
    st.markdown('#')
    st.markdown('#')

    line_chart_multi(data, 'Uniswap_trade_per_month', 'month','trades','uniswap_version' , 'Uniswap Trade per Month')


    st.markdown('#') 
    st.subheader("Uniswap v3 ETH Table")
    st.dataframe(table(data,'Uniswap_v3_ETH_table'))

    st.markdown('#') 
    st.subheader("Uniswap v3 ETH gas Paid per Swap")
    st.dataframe(table(data,'Uniswap_v3_eth_gas_paid_per_swap'))
        
    
   



    
    

    
    

    
   



