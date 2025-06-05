
import streamlit as st
from auth import login_user, register_user
from dashboard import show_dashboard

st.set_page_config(page_title="Smart Chama", layout="wide")

# Session state setup
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# ----------- Login Page ------------
def login_page():
    st.title("🔐 Login to Smart Chama")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(email, password):
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.experimental_rerun()
        else:
            st.error("Incorrect email or password")

# ----------- Registration Page ------------
def register_page():
    st.title("📝 Register New Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if register_user(email, password):
            st.success("Registered! Please login.")
        else:
            st.error("Email already exists")

# ----------- Main Router ------------
import streamlit as st

def main():
    st.title("Login Page")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email and password:
            # call your auth function, e.g. auth.login_user(email, password)
            st.success(f"Logged in as {email}")
            # maybe redirect or show dashboard here
        else:
            st.error("Please enter email and password")
if login_successful:
    st.session_state['user_email']= email
if _name_ == "_main_":
    main()
