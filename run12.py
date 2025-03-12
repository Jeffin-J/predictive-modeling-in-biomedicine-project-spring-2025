import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ✅ Load dataset
df = pd.read_csv("Final_Merged_RNAseq.csv", index_col=0)

# ✅ Identify TCGA and GTEx samples
tcga_samples = [col for col in df.columns if "TCGA" in col]
gtex_samples = [col for col in df.columns if "GTEX" in col]

# 🚨 Fix Negative & NaN Values BEFORE Log2
df[df < 0] = 0  # Replace negative values with 0
df.fillna(0, inplace=True)  # Fill NaNs with 0 (or use df.fillna(df.median()) for median replacement)

# ✅ Apply log2 transformation
df_log2 = np.log2(df + 1)  # Adding 1 prevents log(0) issues

# ✅ Normalize TCGA & GTEx separately using Z-score
scaler_tcga = StandardScaler()
scaler_gtex = StandardScaler()

df_log2[tcga_samples] = scaler_tcga.fit_transform(df_log2[tcga_samples])
df_log2[gtex_samples] = scaler_gtex.fit_transform(df_log2[gtex_samples])

# ✅ Save the correctly normalized dataset
df_log2.to_csv("Final_Merged_RNAseq_Log2_Zscored.csv")
print("✅ Log2 + Z-score normalization applied and saved!")
