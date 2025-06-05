
import streamlit as st
# Initialize session variables
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'user_email' not in st.session_state:
    st.session_state['user_email'] = ""
from dashboard import main as dashboard_main
from auth import login_user, signup_user

st.set_page_config(page_title="Smart Chama", layout="wide")

# Session state setup
if "logged_in" not in st.session_state:
    st.session_state [logged_in] = False
if "user_email" not in st.session_state:
    st.session_state [user_email] = ""

# ----------- Login Page ------------
def login_page():
    st.title("🔐 Login to Smart Chama")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(email, password):
            st.session_state[logged_in] = True
            st.session_state [user_email] = email
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
    st.title("Welcome to Smart Chama")

    # Step 1: Page selector — lets user choose Login or Sign Up
    page = st.radio("Choose action", ["Login", "Sign Up"])

    if page == "Login":
        # Login page inputs
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if email and password:
                # Your login authentication logic here
                st.success(f"Logged in as {email}")
                # Redirect or show dashboard here
            else:
                st.error("Please enter email and password")

    elif page == "Sign Up":
        # Sign Up page inputs
        name = st.text_input("Your Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Sign Up"):
            if name and email and password:
                # Your sign up logic here (e.g., save user, hash password)
                st.success(f"Account created for {name}!")
                # Possibly auto-login or redirect
            else:
                st.error("Please fill in all the fields")

        if st.session_state['logged_in']:
            dashboard_main()

if __name__ == "__main__":
    main()

