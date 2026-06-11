import subprocess
import os

def import_data():

    print("Importing sequences...\n")

    os.makedirs("results", exist_ok=True)

    subprocess.run("""
    qiime tools import \
    --type 'SampleData[PairedEndSequencesWithQuality]' \
    --input-path ../manifest.tsv \
    --output-path results/demux.qza \
    --input-format PairedEndFastqManifestPhred33V2
    """, shell=True, check=True)

    subprocess.run("""
    qiime demux summarize \
    --i-data results/demux.qza \
    --o-visualization results/demux.qzv
    """, shell=True, check=True)

    print("Import completed.\n")
