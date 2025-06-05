# chama/summary.py
import streamlit as st

def show_summary(chama_members, goal):
    if not chama_members:
        st.info("No members added yet.")
        return

    total = sum(m['contribution'] for m in chama_members)
    st.write("### 💰 Total Contributions")
    st.success(f"**KES {total:,.2f}**")

    if goal > 0:
        progress = min(total / goal, 1.0)
        st.progress(progress)
        st.write(f"🎯 Goal: KES {goal:,.0f} | Progress: {progress*100:.1f}%")
