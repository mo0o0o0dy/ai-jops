import streamlit as st
import pandas as pd

st.set_page_config("Main Home",page_icon="🔥",layout="wide")
st.header("🔥Ai Jobs Analysis")
st.write("These Are Some Ai Jobs Analyses About Modern Ai Jobs")

df = pd.read_csv("ai_job_dataset.csv")
st.dataframe(df.head(10))