import pandas as pd

# Load the dataset
df_tcga_filtered = pd.read_csv("TCGA_LUAD_Filtered.csv", index_col=0)

# Convert `Entrez_Gene_Id` to string if needed, or drop it if unnecessary
df_tcga_filtered.index = df_tcga_filtered.index.astype(str)  # Ensure row names are strings

# Convert all columns to float64
df_tcga_filtered = df_tcga_filtered.astype(float)

# Save the cleaned version
df_tcga_filtered.to_csv("TCGA_LUAD_Filtered_Cleaned.csv")
print("✅ Data cleaned and saved as 'TCGA_LUAD_Filtered_Cleaned.csv' with all float64 values.")
