import streamlit as st
import plost
import datetime
from dune import getdata_fromdune
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def defi_home():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">DeFi (or “decentralized finance”) is an umbrella term for financial services on public blockchains, primarily Ethereum. With DeFi, you can do most of the things that banks support — earn interest, borrow, lend, buy insurance, trade derivatives, trade assets, and more — but it’s faster and doesn’t require paperwork or a third party. As with crypto generally, DeFi is global, peer-to-peer (meaning directly between two people, not routed through a centralized system), pseudonymous, and open to all.</p>'
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')

    st.header("Why is DeFi important?")

    top_trend = '<p style="font-family:Courier; color:blue; font-size: 20px;">DeFi takes the basic premise of Bitcoin — digital money — and expands on it, creating an entire digital alternative to Wall Street, but without all the associated costs (think office towers, trading floors, banker salaries). This has the potential to create more open, free, and fair financial markets that are accessible to anyone with an internet connection.</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('#')

    top_trend = '<p style="font-family:Courier; color:white; font-size: 25px;">Top Protocols with holders</p>'
    st.markdown(top_trend, unsafe_allow_html=True)


    data = connect('db/defi.db')

    st.markdown('#')

    bar_chart(data, 'Defi_project_top_holders', 'contract_address', 'holders')





    