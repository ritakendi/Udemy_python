import streamlit as st
import functions

todos = functions.get_todos()
print(todos)

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

if todos:
    for i, todo in enumerate(todos):
        st.checkbox(todo, key=f"todo-{i}")

st.text_input(label="", placeholder="Add a new todo...",
                on_change = add_todo, key="new_todo")
