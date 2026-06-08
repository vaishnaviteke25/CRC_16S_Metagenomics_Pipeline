import os

print("Running PICRUSt2 functional prediction...")

cmd = """
picrust2_pipeline.py \
-s rep-seqs.fasta \
-i table.biom \
-o picrust2_results \
-p 4
"""

os.system(cmd)

print("PICRUSt2 completed.")
