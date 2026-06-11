This project is an automated 16S rRNA microbiome analysis pipeline developed using Python and QIIME2 for studying gut microbiome alterations associated with colorectal cancer (CRC). The workflow compares Healthy, CRC Distal, and CRC Rectal samples through sequence processing, taxonomic classification, diversity analysis, and differential abundance testing.

The pipeline is divided into separate Python scripts for better organization. The main script, run_pipeline.py, executes the complete workflow automatically. Other scripts perform specific tasks including sequence import, DADA2 denoising, feature table summarization, phylogenetic tree generation, taxonomy assignment, diversity analysis, and ANCOM-BC differential abundance testing.

Paired-end FASTQ files should be listed in a manifest.tsv file containing sample IDs and absolute file paths. A sample-metadata.tsv file is required for group information such as Healthy, CRC Distal, and CRC Rectal samples. Taxonomic classification is performed using a pre-trained SILVA classifier (.qza file).

The pipeline was developed and tested on Linux/WSL with Python 3 and QIIME2 installed. The complete workflow can be executed using:

python run_pipeline.py

All generated outputs are stored in the results/ directory, including feature tables, representative sequences, phylogenetic trees, taxonomy assignments, diversity metrics, ANCOM-BC results, and QIIME2 visualization files (.qzv).

## Requirements

- Python 3
- QIIME2 (2025.10)
- SILVA classifier (.qza)

## Run

```bash
conda activate qiime2-amplicon-2025.10
python run_pipeline.py
