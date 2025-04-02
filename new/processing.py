import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# ✅ Load data
file_path = r"C:\xampphtdocs\htdocs\23CSR101\hackbuzz\dataset\spam.csv"
df = pd.read_csv(file_path, encoding="latin1")

# ✅ Fix column names
df.columns = df.columns.str.strip()

# ✅ Convert 'Category' column to binary labels
df['Category'] = df['Category'].map({'ham': 0, 'spam': 1})

# ✅ Clean the text data
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

df['Message'] = df['Message'].apply(clean_text)

# ✅ Split data into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(df['Message'], df['Category'], test_size=0.2, random_state=42)

# ✅ Convert text to numerical format using TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("✅ Data preprocessing complete!")
