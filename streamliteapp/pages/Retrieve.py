import streamlit as st
import app_logic as al

st.title("Retrieve document") 


if 'show' not in st.session_state:
    st.session_state['show'] = False
if 'passage' not in st.session_state:
    st.session_state['passage'] = None
if 'summary_show' not in st.session_state:
    st.session_state['summary_show'] = None

with st.form('my_form'):
    text = st.text_area('Enter text:', '')
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.session_state['show'] = True
        st.session_state['passage'] = al.retrieve_passage(text)

if st.session_state['show']:
    st.info(st.session_state['passage'])
    summary = st.button('Summarize')
    if summary:
        st.session_state['summary_show'] = True
        st.session_state['show'] = False
        st.rerun()

if st.session_state['summary_show']:
    st.success(al.summarize(st.session_state['passage']))
    st.session_state['passage'] = None
    st.session_state['summary_show'] = False
    clear = st.button('Clear')
    if clear:
        st.rerun()