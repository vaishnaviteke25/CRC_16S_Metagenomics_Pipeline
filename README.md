This project presents an automated 16S rRNA metagenomics analysis pipeline developed using Python and QIIME2 to investigate gut microbiome alterations associated with colorectal cancer (CRC). The workflow was designed to compare microbial community structure and functional potential between healthy controls and colorectal cancer patient samples.

The pipeline performs the major stages of microbiome analysis, including raw sequencing data processing, quality assessment, sequence denoising, phylogenetic tree construction, taxonomic classification, diversity analysis, differential abundance testing, and functional prediction. The workflow integrates widely used bioinformatics tools such as FastQC, MultiQC, QIIME2, DADA2, ANCOM-BC, and PICRUSt2.

For better organization and reproducibility, the analysis is divided into multiple Python scripts. Each script performs a specific task such as data download, quality control, QIIME2 data import, DADA2 denoising, phylogeny generation, taxonomy assignment, diversity analysis, differential abundance testing, and functional prediction. The complete workflow can be executed automatically using the main script:

```bash
python run_pipeline.py
```

The analysis requires paired-end FASTQ files, a manifest.tsv file containing sample identifiers and file paths, and a sample-metadata.tsv file containing sample information such as Healthy, CRC Distal, and CRC Rectal groups.

Taxonomic classification is performed using a pre-trained SILVA classifier database. Representative sequences generated after DADA2 denoising are assigned taxonomy using the SILVA reference database to identify bacterial taxa present in the samples.

The diversity analysis module calculates both alpha and beta diversity metrics, including Observed Features, Shannon Diversity Index, Faith's Phylogenetic Diversity, Bray-Curtis Dissimilarity, Jaccard Distance, Weighted UniFrac, and Unweighted UniFrac. Principal Coordinate Analysis (PCoA) plots are generated for visualization of microbial community differences between study groups.

Differential abundance analysis is performed using ANCOM-BC to identify significantly altered microbial taxa associated with colorectal cancer. Functional prediction is carried out using PICRUSt2 to infer KEGG Orthologs (KO), Enzyme Commission (EC) numbers, and metabolic pathways from 16S rRNA sequencing data.

The pipeline was developed and executed in a Linux-based environment using Python 3 and QIIME2. All generated outputs, including feature tables, taxonomy assignments, phylogenetic trees, diversity metrics, ANCOM-BC results, PICRUSt2 predictions, and QIIME2 visualization files (.qzv), are stored in the results directory.

This project demonstrates a reproducible computational workflow for studying gut microbiome dysbiosis and functional alterations associated with colorectal cancer using next-generation sequencing (NGS) data.

