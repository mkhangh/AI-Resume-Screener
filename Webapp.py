import streamlit as st

# -----------------------------
# LOGIN CREDENTIALS
# -----------------------------

USERNAME = "admin"
PASSWORD = "Project@123"

# -----------------------------
# SESSION STATE
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# LOGIN PAGE
# -----------------------------

def login():

    st.title("🔐 Login Page")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):

        if user == USERNAME and pwd == PASSWORD:

            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Wrong credentials")

# -----------------------------
# MAIN APP
# -----------------------------

def app():

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Go To",
        ["Home", "Project PPT", "Logout"]
    )

    # HOME PAGE
    if page == "Home":

        st.title("📊 AI Resume Screener Project")

        st.write("""
        Welcome to my AI Resume Screener Project Web App.

        Project Overview:
        
        The AI-Powered Resume Screening System automates the recruitment process by analysing candidate resumes, evaluating skills and experience using AI, assigning scores, storing results in Google Sheets, and automatically sending emails to shortlisted candidates.

        Technologies Used:
        - n8n Cloud Automation
        - Gmail API
        - PDF Extraction
        - Groq AI
        - JavaScript
        - Google Sheets API
        - If Node 
        - Gmail Node
        - Streamlit
        """)

        st.success("Project Running Successfully")

    # PPT PAGE
    elif page == "Project PPT":

        st.header("📂 Project Presentation")

        st.write("Click below to download the project PPT.")

        with open("AI-Powered Resume Screener.pptx", "rb") as ppt:

            st.download_button(
                label="⬇ Download PPT",
                data=ppt,
                file_name="AI-Powered Resume Screener.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )

    
    # LOGOUT
    elif page == "Logout":

        st.session_state.logged_in = False
        st.rerun()

# -----------------------------
# APP START
# -----------------------------

if st.session_state.logged_in:
    app()
else:
    login()

    


