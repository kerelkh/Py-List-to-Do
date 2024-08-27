import streamlit as st
import functions


st.title("List To Do")
st.subheader("Please input task")

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['todo']
    todos.append(todo)
    functions.write_todos(todos)
    del st.session_state["todo"]
    st.session_state.todo = ""
    st.info("Data has been added")


st.text_input(key="todo", label="Insert new task", on_change=add_todo, value="")


st.write("Check the box for completing task")
for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}-{i}")
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[f"{todo}-{i}"]
        st.rerun()