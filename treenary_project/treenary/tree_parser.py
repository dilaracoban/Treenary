from ete3 import Tree


def parse_fasta(file_path):
    """
    Parses a FASTA file to extract organism names and protein sequences.

    Args:
        file_path (str): Path to the FASTA file.

    Returns:
        dict: A dictionary where keys are organism names and values are protein sequences.
    """
    sequences = {}
    current_organism = None
    current_sequence = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_organism:
                    sequences[current_organism] = "".join(current_sequence)
                # Extract only the organism name before any spaces or pipes
                current_organism = line[1:].split()[0].split('|')[-1]
                current_sequence = []
            else:
                current_sequence.append(line)

        # Add the last organism's sequence
        if current_organism:
            sequences[current_organism] = "".join(current_sequence)

    return sequences


def parse_bestTree(file_path):
    """    Parses a Newick-format bestTree file.

    Args:
        file_path (str): Path to the bestTree file.

    Returns:
        Tree: An ete3 Tree object representing the phylogenetic tree.
    """
    try:
        with open(file_path, 'r') as file:
            tree_string = file.read().strip()
        tree = Tree(tree_string, format=1)  # Newick format
        return tree
    except Exception as e:
        raise ValueError(f"Error parsing bestTree from {file_path}: {e}")
