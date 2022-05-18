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


def unstop_extract():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:violet; font-size: 20px;">Unstoppable domains are a type of domain name that uses blockchain technology to handle registration and many other features. Rather than using domain name services (DNSs) like traditional websites, unstoppable domains use a blockchain-based solution called the crypto name service (CNS)..</p>'
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')
    data = pd.read_csv('unstoppable/unstop.csv')

    #st.dataframe(data.head())

    st.header("Unstoppable Domains Opensea Marketplace Analysis")

    data['timestamp'] = pd.to_datetime(data['timestamp'])
    polygon = data[data['chain_id'] == 137]
    
    eth = data[data['chain_id'] == 1]

    poly_wash = polygon[polygon['is_washtrade'] == 'Washtrade']
    eth_wash = eth[eth['is_washtrade'] == 'Washtrade']

    col1, col2 = st.columns((2,2))
    col1.metric(label = "Polygon Sales Volume in USD", value = '$' + str(int(polygon['sale_price_usd'].sum())))
    col2.metric(label = "ETH Sales Volume in USD", value = '$' + str(int(eth['sale_price_usd'].sum())))
    col1.metric(label = "Polygon sales Count", value = int(len(polygon['sale_price_usd'])))
    col2.metric(label = "ETH sales Count", value = int(len(eth['sale_price_usd'])))

    col1,col2 = st.columns((2,2))
    with col1:
        plost.bar_chart(
        polygon,
        bar='timestamp',
        value='sale_price_usd',width=500, height=400, title="NFT Sales On Polygon")
    with col2:
        plost.bar_chart(
        eth,
        bar='timestamp',
        value='sale_price_usd',width=500, height=400, title="NFT Sales On ETH")
    
    col1,col2 = st.columns((2,2))
    with col1:
        plost.bar_chart(
        poly_wash,
        bar='timestamp',
        value='sale_price_usd',width=500, height=400, title="Possible NFT Washtraded Sales On Polygon")
    with col2:
        plost.bar_chart(
        eth_wash,
        bar='timestamp',
        value='sale_price_usd',width=500, height=400, title="Possible NFT Washtraded Sales On ETH")
    
    st.subheader("Wallet level NFT Analysis")
    df = data
    col1, col2 = st.columns((1,5))
    unique_wallets = df[["seller", "buyer"]].values.ravel()
    unique_wallets = len(pd.unique(unique_wallets))
    net = df[df['event'] != 'mint']
    net_seller = net.groupby(['seller']).agg({'sale_price_eth': 'sum'}).reset_index() 
    net_seller = net_seller.nlargest(1,'sale_price_eth')
    net_buyer = net.groupby(['buyer']).agg({'sale_price_eth': 'sum'}).reset_index() 
    net_buyer = net_buyer.nlargest(1,'sale_price_eth')
    count = len(df)
    col1.metric(label = "Unique Wallets", value = unique_wallets)
    col2.metric(label = "Top Seller by Volume", value = net_seller['seller'].max())
    col1.metric(label = "Total Transactions", value = count)
    col2.metric(label = "Top Buyer by Volume", value = net_buyer['buyer'].max())
    st.markdown("#")
    input = st.text_input("Enter Wallet address ",)
    

    if input:
        
        try:
            df = data
            st.markdown('####')
            data = df[(df['seller'] == str(input)) | (df['buyer'] == str(input)) ]
            data1= data[data['is_sold'] == True]
            st.info("Wallet Summary")
            Trans_count = len(data[data['event'] == 'sale'])
            mint_count = len(data[data['event'] == 'mint'])
            coin = data['token_symbol'].value_counts().idxmax()
            data2 = data[data['seller'] != '0x0000000000000000000000000000000000000000']
            interacted = data2.groupby(['seller','buyer']).size().idxmax()
            max_value = data['sale_price_eth'].max()
            min_value = data1['sale_price_eth'].min()
            avg_value = data['sale_price_eth'].mean()
            overall = data['sale_price_eth'].sum()
            st.text(f"Total Transactions Counts = {Trans_count}")
            st.text(f'Most Used Token Symbol = {coin}')
            st.text(f"Most Interacted Wallet = {interacted}")
            st.text(f"Max Sale = {max_value}" + "ETH")
            st.text(f"Min Sale = {min_value}" + 'ETH')
            st.text(f"Avg Sale = {avg_value}" + 'ETH')
            st.success(f"Overall Sale Volume = {overall}" + 'ETH')
            st.markdown('####')
            st.info("Transaction Table")
            st.dataframe(data)
            data1['timestamp'] = pd.to_datetime(data1['timestamp'])
            data1['date'] = data1['timestamp'].dt.date
            data1 = data1.sort_values(by="date")
            line = alt.Chart(data1).mark_bar().encode(
                    x = 'date',
                    y = 'sale_price_eth'
                ).properties(width = 1100, height = 400, ).interactive()
            st.markdown('####')
            st.info('Sale Chart')
            st.altair_chart(line)

        except:
            st.warning("Info not found in DB")
    else:
        df = data
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.sort_values(by='timestamp',ascending=False, inplace=True)
        st.markdown("####")
        st.info("Recent 100 Transaction")
        st.dataframe(df.head(100), height=900)

    