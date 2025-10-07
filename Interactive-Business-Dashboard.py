import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv(r'd:/python_ka_chilla/Internship/Part 2/Task 5/Global Superstore.csv', encoding='ISO-8859-1')
    df = df.dropna(subset=['Sales', 'Profit'])
    return df

df = load_data()
st.title("📊 Global Superstore Interactive Dashboard")
st.write("✅ Data Loaded Successfully!", df.head())

st.sidebar.header("📌 Filter Options")
region = st.sidebar.multiselect("Select Region:", options=df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("Select Category:", options=df['Category'].unique(), default=df['Category'].unique())
sub_category = st.sidebar.multiselect("Select Sub-Category:", options=df['Sub-Category'].unique(), default=df['Sub-Category'].unique())

df_selection = df.query("Region == @region & Category == @category & `Sub-Category` == @sub_category")

total_sales = round(df_selection['Sales'].sum(), 2)
total_profit = round(df_selection['Profit'].sum(), 2)
top_customers = df_selection.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.metric("Total Sales 💰", f"${total_sales}")
with middle_column:
    st.metric("Total Profit 💹", f"${total_profit}")
with right_column:
    st.metric("Top 1 Customer 🏆", f"{top_customers.index[0]}: ${round(top_customers.iloc[0], 2)}")

st.markdown("---")
fig_sales = px.bar(top_customers, x=top_customers.index, y=top_customers.values, title="Top 5 Customers by Sales", labels={'y':'Sales', 'index':'Customer Name'}, color=top_customers.values, color_continuous_scale='Blues')
st.plotly_chart(fig_sales, use_container_width=True)

fig_profit = px.pie(df_selection, names='Sub-Category', values='Profit', title='Profit Distribution by Sub-Category')
st.plotly_chart(fig_profit, use_container_width=True)

fig_region = px.bar(df_selection.groupby('Region')['Sales'].sum().reset_index(), x='Region', y='Sales', title='Sales by Region', color='Sales', color_continuous_scale='Greens')
st.plotly_chart(fig_region, use_container_width=True)
