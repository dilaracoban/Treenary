def encode_bestTree_node(tree, target_name):
    """    Encodes a single node in the bestTree by generating its Treenary string.

    Args:
        tree (Tree): An ete3 Tree object.
        target_name (str): Name of the target organism (leaf node).

    Returns:
        str: The Treenary string for the target node.
    """
    node = tree.search_nodes(name=target_name)
    if not node:
        raise ValueError(f"Target organism '{target_name}' not found in the tree.")
    node = node[0]

    treenary_string = []
    while node.up:  # Traverse from leaf to root
        parent = node.up
        if parent.get_children().index(node) == 0:  # Left child
            treenary_string.append('1')
        else:  # Right child
            treenary_string.append('2')
        node = parent

    return ''.join(reversed(treenary_string))  # Reverse to get root-to-leaf path

def encode_bestTree(tree):
    """    Encodes all leaf nodes in the bestTree.

    Args:
        tree (Tree): An ete3 Tree object.

    Returns:
        dict: A dictionary mapping organism names to their Treenary strings and branch lengths.
              Format: {name: (treenary_string, branch_length)}
    """
    encoded_data = {}
    for leaf in tree.iter_leaves():
        treenary_string = encode_bestTree_node(tree, leaf.name)
        branch_length = leaf.dist  # Distance from the parent node
        encoded_data[leaf.name] = (treenary_string, branch_length)
    return encoded_data

def pad_treenary_strings(encoded_data):
    """
    Pads Treenary strings with 0s to make all strings the same length.

    Args:
        encoded_data (dict): Dictionary with organism names as keys and 
                             (treenary_string, branch_length) as values.

    Returns:
        dict: Updated dictionary with padded Treenary strings.
    """
    # Find the maximum length of Treenary strings
    max_length = max(len(treenary) for treenary, _ in encoded_data.values())

    # Pad each Treenary string with 0s
    padded_data = {
        name: (treenary.ljust(max_length, '0'), branch_length)
        for name, (treenary, branch_length) in encoded_data.items()
    }
    return padded_data

def write_padded_treenary(output_path, padded_data):
    """
    Writes padded Treenary strings and branch lengths to an output file.

    Args:
        output_path (str): Path to the output file.
        padded_data (dict): Dictionary with padded Treenary strings.
    """
    with open(output_path, "w") as output_file:
        for name, (padded_string, branch_length) in padded_data.items():
            output_file.write(f"{name}, {padded_string}, {branch_length}\n")

def write_padded_treenary_with_msa(output_path, padded_data, sequences=None):
    """
    Writes padded Treenary strings, branch lengths, and protein sequences to an output file.

    Args:
        output_path (str): Path to the output file.
        padded_data (dict): Dictionary with padded Treenary strings.
        sequences (dict, optional): Dictionary of protein sequences.
    """
    with open(output_path, "w") as output_file:
        for name, (padded_string, branch_length) in padded_data.items():
            sequence = sequences.get(name, "N/A") if sequences else "N/A"
            output_file.write(f"{name}, {padded_string}, {branch_length}, {sequence}\n")
