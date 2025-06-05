import streamlit as st
import pandas as pd

# Custom CSS styles for better design
st.markdown("""
<style>
    .title {
        font-size: 36px;
        font-weight: 700;
        color: #0d6efd;
        text-align: center;
        margin-bottom: 20px;
    }
    .highlight-box {
        background-color: #f0f8ff;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
    }
    .footer {
        font-size: 12px;
        color: #888;
        text-align: center;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Smart Chama Optimization Tool</div>', unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("User Inputs")
    member_name = st.text_input("Member Name")
    contribution = st.number_input("Contribution Amount (KES)", min_value=0)
    month = st.selectbox("Month", options=["January", "February", "March", "April"])

# Main layout with two columns
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.subheader("Summary")
    if member_name:
        st.write(f"Member: **{member_name}**")
        st.write(f"Contribution: **KES {contribution:,}**")
        st.write(f"Month: **{month}**")
    else:
        st.info("Please enter member info on the sidebar.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("Contributions Over Time")
    # Replace with your real data or logic
    data = pd.DataFrame({
        "Month": ["January", "February", "March", "April"],
        "Contribution": [1000, 1500, 1300, 1600]
    }).set_index("Month")
    st.bar_chart(data)

# Footer
st.markdown('<div class="footer">© 2025 Smart Chama Project</div>', unsafe_allow_html=True)
