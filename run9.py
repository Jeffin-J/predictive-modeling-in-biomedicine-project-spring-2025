import pandas as pd

# Load datasets
df_tcga = pd.read_csv("TCGA_LUAD_Zscored.csv", index_col=0)
df_gtex = pd.read_csv("GTEx_Lung_Zscored.csv", index_col=0)

# Load the missing genes report
missing_genes = pd.read_csv("GTEx_Missing_Values_Report.csv", index_col=0)

# Remove missing genes from both datasets
df_tcga_cleaned = df_tcga.drop(index=missing_genes.index, errors='ignore')
df_gtex_cleaned = df_gtex.drop(index=missing_genes.index, errors='ignore')

# Save the cleaned datasets
df_tcga_cleaned.to_csv("TCGA_LUAD_Zscored_Clean.csv")
df_gtex_cleaned.to_csv("GTEx_Lung_Zscored_Clean.csv")

print(f"✅ Removed {len(missing_genes)} genes with missing values.")
print(f"✅ Cleaned TCGA Data Shape: {df_tcga_cleaned.shape}")
print(f"✅ Cleaned GTEx Data Shape: {df_gtex_cleaned.shape}")
print("✅ Datasets saved as 'TCGA_LUAD_Zscored_Clean.csv' and 'GTEx_Lung_Zscored_Clean.csv'")
