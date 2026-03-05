import streamlit as st
import plotly.express as px
import pandas as pd

# datos de ejemplo
df = px.data.tips()

# gráfico
fig = px.scatter(df, x="total_bill", y="tip", color="sex")

st.title("Mi gráfico interactivo")

st.plotly_chart(fig)