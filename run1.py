import tarfile
import gzip
import pandas as pd

# File paths
tcga_tar = "positive.tar.gz"
gtex_gct = "negative.gct.gz"

# TCGA RNA-seq file inside the tar archive (update if needed)
tcga_rna_file = "luad_tcga_pan_can_atlas_2018/data_mrna_seq_v2_rsem.txt"  

# GTEx RNA-seq file inside the GCT archive
gtex_rna_file = "negative.gct.gz"  # The GCT file itself contains the data

### 🔄 Extract TCGA LUAD RNA-seq ###
print("🔄 Extracting TCGA LUAD RNA-seq data...")
with tarfile.open(tcga_tar, "r:gz") as tar:
    extracted_file = tar.extractfile(tcga_rna_file)
    if extracted_file:
        df_tcga = pd.read_csv(extracted_file, sep="\t", index_col=0)
        df_tcga.to_csv("TCGA_LUAD_Raw.csv")
        print("✅ TCGA LUAD RNA-seq extracted & saved as 'TCGA_LUAD_Raw.csv'")
    else:
        print("❌ Error: TCGA RNA-seq file not found in archive!")

### 🔄 Extract GTEx RNA-seq ###
print("🔄 Extracting GTEx RNA-seq data...")
with gzip.open(gtex_gct, "rt") as gct_file:
    lines = gct_file.readlines()

# Process GCT file
meta_info = lines[:2]  # Metadata
columns = lines[2].strip().split("\t")  # Column headers
data = [line.strip().split("\t") for line in lines[3:]]  # Data

# Convert to DataFrame
df_gtex = pd.DataFrame(data, columns=columns)
df_gtex.set_index(columns[0], inplace=True)

# Save to CSV
df_gtex.to_csv("GTEx_Lung_Raw.csv")
print("✅ GTEx RNA-seq extracted & saved as 'GTEx_Lung_Raw.csv'")

