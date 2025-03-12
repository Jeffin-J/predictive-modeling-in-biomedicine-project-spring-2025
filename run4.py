import pandas as pd

# Load datasets
df_tcga = pd.read_csv("TCGA_LUAD_Raw.csv", index_col=0)
df_gtex = pd.read_csv("GTEx_Lung_HGNC.csv", index_col=0)

# Get the gene names
tcga_genes = set(df_tcga.index)
gtex_genes = set(df_gtex.index)

# Find overlaps
overlapping_genes = tcga_genes & gtex_genes

# Display results
print(f"✅ Total TCGA LUAD Genes: {len(tcga_genes)}")
print(f"✅ Total GTEx Lung Genes: {len(gtex_genes)}")
print(f"✅ Overlapping Genes: {len(overlapping_genes)}")

# Save overlapping gene list
with open("overlapping_genes.txt", "w") as f:
    f.write("\n".join(sorted(overlapping_genes)))

print("✅ Overlapping genes saved to 'overlapping_genes.txt'")

