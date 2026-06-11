from import_data import import_data
from denoise import run_dada2
from summarize import summarize_data
from phylogeny import generate_tree
from taxonomy import taxonomy_analysis
from diversity import diversity_analysis
from ancombc import run_ancombc

def main():

    print("Starting CRC 16S Metagenomics Pipeline...\n")

    import_data()
    run_dada2()
    summarize_data()
    generate_tree()
    taxonomy_analysis()
    diversity_analysis()
    run_ancombc()

    print("\nPipeline completed successfully!")

if __name__ == "__main__":
    main()
