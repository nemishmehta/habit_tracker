import streamlit as st
from db_process import init_connection, select_query

conn = init_connection()

def check_user_exist(email_id, password):
    user_exist_query = select_query(
        conn, 
        f"SELECT EXISTS (SELECT 1 FROM users WHERE (email_id = '{email_id}' AND password = crypt('{password}', password)));"
        )
    user_exist_bool = user_exist_query[0][0]
    if user_exist_bool is True:
        st.write("Login successful.")
    else:
        st.write("Account credentials are incorrect. Please enter them again.")

def login():
    with st.form("login", clear_on_submit=False):
        st.title("Login")
        email_id = st.text_input("E-mail address")
        password = st.text_input("Password", type="password")
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            check_user_exist(email_id, password)        
        

        
        
    