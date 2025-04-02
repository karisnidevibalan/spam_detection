# ✅ Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# ✅ Predict on test data
y_pred = model.predict(X_test_tfidf)

# ✅ Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.2f}")

# ✅ Print classification report
print(classification_report(y_test, y_pred))
