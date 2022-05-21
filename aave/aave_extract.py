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


def aave_extract():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">Aave is a decentralized lending system that allows users to lend, borrow and earn interest on crypto assets, all without middlemen. It is a fully decentralized, community governed protocol with 110,597 token holders.  Aave currently supports several cryptocurrencies built on top of the Ethereum blockchain, and the range of services is constantly growing.</p>'
    
    st.markdown(Defi_title, unsafe_allow_html=True)

    data = connect('db/aave.db')

    st.markdown('#')

    st.markdown('#') 

    bar_chart_vertical(data, 'Aave_polygon_active_users', 'dt', 'cumulative_total', 'Aave users cummulative')

   



    
    

    
    

    
   



