import os

print("Downloading FASTQ files from ENA...")

# Example download command
# Replace accession numbers with your own samples

os.system("wget ftp://ftp.sra.ebi.ac.uk/path/sample.fastq.gz")

print("Download completed.")
