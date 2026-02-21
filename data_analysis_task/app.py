import streamlit as st
import pandas as pd

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(page_title="Employment Planning Dashboard", layout="wide")

st.title("📊 Employment Planning & Workforce Allocation Dashboard")
st.markdown("Interactive Workforce Analysis based on Demographic Factors")

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("census.csv")
    return df

df = load_data()

# ----------------------------------------------------
# Sidebar Filters
# ----------------------------------------------------
st.sidebar.header("🔎 Filter Options")

min_age = st.sidebar.slider("Select Minimum Age", 18, 60, 18)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

selected_education = st.sidebar.multiselect(
    "Select Education",
    df["Eduation"].unique(),
    default=df["Eduation"].unique()
)

# ----------------------------------------------------
# Apply Filters
# ----------------------------------------------------
df_filtered = df[
    (df["Age"] >= min_age) &
    (df["Gender"].isin(selected_gender)) &
    (df["Eduation"].isin(selected_education))
]

# ----------------------------------------------------
# Employment Classification
# ----------------------------------------------------
df_filtered["Employment_Status"] = df_filtered["Weeks_worked"].apply(
    lambda x: "Needs Employment Support" if x < 20 else "Employed"
)

# ----------------------------------------------------
# Dashboard Metrics
# ----------------------------------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total People", len(df_filtered))
col2.metric("Employed", len(df_filtered[df_filtered["Employment_Status"] == "Employed"]))
col3.metric("Needs Support", len(df_filtered[df_filtered["Employment_Status"] == "Needs Employment Support"]))

# ----------------------------------------------------
# Education Distribution
# ----------------------------------------------------
st.subheader("🎓 Education Distribution")
st.bar_chart(df_filtered["Eduation"].value_counts())

# ----------------------------------------------------
# Gender Distribution
# ----------------------------------------------------
st.subheader("👥 Gender Distribution")
st.bar_chart(df_filtered["Gender"].value_counts())

# ----------------------------------------------------
# Marital Status Distribution
# ----------------------------------------------------
st.subheader("💍 Marital Status Distribution")
st.bar_chart(df_filtered["Marital_Status"].value_counts())

# ----------------------------------------------------
# Income Analysis
# ----------------------------------------------------
st.subheader("💰 Average Income by Education")

income_by_education = (
    df_filtered.groupby("Eduation")["Income"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(income_by_education)

# ----------------------------------------------------
# Employment Crosstab
# ----------------------------------------------------
st.subheader("📊 Education vs Employment Status")

crosstab = pd.crosstab(
    df_filtered["Eduation"],
    df_filtered["Employment_Status"]
)

st.dataframe(crosstab)

# ----------------------------------------------------
# Data Preview
# ----------------------------------------------------
st.subheader("📄 Filtered Data Preview")
st.dataframe(df_filtered.head(50))