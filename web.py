import streamlit as st
import functions

st.title("My To-do App")
st.subheader("This is a subheader")
st.write("This is an app created to improve productivity")

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new to-do...")
