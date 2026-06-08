import os

print("Assigning taxonomy using SILVA database...")

cmd = """
qiime feature-classifier classify-sklearn \
--i-classifier silva-138-classifier.qza \
--i-reads rep-seqs.qza \
--o-classification taxonomy.qza
"""

os.system(cmd)

print("Taxonomy assignment completed.")
