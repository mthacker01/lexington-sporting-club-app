import streamlit as st
import polars as pl
import sqlite3

conn = sqlite3.connect('database.sqlite')
df = pl.read_database(query='SELECT * FROM players', connection=conn)

st.dataframe(df)