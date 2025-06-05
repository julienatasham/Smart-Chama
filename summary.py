import streamlit as st

def show_summary(members_list):
    if not members_list:
        st.info("No members added yet.")
        return
    total = 0
    for member in members_list:
        st.write(f"- {member['name']}: KES {member['contribution']}")
        total += member['contribution']
    st.write(f"💰 Total Contributions: KES {total}")

