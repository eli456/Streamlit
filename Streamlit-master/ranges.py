import streamlit as st
import pandas as pd

st.title('Streamlit - Search names')

DATA_URL = ('/content/dataset.csv')

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_cvs(DATA_URL)
    filtered_data_byrange = data[ (data ['index'] >= startid) & (data ['index'] <= endid) ]
    
    return filtered_data_byrange

startid = st.text_input('Start index :')
endid = st.text_input('End index :')
btnRange = st.button('Seach by range')

if (btnRange):
    filterbyrange = load_data_byrange(int(startid), int(endid))
    count_row = filterbyrange.shape[0] #Gives number of row
    st.write(f"Total ites : {count_row}")
    
    st.dataframe(filterbyrange)
