import streamlit as st

def show_summary(chama_members):
    """
    Shows member list and total contributions.
    """
    if not chama_members:
        st.info("No members added yet.")
        return
    total = 0
    for member in chama_members:
        st.write(f"- {member['name']}: KES {member['contribution']}")
        total += member['contribution']
    st.markdown(f"### 💰 Total Contributions: KES {total}")
