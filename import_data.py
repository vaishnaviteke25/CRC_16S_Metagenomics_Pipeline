import os

print("Starting QIIME2 import...")

cmd = """
qiime tools import \
--type 'SampleData[PairedEndSequencesWithQuality]' \
--input-path manifest.tsv \
--output-path demux-paired.qza \
--input-format PairedEndFastqManifestPhred33V2
"""

os.system(cmd)

print("Import completed.")
