import streamlit as st
from db_process import select_query
from habits import select_habit
import altair as alt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as pg

# Different habits progression on the same bar chart --> see Streamlit plotly
st.session_state

st.header(f"Dashboard - {st.session_state['first_name']}")

chosen_habit = select_habit()
habits_table = {"Staying fit": "stay_fit"}

# user name, entry_date, entry_val
#@st.experimental_memo(ttl=300)
def habit_bar_chart():
    db_habit = habits_table[chosen_habit]
    habit_history = select_query(f"SELECT entry_date, entry_val FROM {db_habit} WHERE user_id = '{st.session_state['user_id']}' ORDER BY entry_date ASC;")    
    records = {"date": [], "val": []}
    for record in habit_history:
        records["date"].append(record[0])
        if record[1] is True:
            records["val"].append(1)
        else:
            records["val"].append(-1)
    return records

def weekly_habit_history(habit_history_val):
    
    fig = px.bar(data_frame=habit_history_val, x='date', y='val', range_y=[-1.25,1.25])
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=False)
    

habit_history_val = habit_bar_chart()

weekly_habit_history(habit_history_val)