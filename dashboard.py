
import streamlit as st
from chama.chama import load_chamas_for_user, create_chama_for_user

def show_dashboard(email):
    st.title(f"🏠 Welcome, {email}")
    st.markdown("## Your Chamas")

    chamas = load_chamas_for_user(email)

    if chamas:
        for chama in chamas:
            st.subheader(chama['name'])
            st.write(f"👥 Members: {len(chama['members'])}")
            st.write(f"💰 Transactions: {len(chama['transactions'])}")
    else:
        st.info("You haven't created any Chamas yet.")

    st.markdown("---")

    with st.form("create_chama"):
        st.subheader("➕ Create a New Chama")
        new_name = st.text_input("Chama Name")
        submitted = st.form_submit_button("Create")
        if submitted and new_name:
            create_chama_for_user(email, new_name)
            st.success(f"Chama '{new_name}' created!")
            st.experimental_rerun()

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_email = ""
        st.experimental_rerun()
