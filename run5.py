import pandas as pd

# Load datasets
df_tcga = pd.read_csv("TCGA_LUAD_Raw.csv", index_col=0)
df_gtex = pd.read_csv("GTEx_Lung_HGNC.csv", index_col=0)

# Load overlapping genes
with open("overlapping_genes.txt") as f:
    overlapping_genes = set(f.read().splitlines())

# Filter datasets
df_tcga_filtered = df_tcga.loc[df_tcga.index.intersection(overlapping_genes)]
df_gtex_filtered = df_gtex.loc[df_gtex.index.intersection(overlapping_genes)]

# Save filtered datasets
df_tcga_filtered.to_csv("TCGA_LUAD_Filtered.csv")
df_gtex_filtered.to_csv("GTEx_Lung_Filtered.csv")

print(f"✅ Filtered TCGA Data Shape: {df_tcga_filtered.shape}")
print(f"✅ Filtered GTEx Data Shape: {df_gtex_filtered.shape}")
print("✅ Filtered datasets saved as 'TCGA_LUAD_Filtered.csv' and 'GTEx_Lung_Filtered.csv'")
