import streamlit as st
import plost
import datetime
from metrics import getdata
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def maker_extract():
    st.markdown('#') 
    top_trend = '<p style="font-family:Courier; color:violet; font-size: 25px;"> MakerDAO is a crypto lending credit facility that gives loans at predetermined interest rates. If a MakerDAO user wants to borrow, they would first deposit the Ethereum into a Maker smart contract. The smart contract creates a Collateralized Debt Position (CDP)...</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('#') 

    st.header('MAKERDAO STATS')

    st.markdown('#') 

    data = connect('db/maker.db')

    line_chart(data, 'Maker_price', 'hour', 'median_price', 'Mkr Price')

    line_chart_multi(data,'Maker_assets_per_type', 'dt', 'asset', 'collateral', 'MakerDAO Assets Per Type')

    top_trend = '<p style="font-family:Courier; color:green; font-size: 25px;"> An oracle module is deployed for each collateral type, feeding it the price data for a corresponding collateral type to the Vat. The Oracle Module introduces the whitelisting of addresses, which allows them to broadcast price updates off-chain, which are then fed into a median before being pulled into the OSM.</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('#') 

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'Maker_oracle_Medianizer_daily', 'time', 'tx_fee_usd', 'Oracle Gas Fees (tx_fee): Medianizer Total Daily')
    with col2:
        line_chart(data, 'Maker_oracle_OSM_Megapoker_daily', 'time', 'tx_fee_usd', 'Oracle Gas Fees (tx_fee): OSM daily')

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'Maker_oracle_gas_fee_Medianizer_daily', 'time', 'mgas', 'Oracle Gas Fees: Medianizer daily gas used')
    with col2:
        line_chart(data, 'Maker_oracle_gas_fee_OSM_Megapoker_daily', 'time', 'mgas', 'Oracle Gas Fees: OSM daily gas used')
    st.markdown('#') 
    line_chart_multi(data, 'Maker_oracle_gas_fee_pairs', 'time', 'tx_fee_usd', 'medianizer', 'Oracle Gas Fees: Pairs')

    st.markdown('#') 
    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'Maker_outstanding_dai', 'day', 'outstanding_dai', 'Maker_outstanding_dai')
    with col2:
        bar_chart_vertical(data, 'Maker_total_user', 'date', 'total_users', 'Maker_total_users')
        
    st.markdown('#') 
    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'Maker_volume_balance', 'date', 'inflow', 'Volumes Maker - Money Markets Inflow')
    with col2:
         line_chart(data, 'Maker_volume_balance', 'date', 'outflow', 'Volumes Maker - Money Markets Outflow')

    st.markdown('#') 
    line_chart(data, 'Maker_volume_balance', 'date', 'lifetime_turnover', 'Volumes Maker - Money Markets Turnover')
