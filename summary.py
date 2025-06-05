import streamlit as st

def show_summary(members_list):
    if not members_list:
        st.info("No members added yet.")
        return

    total = sum(m["contribution"] for m in members_list)
    for m in members_list:
        st.write(f"{m['name']}: KES {m['contribution']}")
    st.subheader(f"💰 Total Contributions: KES {total}")

