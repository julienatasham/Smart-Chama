import streamlit as st
from chama import create_chama
from chama.members import add_member
from chama.summary import show_summary

st.title("Welcome to Smart-Chama, saving made easier")
st.write("This tool will help Kenyan women manage and optimize Chama Groups.")

# Create or load the chama group name
if "group" not in st.session_state:
    st.session_state.group = create_chama()

# Initialize members list in session state (to keep data live during session)
if "chama_members" not in st.session_state:
    st.session_state.chama_members = []

# Sidebar menu
option = st.sidebar.selectbox("Choose an option:", ["Add Member", "Show Summary", "Exit"])

if option == "Add Member":
    st.header("Add a Chama Member")
    name = st.text_input("Enter member name:")
    amount = st.number_input(f"Enter {name}'s contribution amount (KES):", min_value=0.0)

    if st.button("Add Member"):
        if name and amount > 0:
            add_member(name, amount, st.session_state.chama_members)
            st.success(f"✅ Added {name} with contribution of KES {amount}")
        else:
            st.error("Please enter a valid name and amount.")

elif option == "Show Summary":
    st.header("Chama Summary")
    show_summary(st.session_state.chama_members)

elif option == "Exit":
    st.write(f"👋 Thanks for using Smart-Chama, {st.session_state.group}!")
    st.stop()

