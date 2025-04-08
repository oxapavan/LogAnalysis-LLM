import streamlit as st
from PIL import Image

# Optional Background Image (if you want)
def set_background():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://picsum.photos/1200/800");
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

# Call background function (optional)
# set_background()

# Main Title
st.title("AI Tools Dashboard")

st.markdown("---")

st.markdown("### Available Applications")

# Navigation Links
st.page_link("ai_apps/Pages/2_RAG_Chat.py", label="🧠 RAG Research App")

st.page_link("ai_apps/Pages/3_Dashboard_Analyzer.py", label="📊 Dashboard Analyzer App")

st.page_link("ai_apps/Pages/1_Log_Exceptions.py", label="🔍 Search Log Exceptions App")

st.markdown("---")

st.caption("Powered by Streamlit | Built with ❤️ by Pavan")

