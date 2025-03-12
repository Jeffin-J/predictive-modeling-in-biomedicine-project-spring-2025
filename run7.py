import pandas as pd
from scipy.stats import zscore

# Load filtered data
df_tcga_filtered = pd.read_csv("TCGA_LUAD_Filtered_Cleaned.csv", index_col=0)
df_gtex_filtered = pd.read_csv("GTEx_Lung_Filtered.csv", index_col=0)

# ✅ **Ensure Gene Names are the Index**
if df_gtex_filtered.iloc[:, 0].dtype == 'object':
    print("🚨 Warning: GTEx data still contains non-numeric values. Attempting to fix...")
    df_gtex_filtered.set_index(df_gtex_filtered.columns[0], inplace=True)

# ✅ **Convert all values to float**
df_tcga_filtered = df_tcga_filtered.astype(float)
df_gtex_filtered = df_gtex_filtered.astype(float)  # 🔥 Fix: Convert GTEx integers to float

# ✅ **Apply Z-score normalization**
df_tcga_zscore = df_tcga_filtered.apply(zscore, axis=1)
df_gtex_zscore = df_gtex_filtered.apply(zscore, axis=1)

# ✅ **Save normalized data**
df_tcga_zscore.to_csv("TCGA_LUAD_Zscored.csv")
df_gtex_zscore.to_csv("GTEx_Lung_Zscored.csv")

# ✅ **Confirm successful processing**
print(f"✅ Normalized TCGA Data Shape: {df_tcga_zscore.shape}")
print(f"✅ Normalized GTEx Data Shape: {df_gtex_zscore.shape}")
print("✅ Normalized datasets saved as 'TCGA_LUAD_Zscored.csv' and 'GTEx_Lung_Zscored.csv'")
