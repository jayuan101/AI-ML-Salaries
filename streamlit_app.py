import streamlit as st
import pandas as pd

# Load the CSV file
file_path = 'C:/Users/young/OneDrive/Desktop/salaries.csv'  # Use forward slashes
df = pd.read_csv(file_path)

# Streamlit app
def main():
    st.title("Salaries Data Dashboard")

    # Display the DataFrame
    st.write("## Data")
    st.write(df)

    # Filter by job title
    job_titles = df['job_title'].unique()
    selected_job_title = st.selectbox("Select Job Title", job_titles)
    filtered_df = df[df['job_title'] == selected_job_title]
    st.write(f"## Data for {selected_job_title}")
    st.write(filtered_df)

    # Display basic statistics
    st.write("## Summary Statistics")
    st.write(filtered_df.describe())

    # Display a line chart
    st.write("## Salary Distribution")
    st.line_chart(filtered_df['salary_in_usd'])

if __name__ == "__main__":
    main()
