import streamlit as st

def main():
    # Sidebar Navigation
    selected_app = st.sidebar.selectbox(
        "Choose an AI App",
        ["Home", "Search Log Exceptions", "RAG Research for Errors", "Analyzing Dashboards"]
    )

    # Display content based on selection
    if selected_app == "Home":
        st.markdown("### Select an AI App from the sidebar to get started.")
        show_app_list()
    elif selected_app == "Search Log Exceptions":
        st.markdown("## Search Log Exceptions App Coming Soon...")
    elif selected_app == "RAG Research for Errors":
        st.markdown("## RAG Research App Coming Soon...")
    elif selected_app == "Analyzing Dashboards":
        st.markdown("## Dashboard Analyzer App Coming Soon...")

def show_app_list():
    st.markdown("""
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #4CAF50;
                color: white;
            }
            tr:hover {background-color: #f5f5f5;}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <table>
          <tr>
            <th>App Name</th>
            <th>Description</th>
          </tr>
          <tr>
            <td>Search Log Exceptions</td>
            <td>Search and analyze log exceptions</td>
          </tr>
          <tr>
            <td>RAG Research for Errors</td>
            <td>Research and analyze errors with RAG</td>
          </tr>
          <tr>
            <td>Analyzing Dashboards</td>
            <td>Analyze and optimize dashboard performance</td>
          </tr>
        </table>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()















# import nest_asyncio
# import streamlit as st

# # Apply necessary asyncio patches for Streamlit
# nest_asyncio.apply()

# # Configuration for the Streamlit web page
# st.set_page_config(
#     page_title="Log AI Analyzer",  # Set your desired page title
#     page_icon=":orange_heart:",  # Set your desired favicon using emoji or a URL to an image
# )

# # Inject custom CSS for sidebar color
# st.markdown(
#     """
#     <style>
#     /* Target the sidebar directly with its internal Streamlit structure */
#     div[data-testid="stSidebar"] {
#         background-color: #007BFF;  /* Your desired blue color */
#         color: #ffffff;  /* Ensuring text is white for better readability */
#     }
#     /* Adjust link colors in the sidebar */
#     div[data-testid="stSidebar"] a {
#         color: #ffffff;
#     }
#     /* Adjust button colors in the sidebar */
#     div[data-testid="stSidebar"] .stButton > button {
#         color: #ffffff;
#         background-color: #0056b3;  /* Darker blue for buttons */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Main title of the application
# st.title("Log AI Analyzer")  # Change the title as required

# # Main function to structure the page
# def main() -> None:
#     st.markdown("---")  # Separator for visual appeal
#     st.markdown("### Select an AI App from the sidebar:")  # Instruction or headline for the sidebar
#     # Descriptions for each app or function in the sidebar
#     st.markdown("#### 1. Searching Log Exceptions")  # Describe the first app
#     st.markdown("#### 2. RAG Research for Errors")  # Describe the second app
#     st.markdown("#### 3. Analyzing Dashboards")  # Describe the third app

#     # Sidebar interface for user selection
#     st.sidebar.success("Select App from above")  # Prompt or call to action in the sidebar

# # Execute the main function to run the app
# main()
