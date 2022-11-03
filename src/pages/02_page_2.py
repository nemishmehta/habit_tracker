import streamlit as st
import datetime
from db_process import insert_query, select_query

# Session state loses info when a habit is selected.
st.header(f"Welcome, {st.session_state['first_name']} {st.session_state['last_name']}")

def select_habit():
    #habits_list = ['Staying fit', 'Saving money', 'Eating healthy']
    habits_list = ['Staying fit']
    chosen_habit = st.selectbox("Select a habit.", habits_list)
    return chosen_habit

habits_table = {"Staying fit": "stay_fit"}

def check_exist_habit_val(db_habit, user_id, entry_date):
    
    exist_habit_val = select_query(f"SELECT * FROM {db_habit} WHERE (user_id = '{user_id}' AND entry_date = '{entry_date}');")
    
    return bool(exist_habit_val)

def add_habit_val(habit, user_id, entry_date, entry_val):
    db_habit = habits_table[habit]
    
    if check_exist_habit_val(db_habit, user_id, entry_date) is True:
        st.write("Entry already exists.")
        st.write(f"UPDATE {db_habit} SET entry_val = '{entry_val}' WHERE (user_id = '{user_id}' AND entry_date = '{entry_date}');")
        update_habit_bool = insert_query(f"UPDATE {db_habit} SET entry_val = '{entry_val}' WHERE (user_id = '{user_id}' AND entry_date = '{entry_date}');")
        return update_habit_bool
    else:
        add_habit_bool = insert_query( 
            f"INSERT INTO {db_habit} (entry_id, user_id, entry_date, entry_val) VALUES (uuid_generate_v4(), '{user_id}', '{entry_date}', '{entry_val}');")
        return add_habit_bool

def update_habit():
    with st.form("update_habit", clear_on_submit=False):
        st.title("Habit Tracking")
    
        chosen_habit = select_habit()
    
        date = st.date_input(
                "Select date", 
                min_value=datetime.date(1920, 1, 1), 
                max_value=datetime.date.today())
        
        habit_val = st.radio("Did you work out?", ["Yes", "No"])
        st.write(habit_val)
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
    
            if chosen_habit and date and habit_val:
                
                add_habit_db = add_habit_val(chosen_habit, st.session_state["user_id"], date, habit_val)
                if add_habit_db:
                    st.write("Habit tracker updated.")
                else:
                    st.write("Error updating habit tracker. Please contact administrator.")   
            
    
update_habit()
st.session_state