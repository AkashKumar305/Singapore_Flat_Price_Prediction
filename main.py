# Importing necessary libraries
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import joblib

# Function to display project information
def display_project_info():

    st.title('Singapore Resale Flat Price Prediction')
    st.subheader('Technologies used:')
    streamlit_list = "1. Streamlit\n2. Pandas\n3. Data Wrangling\n4. Machine Learning\n5. EDA"
    st.write(streamlit_list)
    st.subheader('Domain:')
    st.write('Real Estate')
    st.subheader('About:')
    st.write('''This project aims to analyze a dataset from the Singapore Housing and Development Board (HDB). 
             The dataset has undergone feature engineering, EDA analysis, and data wrangling steps. 
             Finally, the cleaned dataset is utilized for building a regression model to predict the resale price for each property. 
             The model is then deployed.''')
    
# Function to create input columns
def create_input_columns(column, input_labels):

    with column:
        st.subheader('Enter the Values:')
        inputs = [st.text_input(label, 0) for label in input_labels]
    return inputs

# Function to predict results using the loaded model
def predict_results(loaded_model, input_data):

    try:
        results = loaded_model.predict([input_data])
        st.success(f'Predicted Result: {results[0]}')
    except Exception as e:
        st.error(f'Error predicting: {e}')

# Function to run regression model  
def run_regression(df, loaded_model):

    st.dataframe(df)
    col1,col2,col3,col4 = st.columns(4)

    input_labels = [
        'flat_type', 'block_0', 'block_1', 'block_2', 'street_name_0',
        'street_name_1', 'floor_area_sqm', 'flat_model', 'lease_commence_date',
        'year', 'start_storey_range', 'end_storey_range','town_PUNGGOL', 'town_SENGKANG'
    ]

    inputs = create_input_columns(col1, input_labels)

    if st.button('Submit'):
        input_data = [value for value in inputs]
        predict_results(loaded_model, input_data)

# Main function
def main():
    # Load the data from CSV file
    df = pd.read_csv(r'Singapore_Flat_Cleaned.csv')

    # Load the Models
    loaded_regression_model = joblib.load('regression_model.joblib')

    # Sidebar menu options
    with st.sidebar:
        options = option_menu('Menu',['Home','ML Prediction'])

    if options == 'Home':
        display_project_info()

    if options == 'ML Prediction':
        st.subheader('Table:')
        run_regression(df, loaded_regression_model)

# Call the main function
if __name__ == '__main__':
    main()