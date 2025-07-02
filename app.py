import streamlit as st
st.title ("Hello World")
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)
column= df.columns
if st.button("Send Balloons"):
    st.balloons()
    column = ['col 0', 'col 1']
    #st.table(df)
st.table(df[column])

st.text(column)