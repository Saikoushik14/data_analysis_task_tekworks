# data_analysis_task_tekworks
### 📊 Employment Planning & Workforce Allocation System
## Project Overview
This project analyzes working-age population data to identify underemployment and provide employment allocation strategies based on demographic factors.

The system consists of:

1️⃣ Pandas Analysis (Jupyter Notebook) – Data exploration and analysis
2️⃣ Streamlit Dashboard (app.py) – Interactive workforce planning application

## Objective
Identify working-age population (Age ≥ 18)

Analyze education distribution

Detect underemployment (low weeks worked)

Study income trends by education

Provide employment classification

Build an interactive dashboard for decision-making

### Project Structure
Employment-Planning-Project/
│
├── census.csv
├── analysis.ipynb
├── app.py
└── README.md

### Pandas Analysis (Jupyter Notebook)
employment_report.ipynb
# What It Does:

Loads census dataset

Filters working-age population

Performs:

Education distribution analysis

Gender distribution analysis

Marital status analysis

Parents status analysis

Weeks worked analysis

Classifies employment status:

Weeks_worked < 20 → Needs Employment Support

Weeks_worked ≥ 20 → Employed

Calculates average income by education

Generates cross-tab reports

### Technologies Used:

 Python

 Pandas

 Jupyter Notebook
 Streamlit Interactive Dashboard
 app.py
### Features:

✔ Age filter
✔ Gender filter
✔ Education filter
✔ Real-time employment classification
✔ Income analysis
✔ Education vs Employment comparison
✔ Interactive charts
✔ Data preview table

### Business Use Case:

Helps identify underemployed individuals

Supports workforce planning

Assists in policy decision-making

Provides real-time demographic insights

### Dataset Information:
Total Records: 2000

Working Age Population (18+): 1465

### Key Columns Used:

Age

Eduation

Gender

Marital_Status

Parents_Status

Weeks_worked

Income

### Employment Classification:
If Weeks_worked < 20:
    Employment_Status = "Needs Employment Support"
Else:
    Employment_Status = "Employed"


### Key Insights
Majority population are High School graduates

Higher education correlates with higher income

Underemployment exists in low weeks-worked group

Balanced gender distribution supports inclusive employment policies


# K Sai Koushik
# Employment Planning & Data Analysis Project
