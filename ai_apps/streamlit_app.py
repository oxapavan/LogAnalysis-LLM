import streamlit as st
from streamlit_option_menu import option_menu

# Configuration for the Streamlit web page
st.set_page_config(
    page_title="SmartLog Solutions",
    page_icon="💡",
    layout="wide"
)

# Inject custom CSS for sidebar and main content styling
st.markdown(
    """
    <style>
    /* Sidebar styles */
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

    /* Main title styling */
    .title {
        font-size: 3em;
        text-align: center;
        padding-bottom: 20px;
        animation: glow 2s linear infinite alternate;
        text-shadow: 0 0 10px #007BFF, 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3;
    }

    /* Animation for glowing effect */
    @keyframes glow {
        from {
            text-shadow: 0 0 10px #007BFF, 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3;
        }
        to {
            text-shadow: 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3, 0 0 200px #0056b3, 0 0 300px #0056b3;
        }
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
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 20px;
    }
    th, td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    th {
        background-color: #f2f2f2;
        color: #333;
    }
    tr:hover {
        background-color: #f5f5f5;
        border: 3px solid #ccc;
    }
    tr:hover td {
        color: #000;
    }
    
    /* Button styling */
    .nav-button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 8px 16px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

# Page routing
if selected == "Home":
    # Main title of the application with emojis and paragraph
    st.markdown("<h1 class='title'>💡 SmartLog Solutions 💡</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        Analyze logs and errors with ease using our powerful AI tools. 
        Our platform provides comprehensive analysis capabilities to help you gain insights and optimize your workflows.
        """
    )

    st.markdown("---")
    st.markdown("### Select an AI App from the navigation bar or the table below to get started.")

    # Beautified table with navigation buttons
    st.markdown(
        """
        <table>
          <tr>
            <th>App Name</th>
            <th>Description</th>
            <th>Action</th>
          </tr>
          <tr>
            <td>Search Log Exceptions</td>
            <td>Search and analyze log exceptions, and their possible remedial actions</td>
            <td><button class="nav-button" onclick="window.location.href='./Pages/1_Log_Exceptions'">Go to App</button></td>
          </tr>
          <tr>
            <td>RAG Research for Errors</td>
            <td>Research and analyze errors with RAG</td>
            <td><button class="nav-button" onclick="window.location.href='./Pages/2_RAG_Chat'">Go to App</button></td>
          </tr>
          <tr>
            <td>Analyzing Dashboards</td>
            <td>Analyze and optimize dashboard performance</td>
            <td><button class="nav-button" onclick="window.location.href='./Pages/3_Dashboard_Analyzer'">Go to App</button></td>
          </tr>
        </table>
        """,
        unsafe_allow_html=True
    )

elif selected == "Log Exceptions":
    st.switch_page("./Pages/1_Log_Exceptions.py")
    
elif selected == "RAG Chat":
    st.switch_page("./Pages/2_RAG_Chat.py")
    
elif selected == "Dashboard Analyzer":
    st.switch_page("./Pages/3_Dashboard_Analyzer.py")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>© 2023 SmartLog Solutions</div>", unsafe_allow_html=True)
