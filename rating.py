# Libraries and stuff I guess
import streamlit as st
import pandas as pd
import numpy as np

# Loading and preprocessing data.
dataset = pd.read_csv("imdb_top_1000.csv")
subset = dataset[['Series_Title', 'Genre', 'IMDB_Rating', 'Overview', 'Director', 'Gross']]
# st.write(subset)

dep = subset.iloc[['IMDB_Rating', 'Gross']].values
indep = subset.iloc[['Series_Title', 'Genre', 'Overview', 'Director']].values
st.write(dep)
st.write(indep)
# data is not just numbers so .values not workin idk 