import streamlit as st
import pandas as pd

# Streamlit app
def main():
    st.title("Salaries Data Dashboard")

    # Upload CSV file
    uploaded_file = st.file_uploader("salaries.csv", type="csv")
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

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
    else:
        st.write("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
