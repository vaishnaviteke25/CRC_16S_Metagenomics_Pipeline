import subprocess
import os
from config import METADATA, SAMPLING_DEPTH

def diversity_analysis():

    print("Running diversity analysis...\n")

    subprocess.run(f"""
    qiime diversity core-metrics-phylogenetic \
    --i-phylogeny results/rooted-tree.qza \
    --i-table results/table.qza \
    --p-sampling-depth {SAMPLING_DEPTH} \
    --m-metadata-file {METADATA} \
    --output-dir results/core-metrics-results
    """, shell=True, check=True)

    print("Diversity analysis completed.\n")
