import streamlit as st
import plost
import datetime
from dune import getdata_fromdune
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def chainlink_home():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">Chainlink decentralized oracle networks provide tamper-proof inputs, outputs, and computations to support advanced smart contracts on any blockchain..</p>'
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')

    st.header("Why is Chainlink important?")

    top_trend = '<p style="font-family:Courier; color:violet; font-size: 20px;">DeFi takes the basic premise of Bitcoin — digital money — and expands on it, creating an entire digital alternative to Wall Street, but without all the associated costs (think office towers, trading floors, banker salaries). This has the potential to create more open, free, and fair financial markets that are accessible to anyone with an internet connection.</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('#')

    top_trend = '<p style="font-family:Courier; color:white; font-size: 25px;">Top Protocols with holders</p>'
    st.markdown(top_trend, unsafe_allow_html=True)


    data = connect('db/chainlink.db')

    st.markdown('#')

    bar_chart(data, 'chainlinkVRF_total_link_on_cexs',  'exchange','amount','exchange insights')
    
    st.markdown('#')
    
    st.markdown('#')
    pie_chart(data,'chainlink_on_dapps','amount','classification','Classification')
   
#Daily Data vrf1
    st.markdown('#') 

    col1, col2 = st.columns((2,2))

    df = table(data,'chainlinkVRF_v1_daily_BSC')
    col1.header('VRF v1 on (BSC) - Daily')
    with col1:

        st.dataframe(df,500, 300)

    df = table(data,'chainlinkVRF_v1_daily_ETH')
    col2.header(' VRF v1 on Ethereum - Daily')
    with col2:
        st.dataframe(df,500, 300)


#Daily Data vrf2

    st.markdown('#') 

    col1, col2 = st.columns((2,2))

    df = table(data,'chainlinkVRF_v2_daily_BSC')
    col1.header('VRF v2 on (BSC) - Daily')
    with col1:

        st.dataframe(df,500, 300)

    df = table(data,'chainlinkVRF_v2_daily_ETH')
    col2.header(' VRF v2 on Ethereum - Daily')
    with col2:
        st.dataframe(df,500, 300)

    