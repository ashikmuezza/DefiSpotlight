import streamlit as st
import hydralit_components as hc
import datetime
from dune import getdata_fromdune
from polygon import get_data
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu
from polygon_defi.polygon_extract import polygon_extract
import time


st.set_page_config(page_title='Defi dashboard',layout='wide',initial_sidebar_state='collapsed',)

over_theme = {'txc_inactive': '#FFFFFF'}

with st.sidebar:
    option = st.radio(
        'Select sponsors',
        ('DEFI','Polygon', 'DYDX','Makerdao','Uniswap'))

     

st.write(option)


if option == 'Polygon' :

  polygon_extract()