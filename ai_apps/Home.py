import streamlit as st
import os

st.title("AI Tools Dashboard")
st.markdown("---")

st.markdown("### Available Applications")

if st.button("🧠 RAG Research App"):
    os.system("streamlit run ai_apps/Pages/2_RAG_Chat.py")

if st.button("📊 Dashboard Analyzer App"):
    os.system("streamlit run ai_apps/Pages/3_Dashboard_Analyzer.py")

if st.button("🔍 Search Log Exceptions App"):
    os.system("streamlit run ai_apps/Pages/1_Log_Exceptions.py")

st.markdown("---")
st.caption("Powered by Streamlit | Built with ❤️ by Pavan")
