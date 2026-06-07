import streamlit as st
import os
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
        
        ### Project Overview:

        The AI-Powered Resume Screening System automates the recruitment process by analysing candidate resumes, evaluating skills and experience using AI, assigning scores, storing results in Google Sheets, and automatically sending emails to shortlisted candidates.

        ---

        ### Goals:

        To develop an intelligent recruitment automation system that:
        - Automatically reads resumes. 
        - Extracts candidate information. 
        - Evaluates resumes using AI. 
        - Generates candidate scores. 
        - Shortlists qualified applicants. 
        - Sends automated email notifications. 
        - Stores all records for tracking and reporting.

        ---

        ### Project Architecture & Workflow:

        The workflow starts when resumes are received through Gmail. The PDF resumes are automatically extracted and processed to retrieve candidate information. The extracted data is analysed by Groq AI to evaluate skills, experience, and job suitability. JavaScript processes the AI response and generates a candidate score and recommendation. The results are stored in Google Sheets, and shortlisted candidates automatically receive email notifications based on predefined scoring criteria.

        ---

        ### Business Benefits:

        Faster Hiring :
        - Reduces screening time by up to 80%.

        Improved Efficiency :
        - Automates repetitive recruitment tasks.

        Better Candidate Experience :
        - Instant communication.

        Scalability :
        - Can process thousands of resumes.

        Data-Driven Decisions :
        - Consistent and objective evaluation.

        ---

        ### Technologies Used:

        - n8n Cloud Automation
        - Gmail API
        - PDF Extraction
        - Groq AI
        - JavaScript
        - Google Sheets API
        - If Node 
        - Gmail Node
        - Streamlit

        ---

        ### Conclusion:

        The AI-Powered Resume Screener demonstrates how artificial intelligence and workflow automation can transform traditional recruitment processes. By automating resume analysis and candidate evaluation, organizations can improve efficiency, reduce hiring time, and make more data-driven recruitment decisions.

        ---
        
        Achievements :

        - Automated Resume Processing
        - AI-Based Candidate Evaluation
        - Smart Shortlisting
        - Automated Communication
        - Centralized Candidate Database

        Outcome :

        Faster, smarter, and more efficient hiring process.

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

    st.markdown("---")
st.subheader("📑 Slide Preview")

slides_folder = "slides"

if os.path.exists(slides_folder):

    slides = sorted(os.listdir(slides_folder))

    st.write(f"Found {len(slides)} slides")

    for slide in slides:

        slide_path = os.path.join(slides_folder, slide)

        st.image(
            slide_path,
            caption=slide,
            use_container_width=True
        )

else:
    st.warning("Slides folder not found")

    
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

    


