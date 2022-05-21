import streamlit as st
import plost
import datetime
from dune import getdata_fromdune
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def baby_extract():
    st.markdown('#') 
    top_trend = '<p style="font-family:Courier; color:violet; font-size: 25px;">The Heart of Babylon is a garden that receives BABL as deposits and give depositors hBABL. The heart receives 100% of the protocol fees and BABL from stakers and infuse them both with renewed energy..</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    data = connect('db/babylon.db')

    locked = getdata_fromdune(650022)


    col1, col2, col3 = st.columns((2,2,2))
    col1.metric(label = "BABL locked in hBABL contract", value =str(int(locked['babl_balance'].iloc[0])) )
    col2.metric(label = "Balance USD in hBABL Contract", value = '$' + str(int(locked['balance_usd'].iloc[0] )))
    col3.metric(label = "hBABL price", value = '$' + str(int(locked['price'].iloc[0] )))


    line_chart(data, 'babylon_babl_in_heart_over_time', 'day', 'babl_balance', 'babylon_babl_in_heart_over_time')
    line_chart(data, 'babylon_hBABL_daily_balance', 'day', 'balance', 'babylon_hBABL_daily_balance')

    col1, col2 = st.columns((2,2))

    with col1:
        pie_chart(data, 'babylon_hbabl_holders_grouped', 'tokens','holder',  'babylon_hbabl_holders_grouped')
        pie_chart(data, 'babylon_pump_totals', 'amount_usd','description',  'babylon_pump_totals')
    with col2:
        pie_chart(data, 'babylon_hbabl_per_address','hbabl', 'address',  'babylon_hbabl_per_address')
        line_chart_multi(data, 'babylon_seed_investment_per_garden', 'pump', 'weth_invested_usd','garden','babylon_seed_investment_per_garden')

    st.subheader('babylon_heart_babl_sent')
    st.dataframe(table(data,'babylon_heart_babl_sent'))

    st.subheader('babylon_heart_fees_collected')
    st.dataframe(table(data,'babylon_heart_fees_collected'))

    st.subheader('babylon_heart_garden_seedinvest')
    st.dataframe(table(data,'babylon_heart_garden_seedinvest'))

    st.subheader('babylon_heart_liquidity_added')
    st.dataframe(table(data,'babylon_heart_liquidity_added'))

    


    