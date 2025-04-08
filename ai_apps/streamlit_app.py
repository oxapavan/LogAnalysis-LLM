import streamlit as st
from streamlit_option_menu import option_menu
import os

# Configuration for the Streamlit web page
st.set_page_config(
    page_title="SmartLog Solutions",
    page_icon="💡",
    layout="wide"
)

# Inject custom CSS (keep your existing style block)
st.markdown("""
    <style>
    /* Your existing CSS styles here */
    </style>
    """, unsafe_allow_html=True)

# Navigation bar
selected = option_menu(
    menu_title=None,
    options=["Home", "Log Exceptions", "RAG Chat", "Dashboard Analyzer"],
    icons=["house", "search", "chat-left-text", "bar-chart"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f8f9fa"},
        "icon": {"color": "orange", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#007BFF"},
    }
)

# Page content
if selected == "Home":
    st.markdown("<h1 class='title'>💡 SmartLog Solutions 💡</h1>", unsafe_allow_html=True)
    st.markdown("""
        Analyze logs and errors with ease using our powerful AI tools. 
        Our platform provides comprehensive analysis capabilities to help you gain insights and optimize your workflows.
        """)

    st.markdown("---")
    st.markdown("### Select an AI App from the navigation bar or the table below to get started.")

    # Create columns for better layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Search Log Exceptions**")
        st.markdown("Search and analyze log exceptions, and their possible remedial actions")
        if st.button("Go to App", key="log_exceptions"):
            st.switch_page("Pages/1_Log_Exceptions.py")

    with col2:
        st.markdown("**RAG Research for Errors**")
        st.markdown("Research and analyze errors with RAG")
        if st.button("Go to App", key="rag_chat"):
            st.switch_page("Pages/2_RAG_Chat.py")

    with col3:
        st.markdown("**Analyzing Dashboards**")
        st.markdown("Analyze and optimize dashboard performance")
        if st.button("Go to App", key="dashboard"):
            st.switch_page("Pages/3_Dashboard_Analyzer.py")

elif selected == "Log Exceptions":
    st.switch_page("Pages/1_Log_Exceptions.py")
    
elif selected == "RAG Chat":
    st.switch_page("Pages/2_RAG_Chat.py")
    
elif selected == "Dashboard Analyzer":
    st.switch_page("Pages/3_Dashboard_Analyzer.py")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>© 2023 SmartLog Solutions</div>", unsafe_allow_html=True)
