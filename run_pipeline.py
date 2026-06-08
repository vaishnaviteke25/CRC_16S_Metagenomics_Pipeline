import os

print("Starting CRC 16S Metagenomics Pipeline")

os.system("python download_data.py")
os.system("python fastqc.py")
os.system("python import_data.py")
os.system("python denoise.py")
os.system("python phylogeny.py")
os.system("python taxonomy.py")
os.system("python diversity.py")
os.system("python ancombc.py")
os.system("python picrust2.py")

print("Pipeline completed successfully.")
