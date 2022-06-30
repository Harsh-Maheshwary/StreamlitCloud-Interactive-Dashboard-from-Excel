from tabnanny import check
from turtle import end_fill
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px
from requests import options  # pip install plotly-express
import streamlit as st
from traitlets import default  # pip install streamlit


df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )

st.dataframe(df)


# SIDEBAR

st.sidebar.header="Please SELECT"
city = st.sidebar.multiselect("Select City", options=df["City"].unique(),default=df["City"].unique())
customer_type = st.sidebar.multiselect("Select Customer Type", options=df["Customer_type"].unique(),default=df["Customer_type"].unique())
gender = st.sidebar.multiselect("Select Gender", options=df["Gender"].unique(),default=df["Gender"].unique())

df_selection = df.query("City == @city & Customer_type == @customer_type & Gender == @gender")

total_sales = int(df_selection["Total"].sum())

st.write(total_sales)

st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.write(f"{average_rating} {star_rating}")

st.markdown("""---""")