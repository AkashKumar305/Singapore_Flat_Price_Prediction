# Singapore Flat Resale Price Prediction

## Project Overview

Welcome to the Singapore Flat Resale Price Prediction project! This project focuses on predicting the resale price of flats in Singapore using machine learning techniques. The dataset used is sourced from the Singapore Housing and Development Board (HDB) and has undergone extensive data preprocessing, exploratory data analysis (EDA), and feature engineering. The resulting clean dataset is employed to build a regression model, which is then deployed for predictions.

## Project Workflow

### 1. Data Preprocessing
- The initial step involves preparing the dataset for analysis.
- Handling Null values, Feature Engineering, EDA, Outlier Detection, Encoding, Feature Selection steps are performed.
- Refer to the `Data Preprocessing.ipynb` notebook for details on how the dataset was cleaned and processed.

### 2. Model Building
- The `Model Building.ipynb` notebook outlines the process of creating and training the regression model.
- Elastic Net, Random Forest, Decision Tree, Gradient Boosting, LightGBM, XGBoost Regressor were used and compared to select the best performing model.

### 3. Main Application (`main.py`)
- The main application (`main.py`) utilizes the Streamlit framework to create a user-friendly interface.
- Users can input specific property details, and the deployed regression model predicts the resale price.
- The main application integrates the trained model, and user interaction.

### 4. Dataset
- The cleaned dataset used for training and predictions is stored in `Singapore_Flat_Cleaned.csv`.

### 5. Trained Model
- The trained regression model is saved as `regression_model.joblib`.
- This file is essential for loading the model in the main application.

### 6. Requirements
- The `requirements.txt` file lists all the necessary libraries and dependencies required to run the project successfully.

## Running the Application

1. Install the required libraries by running: `pip install -r requirements.txt`.
2. Execute the main application using: `streamlit run main.py`.
3. The app is also hosted on Render platform as a web application: 
The web application may take 30 to 40 seconds to load due to being on a Free plan https://singapore-flat-price-prediction.onrender.com.

## LinkedIn Profile
Link: www.linkedin.com/in/akashkumarl
Visit the link to see the project video

## File Structure
- `Data Preprocessing.ipynb`: Notebook containing the data preprocessing steps.
- `Model Building.ipynb`: Notebook detailing the regression model creation and training.
- `Singapore_Flat_Cleaned.csv`: Cleaned dataset for resale flat prices.
- `main.py`: Main application file utilizing Streamlit for user interaction.
- `regression_model.joblib`: Saved regression model for resale price prediction.
- `requirements.txt`: List of dependencies required to run the project.
- `Project Report.pdf`: PDF containing the Project Report.

Feel free to explore the notebooks and application code to understand the project in depth. If you have any questions or feedback, please don't hesitate to reach out.

Happy predicting! 🏡💰
