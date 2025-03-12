import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler

# ✅ Load dataset and set gene names as columns
df = pd.read_csv("Final_Merged_RNAseq_Log2_Zscored.csv", index_col=0)

# ✅ Fix the structure: Move gene names from rows to columns
df = df.T  # Transpose so genes become columns and samples become rows

# ✅ Identify TCGA (cancer) and GTEx (normal) samples
tcga_samples = [col for col in df.index if "TCGA" in col]
gtex_samples = [col for col in df.index if "GTEX" in col]

# ✅ Add the "Cancer Type" column manually
df["Cancer Type"] = df.index.map(lambda x: 1 if "TCGA" in x else 0)

# ✅ Check if gene names exist now
print("Columns after transposition:", df.columns[:10])  # Print first 10 column names

# ✅ Select relevant genes for LUAD classification
genes_of_interest = ["TP53", "EGFR", "KRAS", "BRAF", "ALK", "MET"]
available_genes = [gene for gene in genes_of_interest if gene in df.columns]

if not available_genes:
    raise ValueError("None of the selected genes are found in the dataset!")

df_filtered = df.loc[:, available_genes + ["Cancer Type"]]  # Ensure "Cancer Type" column is present

# ✅ Separate features (X) and labels (y)
X = df_filtered.drop(columns=["Cancer Type"])
y = df_filtered["Cancer Type"]

# ✅ Standardize gene expression values
scaler = StandardScaler()
X = scaler.fit_transform(X)

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

# ✅ Print feature importance
print("\n🔍 Feature Importance (Logistic Regression Coefficients):")
for gene, coef in zip(available_genes, model.coef_[0]):
    print(f"{gene}: {coef:.4f}")
