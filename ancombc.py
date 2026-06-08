import os

print("Running ANCOM-BC differential abundance analysis...")

cmd = """
qiime composition ancombc \
--i-table table.qza \
--m-metadata-file sample-metadata.tsv \
--p-formula condition
"""

os.system(cmd)

print("ANCOM-BC completed.")
