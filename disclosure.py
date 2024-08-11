import streamlit as st
import os
from datetime import datetime
from kpi_app import run_kpi_app  # Import the function from kpi_app.py

# Log file path
log_file = "user_log.txt"

# Function to log user information
def log_user_info(first_name, last_name, email, decision):
    with open(log_file, "a") as f:
        log_entry = f"{datetime.now()} - {first_name} {last_name}, {email}, Decision: {decision}\n"
        f.write(log_entry)

# Display the NDA on the main page
st.markdown("""
## Confidentiality Notice 

All information stated within this site is strictly confidential and is considered the intellectual property of Adonis M. Hautea. Unauthorized disclosure, copying, distribution, or use of any of the information contained herein is strictly prohibited and may result in legal action.

For more information, kindly contact:
- **Phone:** 09178085600
- **Email:** [donhautea@gmail.com](mailto:donhautea@gmail.com)
""")

# User information form
st.markdown("### Please provide your information to proceed:")
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
email = st.text_input("Email Address")

# Check if all fields are filled out
if first_name and last_name and email:
    st.success("Information provided. You can now proceed.")
    
    # Option buttons for agreeing or disagreeing to the NDA
    decision = st.radio("Please select your decision:", ("", "I agree to the Confidentiality Notice", "I disagree to the Confidentiality Notice"))

    # Logic for handling agree/disagree options
    if decision == "I agree to the Confidentiality Notice":
        st.sidebar.success("Thank you for agreeing to the Confidentiality Notice.")
        log_user_info(first_name, last_name, email, "Agreed")
        if st.sidebar.button("Load KPI App"):
            st.sidebar.write("Loading KPI App...")
            # Call the function from kpi_app.py to run the KPI app
            run_kpi_app()
    elif decision == "I disagree to the Confidentiality Notice":
        st.warning("You have disagreed with the Confidentiality Notice. Please close this page.")
        log_user_info(first_name, last_name, email, "Disagreed")
else:
    st.warning("Please provide your complete information to proceed.")
    st.sidebar.warning("Complete the information form to enable the options.")
