import argparse

def parse_args():
    """    Parse command-line arguments for the Treenary Project.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Encode phylogenetic trees into Treenary strings.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input tree file.")
    parser.add_argument("-o", "--output", required=True, help="Path to save the encoded output.")
    parser.add_argument("-msa", "--msa_file", help="Path to the MSA FASTA file.")
    parser.add_argument("-anc", action="store_true", help="Use ancestralTree parser and encoder.")
    return parser.parse_args()
