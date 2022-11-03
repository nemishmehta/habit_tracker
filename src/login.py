import streamlit as st
from db_process import select_query

def check_user_exist(email_id, password):
    user_exist_query = select_query(
        f"SELECT EXISTS (SELECT 1 FROM users WHERE email_id = '{email_id}');")
    user_exist_bool = user_exist_query[0][0]
    
    if user_exist_bool is True:
        user_details = select_query(f"SELECT * FROM users WHERE (email_id = '{email_id}' AND password = crypt('{password}', password));")
        if bool(user_details) is False:
            st.write("Password provided is incorrect.")
        else:
            st.session_state['user_id'] = user_details[0][0]
            st.session_state['email_id'] = user_details[0][1]
            st.session_state['first_name'] = user_details[0][3]
            st.session_state['last_name'] = user_details[0][4]
            return True      
    else:
        st.write("Account does not exist. Please create a new account.")

def login():
    with st.form("login", clear_on_submit=False):
        st.title("Login")
        email_id = st.text_input("E-mail address")
        password = st.text_input("Password", type="password")
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            user_login = check_user_exist(email_id, password)        

            if user_login is True:
                st.write("Logged in successfully.")

        
        
    