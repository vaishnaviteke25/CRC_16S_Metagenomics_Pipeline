import os

print("Running diversity analysis...")

cmd = """
qiime diversity core-metrics-phylogenetic \
--i-phylogeny rooted-tree.qza \
--i-table table.qza \
--p-sampling-depth 10000 \
--m-metadata-file sample-metadata.tsv \
--output-dir diversity-core-metrics-phylogenetic
"""

os.system(cmd)

print("Diversity analysis completed.")
