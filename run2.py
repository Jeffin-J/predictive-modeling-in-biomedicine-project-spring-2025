import pandas as pd

# Define file path
mapping_file = "ensembl_to_hugo.csv"

try:
    # Load the file with tab separator
    df_mapping = pd.read_csv(mapping_file, sep="\t")

    # Display first few rows
    print("🔍 First few rows of the mapping file:")
    print(df_mapping.head())

    # Rename columns to match expected names
    expected_columns = {
        "HGNC ID": "hgnc_id",
        "Approved symbol": "hgnc_symbol",
        "Ensembl ID(supplied by Ensembl)": "ensembl_gene_id"
    }
    df_mapping.rename(columns=expected_columns, inplace=True)

    # Check for expected columns
    required_columns = {"ensembl_gene_id", "hgnc_symbol"}
    actual_columns = set(df_mapping.columns)

    if not required_columns.issubset(actual_columns):
        print(f"❌ Error: Missing expected columns. Found: {actual_columns}")
    else:
        print("✅ Mapping file has correct columns!")

    # Drop rows where either gene name or Ensembl ID is missing
    df_mapping = df_mapping.dropna(subset=["ensembl_gene_id", "hgnc_symbol"])

    # Save the cleaned file for future use
    df_mapping.to_csv("cleaned_ensembl_to_hugo.csv", index=False)

    print(f"✅ Total valid gene mappings: {df_mapping.shape[0]}")
    print("✅ Cleaned mapping file saved as 'cleaned_ensembl_to_hugo.csv'!")

except FileNotFoundError:
    print("❌ Error: 'ensembl_to_hugo.csv' file not found!")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
