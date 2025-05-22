import streamlit as st
from db.firebase_app import login
from dotenv import load_dotenv
import os
from streamlit_extras.switch_page_button import switch_page
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces

# Initial setup
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

# Load environment variables
load_dotenv()

# Initialize session state for profile
if "profile" not in st.session_state:
    st.session_state.profile = None  # Set default to None or "Verifier"/"Institute"

# Login form
with st.form("login"):
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")
    submit = st.form_submit_button("Login")

# Register button (only for non-Institute profiles)
if st.session_state.profile != "Institute":
    clicked_register = st.button("New user? Click here to register!")
    if clicked_register:
        switch_page("register")

# Login logic
if submit:
    if st.session_state.profile == "Institute":
        valid_email = os.getenv("institute_email")
        valid_pass = os.getenv("institute_password")
        if email == valid_email and password == valid_pass:
            st.success("Login successful!")
            switch_page("institute")
        else:
            st.error("Invalid credentials!")
    else:
        result = login(email, password)
        if result == "success":
            st.success("Login successful!")
            switch_page("verifier")
        else:
            st.error("Invalid credentials!")