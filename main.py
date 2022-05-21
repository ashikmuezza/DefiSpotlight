from babylon.babylon_extract import baby_extract
import streamlit as st
import datetime
from metrics import getdata
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
from olympus.olympus_extract import olympus_extract
from aave.aave_extract import aave_extract
from uniswap.uniswap_extract import uniswap_extract
from apwine.apwine_extract import apwine_extract


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
        'Lyra','Chainlink', 'Badger', 'Unstoppable', 'Epns',
        'Covalent', 'Yearn', 'Olympus', 'Babylon','Aave','Apwine'))

     
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

elif option == 'Epns' :
  epns_extract()

elif option == 'Covalent' :
  covalent_extract()

elif option == 'Yearn' :
  yearn_extract()

elif option == 'Olympus':
  olympus_extract()

elif option == 'Babylon':
  baby_extract()

elif option == 'Aave':
  aave_extract()

elif option == 'Apwine':
  apwine_extract()

elif option == 'Uniswap':
  uniswap_extract()






