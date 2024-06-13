!pip install scikit-learn

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, accuracy_score

# Load the CSV file
file_path = 'salaries.csv'  # Use forward slashes
df = pd.read_csv("salaries.csv")

# Check if necessary columns exist
required_columns = ['experience_level', 'employment_type', 'job_title', 'salary_currency', 'employee_residence', 'company_location', 'company_size', 'salary_in_usd']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    st.error(f"Missing columns in the CSV file: {', '.join(missing_columns)}")
else:
    # Preprocess the data
    df = df.dropna()  # Drop missing values
    df = pd.get_dummies(df, columns=['experience_level', 'employment_type', 'job_title', 'salary_currency', 'employee_residence', 'company_location', 'company_size'])

    # Streamlit app
    def main():
        st.title("Salaries Data Dashboard")

        # Sidebar menu
        menu = ["Overview", "Job Titles", "Statistics", "Salary Distribution", "Machine Learning"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Overview":
            st.subheader("Overview")
            st.write(df)
        
        elif choice == "Job Titles":
            st.subheader("Filter by Job Title")
            job_titles = df.columns[df.columns.str.startswith('job_title_')].str.replace('job_title_', '')
            selected_job_title = st.selectbox("Select Job Title", job_titles)
            filtered_df = df[df[f'job_title_{selected_job_title}'] == 1]
            st.write(f"## Data for {selected_job_title}")
            st.write(filtered_df)
        
        elif choice == "Statistics":
            st.subheader("Summary Statistics")
            st.write(df.describe())
        
        elif choice == "Salary Distribution":
            st.subheader("Salary Distribution")
            st.line_chart(df['salary_in_usd'])
        
        elif choice == "Machine Learning":
            st.subheader("Machine Learning Techniques")
            
            # Split data into features and target
            X = df.drop('salary_in_usd', axis=1)
            y = df['salary_in_usd']

            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Sidebar options for machine learning techniques
            ml_technique = st.sidebar.selectbox("Select ML Technique", ["Linear Regression", "Decision Tree"])

            if ml_technique == "Linear Regression":
                model = LinearRegression()
                model.fit(X_train, y_train)
                predictions = model.predict(X_test)
                mse = mean_squared_error(y_test, predictions)
                st.write(f"Mean Squared Error: {mse}")
                st.write("Predictions vs Actuals")
                st.write(pd.DataFrame({"Actual": y_test, "Predicted": predictions}))
            
            elif ml_technique == "Decision Tree":
                model = DecisionTreeRegressor()
                model.fit(X_train, y_train)
                predictions = model.predict(X_test)
                mse = mean_squared_error(y_test, predictions)
                st.write(f"Mean Squared Error: {mse}")
                st.write("Predictions vs Actuals")
                st.write(pd.DataFrame({"Actual": y_test, "Predicted": predictions}))

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
