import streamlit as st
from email_validator import validate_email, EmailNotValidError
import datetime
from db_process import init_connection, select_query, insert_query

conn = init_connection()
    
def verify_valid_email(input_email_id, is_new_account):

    try:
        validation = validate_email(input_email_id, check_deliverability=is_new_account)
        verified_email_id = validation.email
        return verified_email_id, True
    except EmailNotValidError as e:
        return input_email_id, False
    
def verify_exist_email(verified_email):
    email_exist_query = select_query(
        conn, 
        f"SELECT EXISTS (SELECT 1 FROM users WHERE email_id = '{verified_email}');"
        )
    email_exist_bool = email_exist_query[0][0]
    return email_exist_bool

def password_check(password, verification_password):
    return password == verification_password 
    
def add_user_to_db(first_name, last_name, verified_email, password, date_of_birth):
    add_user_bool = insert_query(
        conn, 
        f"INSERT INTO users (user_id, email_id, password, first_name, last_name, date_of_birth) VALUES (uuid_generate_v4(), '{verified_email}', crypt('{password}', gen_salt('md5')), '{first_name}', '{last_name}', '{date_of_birth}');"
    )
    
    return add_user_bool

def create_account():
    with st.form("create_account", clear_on_submit=False):
        st.title("Create Account")
        first_name = st.text_input("First name")
        last_name = st.text_input("Last name")
        input_email_id = st.text_input("E-mail address")
        
        password = st.text_input("Password", type="password")
        verification_password = st.text_input("Re-enter password", type="password")
        
        date_of_birth = st.date_input(
            "Date of birth", 
            min_value=datetime.date(1920, 1, 1), 
            max_value=datetime.date.today())
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if password_check(password, verification_password) is False:
                st.write("Passwords do not match. Please re-enter passwords again.") 
                
            verified_email, verification_value = verify_valid_email(input_email_id, is_new_account = True)
            if verification_value is False:
                st.write(f"{verified_email}: E-mail address is invalid.")
            
            email_exists_val = verify_exist_email(verified_email)
            if email_exists_val is True:
                st.write(f"{verified_email} already exists. Please use a different e-mail.") 
            
            if verification_value is True and email_exists_val is False and password == verification_password:
                user_added = add_user_to_db(first_name, last_name, verified_email, password, date_of_birth)
                
                if user_added is True:
                    st.write("User has been added successfully.")
                else:
                    st.write("Error adding user. Please contact administrator.")



