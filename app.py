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
            st.experimental_rerun()
        else:
            st.error("Incorrect email or password.")

# ---------------- REGISTER FORM ----------------
def show_register():
    st.title("📝 Register for Smart Chama")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if register_user(email, password):
            st.success("Registration successful! Please log in.")
        else:
            st.error("Email already registered.")

# ---------------- MAIN ROUTER ----------------
def main():
    if st.session_state.logged_in:
        show_dashboard(st.session_state.user_email)
    else:
        menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
        if menu == "Login":
            show_login()
        else:
            show_register()

if _name_ == "_main_":
    main()
