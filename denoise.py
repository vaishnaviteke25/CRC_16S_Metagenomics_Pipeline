import subprocess
import os

def run_dada2():

    print("Running DADA2 denoising...\n")

    os.makedirs("results", exist_ok=True)

    subprocess.run("""
qiime dada2 denoise-paired \
--i-demultiplexed-seqs results/demux.qza \
--p-trunc-len-f 240 \
--p-trunc-len-r 200 \
--o-table results/table.qza \
--o-representative-sequences results/rep-seqs.qza \
--o-denoising-stats results/denoising-stats.qza \
--o-base-transition-stats results/base-transition-stats.qza
""", shell=True, check=True)

    print("DADA2 completed.\n")
