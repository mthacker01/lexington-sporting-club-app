import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('database.sqlite')
df = pd.read_sql(sql='SELECT * FROM players', con=conn)

st.dataframe(df)