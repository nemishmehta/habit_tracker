import streamlit as st
from db_process import init_connection
from create_account import create_account
from login import login


conn = init_connection()

st.title("Welcome to the Habit Tracker App")

choice = st.selectbox("Create a new account/Login", ["Create Account", "Login"])

if choice == "Create Account":
    acc_details = create_account()
elif choice == "Login":    
    login()

st.write(st.session_state)
