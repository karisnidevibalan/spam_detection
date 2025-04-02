import streamlit as st
import joblib
import numpy as np
import os
import streamlit as st
# Load model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Streamlit UI
st.title("📧 Spam Email Detector")
st.write("Paste an email below to check if it's spam or not:")

email_input = st.text_area("Email Text")

if st.button("Check"):
    if email_input:
        # Transform text into features
        X = vectorizer.transform([email_input])
        prediction = model.predict(X)
        
        if prediction[0] == 1:
            st.error("🚨 This is SPAM!")
        else:
            st.success("✅ This is NOT spam.")
    else:
        st.warning("Please enter some text!")
    try:
        import joblib
    except ModuleNotFoundError:
        os.system("pip install joblib")
        import joblib  # Import again after installation