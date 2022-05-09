import streamlit as st
import hydralit_components as hc
import datetime
from dune import getdata_fromdune
from polygon import get_data
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu
import time



def polygon_extract():
    st.markdown('#') 

    DEXs24hVolume = getdata_fromdune(630026)
    DEXs7DVolume = getdata_fromdune(630128)
    DEXs1MVolume = getdata_fromdune(630161)

    col1, col2, col3 = st.columns((3,3,3))
    col1.metric(label = "Past DEXs 24h Volume", value = DEXs24hVolume.values )
    col2.metric(label = "Past DEXs 7D Volume", value = DEXs7DVolume.values )
    col3.metric(label = "Past DEXs 1M Volume", value = DEXs1MVolume.values)

    DEXsTrailingGrowth24h= getdata_fromdune(630173)
    DEXsTrailingGrowth1w= getdata_fromdune(630455)
    DEXsTrailingGrowth1m= getdata_fromdune(630450)

    st.markdown('#') 

    col4, col5, col6 = st.columns((3,3,3))
    col4.metric(label = "DEXs Trailing Past 24h Growth", value =  DEXsTrailingGrowth24h['daily_trailing_growth'][0] )
    col5.metric(label = "DEXs Trailing Past 7D Growth", value =  DEXsTrailingGrowth1w['weekly_trailing_growth'][0] )
    col6.metric(label = "DEXs Trailing Past 1M Growth", value =  DEXsTrailingGrowth1m['monthly_trailing_growth'][0] )

    st.markdown('#') 

    chart1 = get_data('polygon_daily_dex_volume','DEX','Polygon Daily DEXs Volume','Line')
    chart2 = get_data('polygon_daily_dex_volume_per_dex','Project','Polygon Daily Volume per DEX','Line')
    st.altair_chart(chart1 | chart2) 

    st.markdown('#') 

    chart1 = get_data('polygon_weekly_dex_volume','DEX','Polygon Weekly DEXs Volume','Line')
    chart2 = get_data('polygon_weekly_dex_volume_per_dex','Project','Polygon Weekly Volume per DEX','Line')
    st.altair_chart(chart1 | chart2) 

    st.markdown('#') 

    chart1 = get_data('polygon_dex_marketshare_last_week','DEX','DEX Marketshare by Volume','Donut')
    col1, col2 = st.columns((2,2))
    col1.plotly_chart(chart1)
    chart2 = get_data('polygon_dex_marketshare_trading_volume','Project','DEX Marketshare based on Trading Volume','Donut')
    col2.plotly_chart(chart2)

    st.markdown('#') 
    st.markdown('#') 

    col1, col2 = st.columns((2,2))
    df = get_data('polygon_dex_by_volume','DEX','DEXs by Volume','Table')
    col1.write('DEXs by Volume')
    col1.dataframe(df,500, 300)

    df = get_data('polygon_dex_by_users','DEX','DEXs by Volume','Table')
    col2.write('DEXs by Users')
    col2.dataframe(df,500, 300)


    st.markdown('#') 
    st.markdown('#') 


    chart1 = get_data('polygon_aggregators_volume','Project','Aggregators by Volume','Donut')
    col1, col2 = st.columns((2,2))

    df = get_data('polygon_dex_by_transactions_count','DEX','DEXs by Volume','Table')
    col1.write('DEXs by Transaction count')
    col1.dataframe(df,500, 300)
    col2.plotly_chart(chart1)

    col1, col2 = st.columns((2,2))
    df = get_data('polygon_aggregators_volume','DEX','Aggregators by Volume','Table')
    col1.write('Aggregators by Volume')
    col1.dataframe(df,500, 300)

    df1 = get_data('polygon_aggregators_marketshare_trading_volume','DEX','Aggregators Marketshare by Trading volume','Table')
    col2.write('Aggregators Marketshare by Trading volume')
    col2.dataframe(df1,500, 300)

