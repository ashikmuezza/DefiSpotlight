import streamlit as st
import datetime
from metrics import getdata
import numpy as np
from PIL import Image

from common.connect import *



def polygon_extract():
    st.markdown('#') 
    top_trend = '<p style="font-family:Courier; color:violet; font-size: 25px;">Polygon is a cutting-edge platform. It integrates the best of Ethereum and sovereign blockchains into a fully functional multi-chain system. While it is less expensive and faster to use, it does not affect the Ethereum platform’s security and interoperability. As a result, an increasing number of developers are using it to build high-quality decentralized exchanges (DEXes) on top of the Polygon network. Here is a polygon DEXs stats.</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('#') 

    st.header('Polygon DEX Trades')

    st.markdown('#') 
    

    DEXs24hVolume = getdata(630026)
    DEXs7DVolume = getdata(630128)
    DEXs1MVolume = getdata(630161)
    
    col1, col2, col3 = st.columns((3,3,3))
    col1.metric(label = "Past DEXs 24h Volume in Millions", value = str(int(DEXs24hVolume.values)) + "M")
    col2.metric(label = "Past DEXs 7D Volume in Millions", value = str(int(DEXs7DVolume.values )) + "M")
    col3.metric(label = "Past DEXs 1M Volume in Billions", value = str(int(DEXs1MVolume.values)) + "B")

    DEXsTrailingGrowth24h= getdata(630173)
    DEXsTrailingGrowth1w= getdata(630455)
    DEXsTrailingGrowth1m= getdata(630450)

    st.markdown('#') 

    col4, col5, col6 = st.columns((3,3,3))
    col4.metric(label = "DEXs Trailing Past 24h Growth", value =  DEXsTrailingGrowth24h['daily_trailing_growth'][0] )
    col5.metric(label = "DEXs Trailing Past 7D Growth", value =  DEXsTrailingGrowth1w['weekly_trailing_growth'][0] )
    col6.metric(label = "DEXs Trailing Past 1M Growth", value =  DEXsTrailingGrowth1m['monthly_trailing_growth'][0] )

    st.markdown('#') 
    data = connect('db/polygon.db')

    line_chart(data,'polygon_daily_dex_volume', 'time', 'volume', "Polygon Daily DEXs Volume (LAST_3_MONTHS)")
    line_chart_multi(data,'polygon_daily_dex_volume_per_dex', 'time', 'volume', 'project', "Polygon Daily DEXs Volume (LAST_3_MONTHS)")
    st.markdown('#') 
    line_chart(data,'polygon_weekly_dex_volume', 'time', 'volume', "Polygon Weekly DEXs Volume")
    line_chart_multi(data,'polygon_weekly_dex_volume_per_dex', 'time', 'volume', 'project', "Polygon Weekly Volume per DEX")


    st.markdown('#') 
    col1, col2 = st.columns((2,2))
    with col1:
        pie_chart(data, 'polygon_dex_marketshare_last_week', 'Marketshare', 'Project', 'DEX Marketshare by Volume Last Week')
    with col2:
        line_chart_multi(data, 'polygon_dex_marketshare_trading_volume', 'time', 'volume', 'project', 'DEX Marketshare By Trading Volume')

   
    st.markdown('#') 

    col1, col2 = st.columns((2,2))

    df = table(data,'polygon_dex_by_volume')
    col1.header('DEXs by Volume')
    with col1:

        st.dataframe(df,500, 300)

    df = table(data,'polygon_dex_by_users')
    col2.header('DEXs by Users')
    with col2:
        st.dataframe(df,500, 300)


    st.markdown('#') 


    df = table(data,'polygon_dex_by_transactions_count')
    col1.header('DEXs by Transaction count')
    st.dataframe(df,700,1200)
   
    st.markdown('#') 
    st.markdown("#")

    st.title("Aggregators Stats")

    st.markdown('#') 
    st.markdown("#")

    agg_7d =  getdata(630279)
    agg_growth = getdata(631143)
    agg_volume = getdata(630478)
    agg_user = getdata(630487)

    col1, col2 = st.columns((3,3))
    col1.metric(label = "Aggregators Marketshare (From 7D Volume)", value = str(int(agg_7d.values)) + "%")
    col2.metric(label = "Aggregator Marketshare Growth", value = str(agg_growth.values)[3:8])

    st.markdown("#")

    col1, col2 = st.columns((2,2))
    with col1:
        line_chart_multi(data, 'polygon_aggregators_volume', 'time', 'volume', 'project', 'Aggregators by Volume' )
    with col2:
        line_chart_multi(data, 'polygon_aggregators_marketshare_trading_volume', 'time', 'volume', 'project', 'Aggregators Marketshare by Trading volume' )

    st.markdown("#")

    col1, col2 = st.columns((3,3))

    with col1:
        st.dataframe(agg_volume)
    with col2:
        st.dataframe(agg_user)
