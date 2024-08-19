import streamlit as st
import functions

todos = functions.get_todos("/Users/abdallahadel/PycharmProjects/pythonProject/venv/Web-App/todoo.txt")


def add_todo():
    to = st.session_state['new_todo'] + "\n"
    todos.append(to)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo web-app")
st.write("This is made to increase productivity")

for index, to in enumerate(todos):
    checkbox = st.checkbox(to, key=to)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[to]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo , key='new_todo')