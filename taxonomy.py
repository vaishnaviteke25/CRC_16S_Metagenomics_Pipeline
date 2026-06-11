from config import METADATA, CLASSIFIER
import subprocess
import os

def taxonomy_analysis():

    print("Running taxonomy classification...\n")

    os.makedirs("results", exist_ok=True)

    subprocess.run("""
    qiime feature-classifier classify-sklearn \
    --i-classifier {CLASSIFIER} \
    --i-reads results/rep-seqs.qza \
    --o-classification results/taxonomy.qza
    """, shell=True, check=True)

    subprocess.run("""
    qiime metadata tabulate \
    --m-input-file results/taxonomy.qza \
    --o-visualization results/taxonomy.qzv
    """, shell=True, check=True)

    subprocess.run("""
    qiime taxa barplot \
    --i-table results/table.qza \
    --i-taxonomy results/taxonomy.qza \
    --m-metadata-file {METADATA} \
    --o-visualization results/taxa-barplot.qzv
    """, shell=True, check=True)

    print("Taxonomy analysis completed.\n")
