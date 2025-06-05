import streamlit as st
from auth import login_user, register_user
from dashboard import show_dashboard

# Set page title
st.set_page_config(page_title="Smart Chama", layout="wide")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# ---------------- LOGIN FORM ----------------
def show_login():
    st.title("🔐 Login to Smart Chama")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(email, password):
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success("Login successful!")
