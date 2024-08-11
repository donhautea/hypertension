import streamlit as st
import pandas as pd

# Set the page layout to wide
st.set_page_config(layout="wide")

# Load the sample dataset
df = pd.read_csv('Hypertension_Sample_Data.csv')  # Replace with the correct path to your CSV file

# Convert the BP Reduction columns to numeric, just in case there are any non-numeric values
df['Systolic BP Reduction'] = pd.to_numeric(df['Systolic BP Reduction'], errors='coerce')
df['Diastolic BP Reduction'] = pd.to_numeric(df['Diastolic BP Reduction'], errors='coerce')

# Sidebar for filtering options
st.sidebar.header('Filter Options')
selected_sex = st.sidebar.multiselect('Select Sex', options=df['Sex'].unique(), default=df['Sex'].unique())
selected_comorbidities = st.sidebar.multiselect('Select Comorbidities', options=df['Comorbidities'].unique(), default=df['Comorbidities'].unique())
selected_medication = st.sidebar.multiselect('Select Medication', options=df['Medication'].unique(), default=df['Medication'].unique())

# Filtering data based on sidebar selections
filtered_df = df[
    (df['Sex'].isin(selected_sex)) &
    (df['Comorbidities'].isin(selected_comorbidities)) &
    (df['Medication'].isin(selected_medication))
]

# Create two columns
col1, col2 = st.columns(2)

with col1:
    # Display filtered data
    st.write('### Filtered Data', filtered_df)
    st.write("""
    **Explanation**: This table displays the data after applying the filters selected on the sidebar. It includes 
    patient demographics, baseline and follow-up blood pressure readings, and other related details.
    """)

with col2:
    # Display summary statistics
    st.write('### Summary Statistics')
    st.write(filtered_df.describe())
    st.write("""
    **Analysis**: The summary statistics provide an overview of the dataset, including measures such as mean, standard deviation,
    and quartiles for both the baseline and follow-up blood pressure readings. This helps in understanding the central tendencies
    and variability in the patient population.
    """)

# Create three columns for various analyses
col1, col2, col3 = st.columns(3)

with col1:
    # BP Reduction Analysis
    st.write('### BP Reduction Analysis')
    st.bar_chart(filtered_df[['Systolic BP Reduction', 'Diastolic BP Reduction']].mean())
    st.write("""
    **Analysis**: The chart above shows the average reduction in both systolic and diastolic blood pressure 
    after treatment. A higher reduction indicates better effectiveness of the treatment across the population.
    """)

with col2:
    # Patient Profile Distribution by Sex
    st.write('### Patient Profile Distribution')
    st.write('#### By Sex')
    st.bar_chart(filtered_df['Sex'].value_counts())
    st.write("""
    **Analysis**: This chart represents the distribution of patients based on their sex. Understanding the 
    demographic distribution is important for ensuring that the treatment is effective across different population groups.
    """)

with col3:
    # Patient Profile Distribution by Comorbidities
    st.write('#### By Comorbidities')
    st.bar_chart(filtered_df['Comorbidities'].value_counts())
    st.write("""
    **Analysis**: This chart shows the distribution of comorbidities among the patient population. Comorbid conditions 
    can significantly impact the treatment outcomes, so it is important to understand their prevalence.
    """)

# Create two columns for further analyses
col1, col2 = st.columns(2)

with col1:
    # Medication Effectiveness
    st.write('### Medication Effectiveness')
    med_effectiveness = filtered_df.groupby('Medication')[['Systolic BP Reduction', 'Diastolic BP Reduction']].mean()
    st.write(med_effectiveness)
    st.write("""
    **Analysis**: The table above provides the average systolic and diastolic BP reductions for each medication regimen.
    Comparing these values helps in identifying the most effective treatment option for lowering blood pressure.
    """)

with col2:
    # Diagnostic Accuracy
    st.write('### Diagnostic Accuracy')
    diagnostic_accuracy = filtered_df['Diagnosis'].value_counts(normalize=True) * 100
    st.write(diagnostic_accuracy)
    st.write("""
    **Analysis**: This section shows the percentage of patients diagnosed as newly hypertensive versus those 
    who are uncontrolled on other antihypertensive drugs. Understanding these proportions can help assess the 
    accuracy and appropriateness of the diagnostic criteria used in the study.
    """)
