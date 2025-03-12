import pandas as pd

# Load cleaned datasets
df_tcga = pd.read_csv("TCGA_LUAD_Zscored_Clean.csv", index_col=0)
df_gtex = pd.read_csv("GTEx_Lung_Zscored_Clean.csv", index_col=0)

# Load matching genes list, ensuring it's read correctly
matching_genes = pd.read_csv("Matching_Genes_List.csv", header=None, names=["Gene"])
matching_genes = matching_genes["Gene"].astype(str)  # Ensure it's a string list

# Check if matching genes exist in datasets
matching_genes_tcga = df_tcga.index.intersection(matching_genes)
matching_genes_gtex = df_gtex.index.intersection(matching_genes)

# Keep only matching genes
df_tcga = df_tcga.loc[matching_genes_tcga]
df_gtex = df_gtex.loc[matching_genes_gtex]

# Add cancer labels (1 = LUAD, 0 = Normal)
df_tcga["Cancer Type"] = 1
df_gtex["Cancer Type"] = 0

# Merge both datasets
df_merged = pd.concat([df_tcga, df_gtex])

# Save merged dataset
df_merged.to_csv("Final_Merged_RNAseq.csv")

# Print final shape
print(f"✅ Merged dataset saved as 'Final_Merged_RNAseq.csv'")
print(f"✅ Final dataset shape: {df_merged.shape}")
print(f"✅ LUAD Samples: {df_tcga.shape[1] - 1}, GTEx Normal Samples: {df_gtex.shape[1] - 1}")
