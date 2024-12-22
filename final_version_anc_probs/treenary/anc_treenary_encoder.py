def encode_ancTree(tree):
    """
    Encodes all nodes (both leaf and internal nodes) in the ancestralTree.

    Args:
        tree (Tree): An ete3 Tree object.

    Returns:
        dict: A dictionary mapping node names to their Treenary strings and branch lengths.
              Format: {name: (treenary_string, branch_length)}
    """
    encoded_data = {}

    def traverse(node, path):
        # Generate Treenary string for the current node
        if node.name:
            treenary_string = ''.join(path)
            encoded_data[node.name] = (treenary_string, node.dist)

        # Traverse children
        for i, child in enumerate(node.get_children()):
            traverse(child, path + ['1' if i == 0 else '2'])

    # Start traversal from the root
    traverse(tree, [])
    return encoded_data

def combine_node_and_leaf_sequences(node_sequences, leaf_sequences):
    """
    Combines node and leaf sequences into a single dictionary.

    Args:
        node_sequences (dict): Dictionary of node sequences.
        leaf_sequences (dict): Dictionary of leaf sequences.

    Returns:
        dict: A dictionary with combined node and leaf sequences.
    """
    combined_sequences = {}
    combined_sequences.update(node_sequences)
    combined_sequences.update(leaf_sequences)
    return combined_sequences


def write_treenary_with_msa(output_path, treenary_data, sequences=None):
    """
    Writes treenary Treenary strings, branch lengths, and protein sequences to an output file.

    Args:
        output_path (str): Path to the output file.
        treenary_data (dict): Dictionary with treenary Treenary strings.
        sequences (dict, optional): Dictionary of protein sequences.
    """
    with open(output_path, "w") as output_file:
        for name, (treenary_string, branch_length) in treenary_data.items():
            sequence = sequences.get(name, "N/A") if sequences else "N/A"
            output_file.write(f"{name}, {treenary_string}, {branch_length}, {sequence}\n")


