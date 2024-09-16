import streamlit as st
import sys
sys.path.append('')
from moduless import to_do_functions

todos = to_do_functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    to_do_functions.write_todos(todos)

st.title("My To-Do App")
st.subheader("This is my daily to-do app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #print(checkbox)
        todos.pop(index)
        to_do_functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a To-DO: ", placeholder="Add New To-Do......",
              on_change=add_todo, key='new_todo')

# print("hello")
#
# st.session_state