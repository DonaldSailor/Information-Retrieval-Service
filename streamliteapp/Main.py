import streamlit as st
import app_logic as al

st.set_page_config(
    page_title="Main Page",
    page_icon="Main Page",
)
st.title("Retrieval System") 

st.success('Example documents from database')


for document in al.get_random_examples():
    st.info(document)
