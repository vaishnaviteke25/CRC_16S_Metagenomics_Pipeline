import os

print("Running FastQC...")

os.system("fastqc *.fastq.gz")

print("FastQC completed.")

print("Running MultiQC...")

os.system("multiqc .")

print("MultiQC report generated.")
