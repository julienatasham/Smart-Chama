import streamlit as st
from auth import register_user, login_user
import json
import os

CHAMAS_FILE = 'chamas.json'

def load_chamas():
    if not os.path.exists(CHAMAS_FILE):
        return []
    with open(CHAMAS_FILE, 'r') as f:
        return json.load(f)

def save_chamas(chamas):
    with open(CHAMAS_FILE, 'w') as f:
        json.dump(chamas, f, indent=4)

def get_next_id(chamas):
    if not chamas:
        return 1
    return max(chama['id'] for chama in chamas) + 1

def chama_management():
    st.subheader("Add New Chama")
    name = st.text_input("Chama Name")
    details = st.text_area("Chama Details")

    if st.button("Add Chama"):
        if not name.strip():
            st.error("Chama name cannot be empty.")
        else:
            chamas = load_chamas()
            new_id = get_next_id(chamas)
            chamas.append({"id": new_id, "name": name.strip(), "details": details.strip()})
            save_chamas(chamas)
            st.success(f"Chama '{name}' added successfully with ID {new_id}!")

    st.subheader("Existing Chamas")
    chamas = load_chamas()
    if chamas:
        for chama in chamas:
            st.write(f"ID: {chama['id']} | Name: {chama['name']} | Details: {chama['details']}")
    else:
        st.info("No chamas found.")

def main():
    st.title("Chama App with User Login")

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.email = ""

    menu = ["Login", "Register"]
    if st.session_state.logged_in:
        menu.append("Logout")
        menu.append("Manage Chamas")

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login_user(email, password):
                st.success(f"Welcome back, {email}!")
                st.session_state.logged_in = True
                st.session_state.email = email
            else:
                st.error("Invalid email or password")

    elif choice == "Register":
        st.subheader("Create New Account")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_password")
        password2 = st.text_input("Confirm Password", type="password", key="reg_password2")
        if st.button("Register"):
            if not email or not password or not password2:
                st.error("Please fill in all fields")
            elif password != password2:
                st.error("Passwords do not match")
            else:
                if register_user(email, password):
                    st.success("Registration successful! You can now login.")
                else:
                    st.error("Email already registered.")

    elif choice == "Logout":
        st.session_state.logged_in = False
        st.session_state.email = ""
        st.success("You have logged out.")

    elif choice == "Manage Chamas":
        if st.session_state.logged_in:
            st.write(f"Logged in as: {st.session_state.email}")
            chama_management()
        else:
            st.error("Please login first.")

if __name__ == "__main__":
    main()
