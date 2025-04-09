import streamlit as st
import pandas as pd
import numpy as np
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.title('Wine Quality Prediction')

st.sidebar.header('Input Parameters')

def user_input_features():
    fixed_acidity = st.sidebar.slider('Fixed Acidity', 4.0, 16.0, 8.0)
    volatile_acidity = st.sidebar.slider('Volatile Acidity', 0.1, 1.6, 0.5)
    citric_acid = st.sidebar.slider('Citric Acid', 0.0, 1.0, 0.3)
    residual_sugar = st.sidebar.slider('Residual Sugar', 0.9, 15.5, 2.5)
    chlorides = st.sidebar.slider('Chlorides', 0.01, 0.6, 0.08)
    free_sulfur_dioxide = st.sidebar.slider('Free Sulfur Dioxide', 1, 72, 30)
    total_sulfur_dioxide = st.sidebar.slider('Total Sulfur Dioxide', 6, 289, 100)
    density = st.sidebar.slider('Density', 0.99, 1.004, 0.996)
    pH = st.sidebar.slider('pH', 2.74, 4.01, 3.2)
    sulphates = st.sidebar.slider('Sulphates', 0.33, 2.0, 0.65)
    alcohol = st.sidebar.slider('Alcohol', 8.4, 14.9, 10.4)
    
    data = CustomData(
        fixed_acidity=fixed_acidity,
        volatile_acidity=volatile_acidity,
        citric_acid=citric_acid,
        residual_sugar=residual_sugar,
        chlorides=chlorides,
        free_sulfur_dioxide=free_sulfur_dioxide,
        total_sulfur_dioxide=total_sulfur_dioxide,
        density=density,
        pH=pH,
        sulphates=sulphates,
        alcohol=alcohol
    )
    
    return data

data = user_input_features()

st.subheader('User Input parameters')
df = data.get_data_as_dataframe()
st.write(df)

if st.button("Predict"):
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(df)
    
    st.subheader('Prediction')
    st.write(f'The predicted wine quality is: {results[0]}')
    
    # Add quality scale explanation
    st.info("""
    Wine Quality Scale:
    - 3-4: Below Average
    - 5-6: Average
    - 7-8: Above Average
    - 9: Excellent
    """)