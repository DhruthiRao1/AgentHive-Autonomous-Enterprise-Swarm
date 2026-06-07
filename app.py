import streamlit as st
from swarm import run_swarm

st.title('AgentHive - Multi-Agent Service Desk')

ticket = st.text_area('Enter Incident')

if st.button('Run Swarm'):
    output = run_swarm(ticket)
    st.subheader('Plan')
    st.json(output['plan'])

    st.subheader('Resolution')
    st.write(output['result']['answer'])

    st.metric('Confidence', output['result']['confidence'])
