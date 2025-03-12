import pandas as pd

# Load the normalized GTEx dataset
df_gtex = pd.read_csv("GTEx_Lung_Zscored.csv", index_col=0)

# Count missing values per gene
missing_counts = df_gtex.isna().sum(axis=1)

# Find genes with missing values
genes_with_nans = missing_counts[missing_counts > 0]

print(f"🔍 GTEx Genes with Missing Values: {len(genes_with_nans)}")
print(genes_with_nans.sort_values(ascending=False).head(20))  # Show top 20 genes with missing data

# Save a report for reference
genes_with_nans.to_csv("GTEx_Missing_Values_Report.csv")
print("✅ Missing values report saved as 'GTEx_Missing_Values_Report.csv'")
