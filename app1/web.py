import streamlit as st
import functions

todos = functions.get_todos()
print(todos)

st.title('My Todo App')
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")


for i, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo-{i}")

st.text_input(label="", placeholder="Add a new todo")
