import streamlit as st
from db_process import init_connection
from create_account import create_account
from login import login

st.title("Welcome to the Habit Tracker App")

choice = st.selectbox("Create a new account/Login", ["Create Account", "Login"])

if choice == "Create Account":
    create_account()
elif choice == "Login":    
    login()