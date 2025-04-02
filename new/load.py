import pandas as pd
import os

# ✅ Correct file path
file_path = r"C:\xampphtdocs\htdocs\23CSR101\hackbuzz\dataset\spam.csv"

# ✅ Check if file exists
if not os.path.exists(file_path):
    print("❌ Error: File not found! Check the path:", file_path)
    exit()

# ✅ Read CSV with encoding handling
try:
    df = pd.read_csv(file_path, encoding="latin1")  # Change encoding if needed
except Exception as e:
    print(f"❌ Error reading CSV file: {e}")
    exit()

# ✅ Print column names to debug
print("CSV Columns:", df.columns)

# ✅ Strip spaces from column names
df.columns = df.columns.str.strip()

# ✅ Use the correct column names
X = df["Message"]  # Text column (was 'message', now corrected to 'Message')
y = df["Category"]  # Spam/Ham labels

print("✅ Data loaded successfully!")
print(df.head())  # Print first few rows to confirm
