import streamlit as st
from streamlit_option_menu import option_menu

# Configuration for the Streamlit web page
st.set_page_config(
    page_title="SmartLog Solutions",
    page_icon="💡",
    layout="wide"
)

# Custom CSS (keep your existing styles)
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
    /* Table styling */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
    }
    th, td {
        padding: 12px 15px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    th {
        background-color: #f2f2f2;
    }
    tr:hover {
        background-color: #f5f5f5;
    }
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

# Page routing using query parameters
query_params = st.experimental_get_query_params()

if selected == "Log Exceptions" or query_params.get("page", [""])[0] == "log_exceptions":
    st.experimental_set_query_params(page="log_exceptions")
    from Pages import Log_Exceptions
    Log_Exceptions.main()
elif selected == "RAG Chat" or query_params.get("page", [""])[0] == "rag_chat":
    st.experimental_set_query_params(page="rag_chat")
    from Pages import RAG_Chat
    RAG_Chat.main()
elif selected == "Dashboard Analyzer" or query_params.get("page", [""])[0] == "dashboard":
    st.experimental_set_query_params(page="dashboard")
    from Pages import Dashboard_Analyzer
    Dashboard_Analyzer.main()
else:
    # Home page content
    st.markdown("<h1 class='title'>💡 SmartLog Solutions 💡</h1>", unsafe_allow_html=True)
    st.markdown("""
        Analyze logs and errors with ease using our powerful AI tools. 
        Our platform provides comprehensive analysis capabilities to help you gain insights and optimize your workflows.
        """)

    st.markdown("---")
    st.markdown("### Select an AI App from the navigation bar or the links below to get started.")

    # Navigation links
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Search Log Exceptions")
        st.markdown("Search and analyze log exceptions, and their possible remedial actions")
        if st.button("Go to App", key="log_exceptions"):
            st.experimental_set_query_params(page="log_exceptions")
            st.rerun()

    with col2:
        st.markdown("#### RAG Research for Errors")
        st.markdown("Research and analyze errors with RAG")
        if st.button("Go to App", key="rag_chat"):
            st.experimental_set_query_params(page="rag_chat")
            st.rerun()

    with col3:
        st.markdown("#### Analyzing Dashboards")
        st.markdown("Analyze and optimize dashboard performance")
        if st.button("Go to App", key="dashboard"):
            st.experimental_set_query_params(page="dashboard")
            st.rerun()

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>© 2023 SmartLog Solutions</div>", unsafe_allow_html=True)
