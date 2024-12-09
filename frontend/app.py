import streamlit as st
import requests
import os

API_URL = os.getenv("BACKEND_URL", "http://backend:5000")
st.title("To-Do App")
if 'todos' not in st.session_state:
    st.session_state.todos = []

# Fetch the to-do list
def get_todos():
    response = requests.get(f"{API_URL}/todos")
    if response.status_code == 200:
        return response.json()
    else:
        st.toast("Failed to load to-dos")
        return []


# Add a new to-do task
def add_todo(task):
    response = requests.post(f"{API_URL}/todos", json={"task": task})
    st.session_state.todos = get_todos()
    if response.status_code == 201:
        st.toast("To-do added!")
    else:
        st.toast("Failed to add to-do")


# Update a to-do
def update_todo(todo_id, task, done):
    response = requests.put(f"{API_URL}/todos/{todo_id}", json={"task": task, "done": done})
    st.session_state.todos = get_todos()
    if response.status_code == 200:
        st.toast("To-do updated!")
    else:
        st.toast("Failed to update to-do")


# Delete a to-do
def delete_todo(todo_id):
    response = requests.delete(f"{API_URL}/todos/{todo_id}")
    st.session_state.todos = get_todos()
    if response.status_code == 204:
        st.toast("To-do deleted!")
    else:
        st.toast("Failed to delete to-do")

# Show todos
st.session_state.todos = get_todos()

# Display existing to-dos with edit/delete features
for todo in st.session_state.todos:
    col1, col2, col3 = st.columns([5, 1, 1])
    with col1:
        task_input = st.text_input(f"Task {todo['id']}", value=todo['task'], key=todo['id'])
    with col2:
        done_checkbox = st.checkbox("Done", value=todo['done'], key=f"done_{todo['id']}")
    with col3:
        st.button("Delete", on_click=delete_todo, args=(todo['id'],), key=f"delete_{todo['id']}")
    if st.button("Update", key=f"update_{todo['id']}"):
        update_todo(todo['id'], task_input, done_checkbox)

# Add a new to-do section
st.text_input("New Task", key="new_task")
if st.button("Add"):
    new_task = st.session_state.get("new_task")
    if new_task:
        add_todo(new_task)
        st.session_state.todos = get_todos()
    else:
        st.toast("Please enter a task")
