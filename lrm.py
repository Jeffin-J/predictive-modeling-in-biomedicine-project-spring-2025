import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

# ✅ Load preprocessed dataset
df = pd.read_csv("preprocessed_LUAD_data.csv", index_col=0)

# ✅ Separate features (X) and labels (y)
X = df.drop(columns=["Cancer Type"])
y = df["Cancer Type"]

# ✅ Split dataset into train/test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ✅ Train logistic regression model
print("🔄 Training Logistic Regression model on selected genes...")
model = LogisticRegression(max_iter=1000, solver='lbfgs', class_weight='balanced')
model.fit(X_train, y_train)
print("✅ Model training complete!")

# ✅ Make predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# ✅ Evaluate model
accuracy = accuracy_score(y_test, y_pred)
auc_roc = roc_auc_score(y_test, y_prob)
report = classification_report(y_test, y_pred)

# ✅ Display results
print(f"✅ Model Accuracy: {accuracy:.4f}")
print(f"✅ ROC-AUC Score: {auc_roc:.4f}")
print("\n📊 Classification Report:\n", report)

# ✅ Cross-validation setup
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# ✅ Perform cross-validation using ROC-AUC
cv_roc_auc = cross_val_score(model, X, y, cv=cv, scoring="roc_auc")

# ✅ Perform cross-validation using Accuracy
cv_accuracy = cross_val_score(model, X, y, cv=cv, scoring="accuracy")

# ✅ Print cross-validation results
print(f"\n📌 Cross-Validated ROC-AUC Scores: {cv_roc_auc}")
print(f"📌 Mean ROC-AUC Score: {np.mean(cv_roc_auc):.4f} ± {np.std(cv_roc_auc):.4f}")

print(f"\n📌 Cross-Validated Accuracy Scores: {cv_accuracy}")
print(f"📌 Mean Accuracy Score: {np.mean(cv_accuracy):.4f} ± {np.std(cv_accuracy):.4f}")
