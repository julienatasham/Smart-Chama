# dashboard.py
import streamlit as st
from chama.chama import load_chamas_for_user, create_chama_for_user

def show_dashboard(email):
    st.title(f"🏠 Welcome, {email}")
    st.markdown("### 📋 Your Chamas:")

    chamas = load_chamas_for_user(email)

    if chamas:
        for chama in chamas:
            st.subheader(chama['name'])
            st.markdown(f"- 👥 Members: {len(chama['members'])}")
            st.markdown(f"- 💰 Transactions: {len(chama['transactions'])}")
    else:
        st.info("You haven't created any Chamas yet.")

    st.markdown("---")

    with st.form("create_chama_form"):
        st.subheader("➕ Create a New Chama")
        new_chama_name = st.text_input("Enter Chama Name")
        submitted = st.form_submit_button("Create Chama")
        if submitted and new_chama_name:
            create_chama_for_user(email, new_chama_name)
            st.success(f"Chama '{new_chama_name}' created!")
            st.experimental_rerun()

    if st.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.session_state.user_email = ""
        st.experimental_rerun()
