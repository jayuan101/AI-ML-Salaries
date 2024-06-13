{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f68bc905-a29e-4f19-af5b-a45c0963361f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Load the CSV file\n",
    "file_path = 'salaries.csv'\n",
    "df = pd.read_csv(file_path)\n",
    "\n",
    "# Streamlit app\n",
    "def main():\n",
    "    st.title(\"Salaries Data Dashboard\")\n",
    "\n",
    "    # Display the DataFrame\n",
    "    st.write(\"Different Salaries\")\n",
    "    st.write(df)\n",
    "\n",
    "    # Filter by job title\n",
    "    job_titles = df['job_title'].unique()\n",
    "    selected_job_title = st.selectbox(\"Select Job Title\", job_titles)\n",
    "    filtered_df = df[df['job_title'] == selected_job_title]\n",
    "    st.write(f\"## Data for {selected_job_title}\")\n",
    "    st.write(filtered_df)\n",
    "\n",
    "    # Display basic statistics\n",
    "    st.write(\"## Summary Statistics\")\n",
    "    st.write(filtered_df.describe())\n",
    "\n",
    "    # Display a line chart\n",
    "    st.write(\"## Salary Distribution\")\n",
    "    st.line_chart(filtered_df['salary_in_usd'])\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
