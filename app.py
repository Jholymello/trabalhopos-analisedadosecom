import streamlit as st
import pandas as pd
import requests
from data_loader import DataLoader
from data_analysis import DataAnalysis  # Importe a classe DataAnalysis

st.title("E-commerce Data Analysis")

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    st.write("File uploaded. Processing...")
    # Use DataLoader to load and process the file
    data_loader = DataLoader(uploaded_file)
    data = data_loader.load_data()
    st.write("Data preview:")
    st.write(data.head())

    # Initialize DataAnalysis and display graphs
    analysis = DataAnalysis(data)

    if st.button("Show Monthly Spending Graph"):
        fig = analysis.monthly_spending()
        st.pyplot(fig)

    if st.button("Show Demographic Analysis"):
        fig = analysis.demographic_analysis()
        st.pyplot(fig)

    if st.button("Show Ticket Average Distribution"):
        fig = analysis.ticket_average()
        st.pyplot(fig)