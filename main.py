import streamlit as st
import datetime
from dune import getdata_fromdune
from polygon import get_data
import numpy as np
from PIL import Image
from polygon_defi.polygon_extract import polygon_extract
from defi.defi_extract import defi_home
import time


st.set_page_config(
    page_title="DEFI Dash",
    layout="wide"
)


new_title = '<p style="font-family:Bodoni; text-align: center; color:#FFFFFF; font-size: 60px;">DEFI DASHBOARD</p>'
st.markdown(new_title, unsafe_allow_html=True)

with st.sidebar:
    option = st.radio(
        'Select sponsors',
        ('DEFI','Polygon', 'DYDX','Makerdao','Uniswap'))

     

st.write(option)

if option == 'DEFI':
  
  defi_home()

elif option == 'Polygon' :

  polygon_extract()

