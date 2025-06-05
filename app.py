# app.py
import streamlit as st
from chama import create_chama
from chama.members import add_member
from chama.summary import show_summary
from chama.data_handler import save_data, load_data

# Load data from JSON file
chama_members = load_data()

# Sidebar
st.sidebar.title("📌 Smart-Chama Menu")
group_name = st.sidebar.text_input("Enter your Chama group name", value="My Chama")
goal = st.sidebar.number_input("Set a savings goal (KES)", min_value=0, value=10000)

# Main Title
st.title("👩🏾‍🤝‍👩🏿 Smart-Chama: Group Savings Made Easier")

# Add Member Section
st.header("➕ Add Member")
with st.form("add_form"):
    name = st.text_input("Member Name")
    amount = st.number_input("Contribution (KES)", min_value=0.0, step=100.0)
    submitted = st.form_submit_button("Add Member")

    if submitted:
        if name and amount:
            add_member(chama_members, name, amount)
            save_data(chama_members)
            st.success(f"✅ {name} added with KES {amount}")
        else:
            st.error("Please enter both name and amount.")

# Show Summary
st.header("📊 Summary")
show_summary(chama_members, goal)

# Bar Chart
if chama_members:
    st.subheader("📈 Contribution Chart")
    import pandas as pd
    df = pd.DataFrame(chama_members)
    st.bar_chart(data=df, x="name", y="contribution")
