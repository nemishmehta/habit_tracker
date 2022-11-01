from auth0_component import login_button
import streamlit as st

clientId = "IOTZaxFt4kRkWrYS0X1mNpG5u6djaEwZ"
domain = "dev-oa5q2fnsyge0ny7n.eu.auth0.com"

user_info = login_button(clientId, domain = domain)
st.write(user_info)