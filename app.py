# Personal Expense Tracker Dashboard
# Made by Ashish Kumar (toofan1p)

import streamlit as st
import pandas as pd
from datetime import date

st.title("💰 Personal Expense Tracker")

# File name to save data
FILE = "expenses.csv"

# Load previous data
try:
    data = pd.read_csv(FILE)
except FileNotFoundError:
    data = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])

# Input form
st.header("Add a new expense")
with st.form("entry_form"):
    col1, col2 = st.columns(2)
    with col1:
        exp_date = st.date_input("Date", date.today())
        category = st.selectbox("Category", ["Food", "Transport", "Bills", "Shopping", "Health", "Other"])
    with col2:
        amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)
        note = st.text_input("Note")
    submitted = st.form_submit_button("Add Expense")

if submitted:
    new = {"Date": exp_date, "Category": category, "Amount": amount, "Note": note}
    data = pd.concat([data, pd.DataFrame([new])], ignore_index=True)
    data.to_csv(FILE, index=False)
    st.success("✅ Expense added successfully!")

# Display expenses
st.header("📊 All Expenses")
st.dataframe(data)

# Analytics
if not data.empty:
    st.header("🔍 Analysis")
    total = data["Amount"].sum()
    st.metric("Total Spent", f"₹{total:.2f}")

    chart = data.groupby("Category")["Amount"].sum()
    st.bar_chart(chart)
