from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model & vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Spam Detection Function
def predict_spam(email):
    email_tfidf = vectorizer.transform([email])
    prediction = model.predict(email_tfidf)
    return "Spam" if prediction[0] == 1 else "Not Spam"

# API Endpoint for Prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    email_content = data.get("email", "")
    result = predict_spam(email_content)
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
