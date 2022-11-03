import streamlit as st
import psycopg2

@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

@st.experimental_memo(ttl=600)
def select_query(query):
    conn = init_connection()
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
@st.experimental_memo(ttl=600)
def insert_query(query):
    conn = init_connection()
    with conn.cursor() as cur:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(f"{e}")
            return False
        return True