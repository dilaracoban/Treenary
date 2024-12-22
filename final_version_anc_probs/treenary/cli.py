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
    parser.add_argument("-rev", action="store_true", help="Revert Treenary file back to a tree structure.")
    parser.add_argument("-node", "--node_file", help="Path to the node probability file.")

    # New arguments for rooting
    parser.add_argument("--root_at", help="Root the tree at a specific node or leaf (provide node name).")
    parser.add_argument("--midpoint", action="store_true", help="Root the tree at the midpoint of the longest path.")

    # New arguments for ladderizing
    parser.add_argument("--ladderize", choices=["ascending", "descending"], help="Ladderize the tree (ascending or descending).")
    
    return parser.parse_args()
