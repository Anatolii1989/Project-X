import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')

# scatterplot in plotly_express with checkbox
st.header('Car Price by Year')
df_year_1940 = df[df.model_year > 1940]
df_price_100k = df_year_1940[df.price < 100000]
price_more_100k = st.checkbox('Include adds with price more than 100 000')
if price_more_100k:
    fig = px.scatter(
    df_year_1940,
    x="model_year",
    y="price",
    color="model_year",
    color_continuous_scale="reds",)
else:
    fig = px.scatter(
    df_price_100k,
    x="model_year",
    y="price",
    color="model_year",
    color_continuous_scale="reds",)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)

# histogram in plotly_express
st.header('Days Listed Adds (by Condition)')
st.write(px.histogram(df, x='days_listed', color='condition'))

# add new column "Manufacturer"
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# boxplot in plotly_express
df_price_filtered50 = df[(df.price < 50000) & (df.model_year > 1940)]
st.header('Car Price Distribution by Manufacturer')
st.write(px.box(df_price_filtered50, x='manufacturer', y='price', color='manufacturer'))