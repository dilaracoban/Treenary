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
