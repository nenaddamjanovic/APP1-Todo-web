import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    local_todo = st.session_state["key_new_todo"].strip() + "\n"
    todos.append(local_todo)
    write_todos(todos)


st.title("my todo app")
st.subheader("This is my todo app :)")
st.write("You increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Enter a new todo...",
              on_change=add_todo, key="key_new_todo")

st.session_state