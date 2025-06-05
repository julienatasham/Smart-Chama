import streamlit as st
from chama.chama import create_chama
from chama.members import add_member
from chama.summary import show_summary
from chama.data_handler import save_data, load_data

st.set_page_config(page_title="Smart-Chama", page_icon="💡")

st.title("💡 Smart-Chama: Manage Your Savings Group Easily")

# Step 1: Create or load Chama group name
if "group" not in st.session_state:
    group_name = st.text_input("Enter your Chama group name:")
    if group_name:
        st.session_state.group = create_chama(group_name)
        st.success(f"🎉 Chama '{st.session_state.group}' created successfully!")
else:
    st.write(f"Your Chama group: **{st.session_state.group}**")

# Step 2: Load or initialize members list
if "chama_members" not in st.session_state:
    st.session_state.chama_members = load_data()

# Sidebar menu for navigation
menu = st.sidebar.selectbox("Choose an option", ["Add Member", "Show Summary", "Reset Data"])

if menu == "Add Member":
    st.header("Add a New Member")

    with st.form("add_member_form", clear_on_submit=True):
        name = st.text_input("Member Name")
        amount = st.number_input("Contribution Amount (KES)", min_value=0.0, format="%f")
        submitted = st.form_submit_button("Add Member")

        if submitted:
            if not name.strip():
                st.error("Please enter a valid member name.")
            elif amount <= 0:
                st.error("Contribution amount must be greater than zero.")
            else:
                success = add_member(name.strip(), amount, st.session_state.chama_members)
                if success:
                    save_data(st.session_state.chama_members)
                    st.success(f"✅ Added {name} with KES {amount} contribution.")
                else:
                    st.error("Failed to add member. Please try again.")

elif menu == "Show Summary":
    st.header("Chama Contributions Summary")
    show_summary(st.session_state.chama_members)

elif menu == "Reset Data":
    if st.button("Reset All Data"):
        st.session_state.group = None
        st.session_state.chama_members = []
        save_data([])
        st.success("All data reset successfully. Please refresh the page.")
