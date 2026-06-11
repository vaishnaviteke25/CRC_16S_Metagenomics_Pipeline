import subprocess
import os

def run_ancombc():

    print("Running ANCOM-BC...\n")

    os.makedirs("results", exist_ok=True)

    subprocess.run("""
    qiime composition ancombc \
    --i-table results/table.qza \
    --m-metadata-file /mnt/d/COLON3/raw_data/dada2_out/sample-metadata.tsv \
    --p-formula condition \
    --o-differentials results/ancombc_differentials.qza
    """, shell=True, check=True)

    print("ANCOM-BC completed.\n")
