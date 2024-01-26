# streamlit
import streamlit as st
# data preprocessing and storage
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import numpy as np
# data viz
import plotly.express as px

st.set_page_config(layout='wide')

def generate_dashboard():

    # Define sidebar date filter
    st.sidebar.title("Date Filter")
    # Define date range slider
    start_date = st.sidebar.date_input("Select start date:", datetime.now() - timedelta(days=7))
    end_date = st.sidebar.date_input("Select end date:", datetime.now())
    # Format  the dates
    start_date_fmt = start_date.strftime('%Y-%m-%d')
    end_date_fmt = end_date.strftime('%Y-%m-%d')

    # query the database
    con= sqlite3.connect(r"your_directory\cmc_market.db")
    query_cmc = f"SELECT * FROM cmc_market WHERE DATE(date) BETWEEN ? AND ?"
    df_filtered = pd.read_sql_query(query_cmc, con, params = (start_date_fmt, end_date_fmt))
    con.close()

    # Define token selection filter
    selected_tokens = st.multiselect('Select tokens', list(df_filtered['token'].unique()), default = list(df_filtered['token'].unique()))

    # filter the dataframe further on the selected tokens
    df_filtered_selection = df_filtered[df_filtered['token'].isin(selected_tokens)]

    # create a price graph
    fig_price = px.line(df_filtered_selection, x='date', y='price', color = 'token')
    fig_price.update_layout(
        title=f"Token Price",
        xaxis_title="Date",
        yaxis_title="Price"
    )

    # create a volume graph
    fig_volume = px.line(df_filtered_selection, x='date', y='volume', color = 'token')
    fig_volume.update_layout(
        title=f"Token Volume",
        xaxis_title="Date",
        yaxis_title="Volume"
    )

    # calculate combined average price growth
    price = 0
    price_start = 0
    for token in df_filtered_selection['token'].unique():
        price += df_filtered_selection[df_filtered_selection['token'] == token].iloc[-1, 3]
        price_start += df_filtered_selection[df_filtered_selection['token'] == token].iloc[0, 3]
    avg_price = price/df_filtered_selection['token'].nunique()
    avg_price_start = price_start/df_filtered_selection['token'].nunique()
    selected_avg_price_growth = (avg_price - avg_price_start) / avg_price_start

    # calculate combined volume growth
    combined_volume = 0
    combined_volume_start = 0
    for token in df_filtered_selection['token'].unique():
        combined_volume += df_filtered_selection[df_filtered_selection['token'] == token].iloc[-1, 2]
        combined_volume_start += df_filtered_selection[df_filtered_selection['token'] == token].iloc[0, 2]
    selected_vol_growth = (combined_volume - combined_volume_start) / combined_volume_start

    col1, col2 = st.columns(2, gap='large')
    with col1:
        # price graph
        st.metric("Current Average Price", np.round(avg_price, 4), delta = f"{selected_avg_price_growth*100:.2f}%")
        st.plotly_chart(fig_price, use_container_width=True)

    with col2:
        # volume graph
        st.metric("Selected tokens volume", f"{int(combined_volume)/1000000000:.1f}B", delta = f"{selected_vol_growth*100:.2f}%")
        st.plotly_chart(fig_volume, use_container_width=True)

if __name__ == "__main__":
    generate_dashboard()