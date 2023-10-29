import streamlit as st
import app_logic as al

st.title("Add document") 



with st.form('my_form'):
    text = st.text_area('Enter text:', key='input')
    submitted = st.form_submit_button('Submit')
    if submitted:
        al.add_to_corpus(text)
        text = st.empty()
        st.success('Document added')
        clear = st.form_submit_button('Clear')