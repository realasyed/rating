# Libraries and stuff I guess
import streamlit as st
import pandas as pd
import numpy as np

# Loading and preprocessing data.
dataset = pd.read_csv("imbd_top_1000.csv")
subset = dataset[['Series_Title', 'Genre', 'IMBD_Rating', 'Overview', 'Director']]