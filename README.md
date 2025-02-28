# predictive-modeling-in-biomedicine-paper-spring-2025
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the final paired dataset
df = pd.read_csv("final_paired_rnaseq_data.csv")

# Inspect dataset
print("Dataset Preview:")
print(df.head())

# Drop the Unnamed index column if it exists
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Convert categorical labels into numerical values
label_encoder = LabelEncoder()
df["Cancer Type"] = label_encoder.fit_transform(df["Cancer Type"])  # Encode: 0 = Normal, 1 = Lung Cancer

# Define features (X) and labels (y)
X = df[["TP53", "EGFR"]].values  # Extract TP53 and EGFR expression levels
y = df["Cancer Type"].values  # Labels (cancer/normal)

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f" Model Accuracy: {accuracy:.4f}")

# Define class names manually
class_names = ["Normal", "Lung Cancer"]  # Ensure correct labels

# Print classification report
print(" Classification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))
