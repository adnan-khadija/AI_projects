import streamlit as st
import joblib
import pandas as pd

# Load the trained model and TF-IDF vectorizer
model = joblib.load('logistic_regression_model.joblib')
tfidf = joblib.load('tfidf_vectorizer.joblib')


# Streamlit app title
st.title('Email Spam Detector')
st.write('Enter an email message below to check if it is spam or not.')

# Text input for user message
user_input = st.text_area('Enter your message here:', height=200)

# Prediction button
if st.button('Predict'):
    if user_input:
        # Vectorize the user input
        user_input_vec = tfidf.transform([user_input])
        
        # Make prediction
        prediction = model.predict(user_input_vec)
        
        # Display result
        if prediction[0] == 1:
            st.error('This is a SPAM message!')
        else:
            st.success('This is NOT a SPAM message.')
    else:
        st.warning('Please enter a message to predict.')



