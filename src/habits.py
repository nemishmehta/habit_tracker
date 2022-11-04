import streamlit as st

def select_habit():
    #habits_list = ['Staying fit', 'Saving money', 'Eating healthy']
    habits_list = ['Staying fit']
    chosen_habit = st.selectbox("Select a habit.", habits_list)
    return chosen_habit