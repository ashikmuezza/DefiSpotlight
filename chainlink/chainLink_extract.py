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

    Defi_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">Chainlink is a decentralized blockchain oracle network built on Ethereum.[3][4] The network is intended to be used to facilitate the transfer of tamper-proof data from off-chain sources to on-chain smart contracts. Its creators claim it can be used to verify whether the parameters of a smart contract are met in a manner independent from any of the contracts stakeholders by connecting the contract directly to real-world data, events, payments, and other inputs..</p>'
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')

    data = connect('db/chainlink.db')

    col1, col2, col3 = st.columns((3,3,3))
    col1.metric(label = "Wallets with (LINK))", value = str(int(getdata_fromdune(188622).values)) )
    col2.metric(label = "Wallets with > 10  (LINK)", value = str(int(getdata_fromdune(189866).values)) )
    col3.metric(label = "Wallets with > 100 (LINK)", value = str(int(getdata_fromdune(189892).values)))

    st.markdown('#')

    bar_chart(data, 'chainlinkVRF_total_link_on_cexs',  'exchange','amount','Total LINK on centralized exchanges')
    
    st.markdown('#')
    
    pie_chart(data,'chainlink_on_dapps','amount','classification','chainlink_on_L1/L2/Dapps')
   
#Daily Data vrf1
    st.markdown('#') 
    col1, col2 = st.columns((2,2))
    with col1:
        st.write("chainlinkVRF_v1_BSC_LINK_Earned")
        st.dataframe(table(data, 'chainlinkVRF_v1_daily_BSC'))
    with col2:
        st.write("chainlinkVRF_v1_ETH_LINK_Earned")
        st.dataframe(table(data, 'chainlinkVRF_v1_daily_ETH'))

    st.markdown('#') 

    col1, col2 = st.columns((2,2))
    with col1:
       line_chart(data,'chainlinkVRF_v1_daily_BSC', 'date' ,'request', 'chainlinkVRF_v1_daily_BSC')
    with col2:
       line_chart(data,'chainlinkVRF_v2_daily_BSC', 'Day' ,'request', 'chainlinkVRF_v2_daily_BSC')

    st.markdown('#') 

    col1, col2 = st.columns((2,2))

    
    with col1:
        line_chart(data,'chainlinkVRF_v1_daily_ETH', 'day' ,'request', 'chainlinkVRF_v1_daily_ETH')

    with col2:
        line_chart(data,'chainlinkVRF_v2_daily_ETH', 'Day' ,'request', 'chainlinkVRF_v2_daily_ETH')

    line_chart(data,'chainlinkVRF_daily_polygon', 'day' ,'request', 'chainlinkVRF_daily_polygon')

    st.markdown('#') 

   
    line_chart(data, 'chainlinkVRF_keepers_daily_BSC', 'Day', 'UpKeeps', 'chainlinkVRF_keepers_daily_BSC')

    line_chart(data, 'chainlinkVRF_keepers_daily_ETH', 'Day', 'UpKeeps', 'chainlinkVRF_keepers_daily_ETH')

    line_chart(data, 'chainlinkVRF_keepers_daily_poly', 'Day', 'UpKeeps', 'chainlinkVRF_keepers_daily_POLYGON')

    st.markdown('#') 
    col1,col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'chainlink_Feed_Requesting_Transactions', 'date', 'txns', 'chainlink_Feed_Requesting_Transactions')
    with col2:
        line_chart(data, 'chainlink_active_feeds', 'date', 'active_feeds', 'chainlink_active_feeds')

    
    line_chart(data, 'chainlink_active_feeds_requesters', 'date', 'active_feed_requesters', 'chainlink_active_feeds_requesters')

    
    
    