import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv("ai_job_cleaned.csv")
st.header("Ai Jobs Analysis")
st.set_page_config("Salary",page_icon="🔥",layout="wide")


job = st.selectbox("Choose The Job",df.job_title.unique())

month_salary = df[df.job_title == job]["monthly_salary"].mean()
annual_salary = df[df.job_title == job]["annual_salary"].mean()

col1 , col2 = st.columns(2)
con1 = col1.container(border=True)
con2 = col2.container(border=True)

con1.metric("The Monthly Salary",value= f"{round(month_salary)} $")
con2.metric("The Annual Salary",value= f"{round(annual_salary)} $")


fig = px.histogram(df,x="annual_salary",title="Annual Salary",template="simple_white",labels={"annual_salary":"Annual Salary"})
st.plotly_chart(fig)