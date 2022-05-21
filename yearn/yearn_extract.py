import streamlit as st
import plost
import altair as alt
import datetime
from dune import getdata
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def yearn_extract():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">yearn finance is a group of protocols running on the Ethereum blockchain that allow users to optimize their earnings on crypto assets through lending and trading services. One of a number of emerging decentralized finance (DeFi) projects, yearn..</p>'
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')
    data = connect("db/yearn.db")

    one_day = getdata(667379)
    thirty_days = getdata(667371)

    col1, col2 = st.columns((2,2))
    col1.metric(label = "Yearn vaults user activity in the latest 24 hours", value = one_day['unique_users'].iloc[0])
    col2.metric(label = "Yearn vaults user activity in the latest 30 days", value = thirty_days['unique_users'].iloc[0])


    line_chart(data, 'yearn_vault_active_users', 'day', 'new_users', 'yearn_vault_active_new_users')

    col1,col2 = st.columns((2,2))

    with col1:
        line_chart(data,'yearn_vault_active_users', 'day', 'old_users', 'yearn_vault_active__old_users')
    with col2:
        line_chart(data, 'yearn_vault_active_users', 'day', 'number_of_transactions', 'yearn_vault_number_of_transactions')

    with col1:
        line_chart(data, 'yearn_vault_active_users', 'day', 'unique_users', 'yearn_vault_unique_users')
    with col2:
        bar_chart(data,'yearn_vault_Deposit_Value_Distribution', 'buckets', 'count_bucket', 'yearn_vault_Deposit_Value_Distribution')

    st.subheader('yearn_vault_top_25_active_vaults')
    st.dataframe(table(data, 'yearn_vault_top_25_active_vaults'))
    line_chart_multi(data, 'yearn_vault_top_25_active_vaults', 'yday', 'num_addresses','vault_tag','yearn_vault_top_25_active_vaults')

    col1,col2 = st.columns((2,2))

    with col1:
        line_chart_multi(data,'yearn_vault_avg_deposit_withdraw_YCRV', 'time', 'ycrv','operation', 'yearn_vault_avg_deposit_withdraw_YCRV')
    with col2:
        line_chart_multi(data, 'yearn_vault_avg_deposit_withdraw_YLINK', 'time', 'link','operation', 'yearn_vault_avg_deposit_withdraw_YLINK')
    with col1:
        line_chart_multi(data, 'yearn_vault_avg_deposit_withdraw_YUSDC', 'time', 'usdc', 'operation','yearn_vault_avg_deposit_withdraw_YUSDC')
    with col2:
        line_chart_multi(data, 'yearn_vault_avg_deposit_withdraw_YUSDT', 'time', 'usdt','operation', 'yearn_vault_avg_deposit_withdraw_YUSDT')
    with col1:
        line_chart(data, 'yearn_vault_avg_harvested_yCRV', 'time', 'amount', 'yearn_vault_avg_harvested_yCRV')
    with col2:
        line_chart(data, 'yearn_vault_avg_harvested_yDAI', 'time', 'amount', 'yearn_vault_avg_harvested_yDAI')
    with col1:
        line_chart(data, 'yearn_vault_avg_harvested_yUSDC', 'time', 'amount', 'yearn_vault_avg_harvested_yUSDC')
    with col2:
        line_chart(data, 'yearn_vault_avg_harvested_yUSDT', 'time', 'amount', 'yearn_vault_avg_harvested_yUSDT')