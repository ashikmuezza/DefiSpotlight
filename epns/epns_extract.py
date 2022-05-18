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


def epns_extract():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">Unstoppable domains are a type of domain name that uses blockchain technology to handle registration and many other features. Rather than using domain name services (DNSs) like traditional websites, unstoppable domains use a blockchain-based solution called the crypto name service (CNS)..</p>'
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')
    data = connect("db/epns.db")
    holders = getdata_fromdune(589646)
    price = getdata_fromdune(589850)

    col1, col2 = st.columns((2,2))
    col1.metric(label = "PUSH Holders", value = holders['$PUSH Holders'].iloc[0])
    col2.metric(label = "PUSH Recent AVG Price", value = price['Daily Average Price'].iloc[0])

    line_chart(data, 'push_price', 'day', 'token_price_usd', 'push_price')

    col1, col2 = st.columns((2,2))
    with col1:
        bar_chart_vertical(data, 'push_price', 'day', 'supply', 'PUSH_supply')
    with col2: 
        line_chart(data, 'push_price', 'day', 'lp_price', 'PUSH_LP_price')

    with col1:
        bar_chart_vertical(data, 'push_holders', 'day', 'holders', 'PUSH_holders')
    with col2:
        line_chart(data, 'push_uniswap_lp_holders', 'day', 'holders', 'push_uniswap_lp_holders')

    line_chart(data, 'push_weekly_avg_amount_transaction', 'Week', 'total_transaction', 'PUSH_total_transaction')

    line_chart(data, 'push_weekly_avg_amount_transaction', 'Week', 'transfered_amount', 'PUSH_transfered_amount')

    line_chart(data, 'push_weekly_avg_amount_transaction', 'Week', 'avg_push_transfered_amount', 'PUSH_avg_transfered_amount')

    