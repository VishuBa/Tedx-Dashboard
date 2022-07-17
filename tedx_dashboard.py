from cProfile import label
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

df = pd.read_csv('tedxVideos.csv')
overview = pd.read_csv('tedxOverview.csv')


df_agg_dif = df.copy()
# median_val = df.median()
# numeric_cols = np.array((df.dtypes == 'float64') | (df.dtypes == 'int64'))
# df_agg_dif.iloc[:, numeric_cols] = (df_agg_dif[:, numeric_cols] - median_val ).div(median_val)


#build dashboard

add_sidebar = st.sidebar.selectbox('Aggregate or Individual Video', ('Aggregate Metrics', 'Individual Video Analysis'))

# adding pages
if add_sidebar == 'Aggregate Metrics':
    st.title(overview['Channel_name'].item())
    col1, col2, col3 = st.columns(3)
    col1.metric('Subscribers', overview['Subscribers'].item())
    col2.metric('Views', overview['Views'].item())
    col3.metric('Total_videos', overview['Total_videos'].item())
    st.text('Raw data')
    st.dataframe(df)
if add_sidebar == 'Individual Video Analysis':
    st.write('Ind')
