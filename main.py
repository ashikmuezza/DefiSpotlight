import streamlit as st
import datetime
from dune import getdata_fromdune
import numpy as np
from PIL import Image
from polygon_defi.polygon_extract import polygon_extract
from defi.defi_extract import defi_home
from dydx.dydx_extract import dydx_extract
from maker.maker_extract import maker_extract
from lyra.lyra_extract import lyra_home
from badger.badger_extract import badger_extract
from chainlink.chainLink_extract import chainlink_home
from unstoppable.unstop_extract import unstop_extract
from epns.epns_extract import epns_extract
from common.covalent.covalent_extract import covalent_extract
from yearn.yearn_extract import yearn_extract

import time


st.set_page_config(
    page_title="DEFI Dash",
    layout="wide"
)


new_title = '<p style="font-family: Arial, Helvetica, sans-serif; text-align: center; color:#FFFFFF; font-size: 60px;">DEFI SPOTLIGHT</p>'
st.markdown(new_title, unsafe_allow_html=True)

with st.sidebar:
    option = st.radio(
        'Select sponsors',
        ('DEFI','Polygon', 'DYDX','Makerdao','Uniswap',
        'Lyra','Chainlink', 'Badger', 'Unstoppable', 'epns',
        'covalent', 'yearn'))

     
st.header(option)


if option == 'DEFI':
  defi_home()

elif option == 'Polygon' :
  polygon_extract()

elif option == 'DYDX' :
  dydx_extract()

elif option == 'Makerdao' :
  maker_extract()

elif option == 'Lyra' :
  lyra_home()

elif option == 'Chainlink' :
  chainlink_home()

elif option == 'Badger' :
  badger_extract()

elif option == 'Unstoppable' :
  unstop_extract()

elif option == 'epns' :
  epns_extract()

elif option == 'covalent' :
  covalent_extract()

elif option == 'yearn' :
  yearn_extract()






