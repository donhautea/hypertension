import streamlit as st
import os
from datetime import datetime

# Log file path
log_file = "user_log.txt"

# Function to log user information
def log_user_info(first_name, last_name, email, decision):
    with open(log_file, "a") as f:
        log_entry = f"{datetime.now()} - {first_name} {last_name}, {email}, Decision: {decision}\n"
        f.write(log_entry)

# Display the NDA on the main page
st.title("Non-Disclosure Agreement (NDA)")

st.markdown("""
## Non-Disclosure Agreement (NDA)

All information stated within this site is strictly confidential and is considered the intellectual property of Adonis M. Hautea, Data Scientist, and System Developer. Unauthorized disclosure, copying, distribution, or use of any of the information contained herein is strictly prohibited and may result in legal action.

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
    decision = st.radio("Please select your decision:", ("", "I agree to the Non-Disclosure Agreement (NDA)", "I disagree to the Non-Disclosure Agreement (NDA)"))

    # Logic for handling agree/disagree options
    if decision == "I agree to the Non-Disclosure Agreement (NDA)":
        st.sidebar.success("Thank you for agreeing to the NDA.")
        log_user_info(first_name, last_name, email, "Agreed")
        if st.sidebar.button("Load KPI App"):
            st.sidebar.write("Loading KPI App...")
            # Load the KPI app (assuming `kpi_app.py` is located in the same directory)
            os.system('streamlit run kpi_app.py')
    elif decision == "I disagree to the Non-Disclosure Agreement (NDA)":
        st.warning("You have disagreed with the NDA. Please close this page.")
        log_user_info(first_name, last_name, email, "Disagreed")
else:
    st.warning("Please provide your complete information to proceed.")
    st.sidebar.warning("Complete the information form to enable the options.")
