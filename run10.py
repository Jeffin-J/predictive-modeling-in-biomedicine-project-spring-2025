import pandas as pd

# Load cleaned datasets
df_tcga = pd.read_csv("TCGA_LUAD_Zscored_Clean.csv", index_col=0)
df_gtex = pd.read_csv("GTEx_Lung_Zscored_Clean.csv", index_col=0)

# Find matching genes
matching_genes = df_tcga.index.intersection(df_gtex.index)

# Print verification details
print(f"✅ Matching genes between TCGA & GTEx: {len(matching_genes)}")
print(f"✅ Total TCGA Genes: {df_tcga.shape[0]}")
print(f"✅ Total GTEx Genes: {df_gtex.shape[0]}")

# Save matching gene list
matching_genes.to_series().to_csv("Matching_Genes_List.csv", index=False)

print("✅ Matching genes list saved as 'Matching_Genes_List.csv'")
