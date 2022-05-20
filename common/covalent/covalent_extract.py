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


def covalent_extract():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">Covalent is a software that aggregates data from several of the leading blockchain platforms, including Ethereum, Avalanche and Polygon, and allows participants to access these data points for a variety of use cases..</p>'
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')
    data = connect("db/cqt.db")
    
    st.markdown("#")

    line_chart(data, 'cqt_price', 'day', 'price', 'CQT_Price')

    line_chart_multi(data,'cqt_daily_buys_on_dex', 'day', 'volume', 'project', 'CQT_daily_buys_on_dex')

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart(data, 'cqt_daily_active_users', 'time', 'Old', 'CQT_daily_active_users')
    with col2:
        line_chart(data,'cqt_daily_new_account', 'Date', 'acc', 'CQT_daily_new_account')
    with col1:
        line_chart(data, 'cqt_holders_over_time', 'date', 'total_users', 'CQT_holders_over_time')
    with col2:
        line_chart(data, 'cqt_purchases', 'date', 'old_users_purchases', 'CQT_users_purchases')
    with col1:
        pie_chart(data, 'cqt_seven_days_dex_volume','seven', 'Project', "CQT_seven_days_dex_volume")
    with col2:
        pie_chart(data, 'cqt_seven_days_dex_volume','one', 'Project', "CQT_one_days_dex_volume")
    
    line_chart(data, 'cqt_transactions', 'date_trunc', 'count', 'CQT_transactions')

    with col1:
        line_chart(data, 'cqt_monthly_active_users', 'Date', 'month', 'CQT_monthly_active_users')
    with col2:
        line_chart_multi(data,'cqt_unique_address_trading', 'day', 'unique_addresses', 'project', 'CQT_unique_address_trading')