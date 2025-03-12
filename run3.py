import pandas as pd

# File paths
gtex_file = "GTEx_Lung_Raw.csv"  # Your raw GTEx data
mapping_file = "cleaned_ensembl_to_hugo.csv"

# Load GTEx dataset
df_gtex = pd.read_csv(gtex_file, index_col=0)

# Load gene mapping
df_mapping = pd.read_csv(mapping_file)

# Ensure correct column names
df_mapping = df_mapping[["ensembl_gene_id", "hgnc_symbol"]].dropna()

# Remove Ensembl version numbers (e.g., ENSG00000123456.5 → ENSG00000123456)
df_mapping["ensembl_gene_id"] = df_mapping["ensembl_gene_id"].str.split(".").str[0]

# Remove versions from GTEx index
df_gtex.index = df_gtex.index.str.split(".").str[0]

# Merge GTEx dataset with the mapping file
df_gtex = df_gtex.merge(df_mapping, left_index=True, right_on="ensembl_gene_id", how="left")

# Drop genes that couldn’t be mapped
df_gtex.dropna(subset=["hgnc_symbol"], inplace=True)

# Set HGNC symbols as index
df_gtex.set_index("hgnc_symbol", inplace=True)

# Drop unnecessary columns
df_gtex.drop(columns=["ensembl_gene_id"], inplace=True)

# Save converted GTEx data
df_gtex.to_csv("GTEx_Lung_HGNC.csv")

print("✅ GTEx Ensembl IDs successfully converted to HGNC symbols!")
print(f"✅ Final GTEx Data Shape: {df_gtex.shape}")
print(df_gtex.head())

