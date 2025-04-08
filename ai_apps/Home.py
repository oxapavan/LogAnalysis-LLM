import nest_asyncio
import streamlit as st
from streamlit_option_menu import option_menu  # For the navigation bar

# Apply necessary asyncio patches for Streamlit
nest_asyncio.apply()

# Configuration for the Streamlit web page
st.set_page_config(
    page_title="Log AI Analyzer",
    page_icon=":orange_heart:",
    layout="wide"
)

# Custom CSS for the app
st.markdown("""
    <style>
    /* Main content padding */
    .main .block-container {
        padding-top: 2rem;
    }
    /* Sidebar styling */
    div[data-testid="stSidebar"] {
        background-color: #007BFF;
        color: #ffffff;
    }
    div[data-testid="stSidebar"] a {
        color: #ffffff;
    }
    div[data-testid="stSidebar"] .stButton > button {
        color: #ffffff;
        background-color: #0056b3;
    }
    /* Navigation bar styling */
    .st-eb {
        padding: 0.5rem;
    }
    .css-1wivap2.e16fv1kl3 {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation bar
selected = option_menu(
    menu_title=None,
    options=["Home", "Search Log Exceptions", "RAG Research", "Dashboard Analysis"],
    icons=["house", "search", "book", "bar-chart"],
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

# Main content based on navigation selection
if selected == "Home":
    # Home page content
    st.markdown("<h1 style='text-align: center;'>💡 Log AI Analyzer 💡</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center; font-size: 18px;'>
        Analyze logs and errors with ease using our powerful AI tools. 
        Our platform provides comprehensive analysis capabilities to help you gain insights and optimize your workflows.
        </p>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # App features table
    st.markdown("""
    <table style="width:100%">
      <tr>
        <th style="width:30%">App Name</th>
        <th>Description</th>
      </tr>
      <tr>
        <td><b>Search Log Exceptions</b></td>
        <td>Search and analyze log exceptions with advanced filtering and pattern recognition</td>
      </tr>
      <tr>
        <td><b>RAG Research for Errors</b></td>
        <td>Research and analyze errors using Retrieval-Augmented Generation (RAG) technology</td>
      </tr>
      <tr>
        <td><b>Dashboard Analysis</b></td>
        <td>Analyze and optimize dashboard performance with AI-powered insights</td>
      </tr>
    </table>
    """, unsafe_allow_html=True)

elif selected == "Search Log Exceptions":
    st.title("Search Log Exceptions")
    st.write("This is the Search Log Exceptions app page.")
    # Add your actual search functionality here
    
elif selected == "RAG Research":
    st.title("RAG Research for Errors")
    st.write("This is the RAG Research app page.")
    # Add your RAG functionality here
    
elif selected == "Dashboard Analysis":
    st.title("Analyzing Dashboards")
    st.write("This is the Dashboard Analysis app page.")
    # Add your dashboard analysis functionality here

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>© 2023 Log AI Analyzer</div>", unsafe_allow_html=True)
