from ete3 import Tree

def decode_treenary_file(input_file):
    """
    Reads a Treenary file and reconstructs an ETE3 tree.
    
    Args:
        input_file (str): Path to the input Treenary file.

    Returns:
        Tree: Reconstructed ETE3 tree.
    """
    root = Tree()  # Start with an empty tree

    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 4:
                raise ValueError(f"Invalid line format: {line}")
            
            node_name = parts[0].strip()
            treenary_string = parts[1].strip()
            branch_length = float(parts[2].strip())

            decode_treenary_string(root, treenary_string, node_name, branch_length)

    return root

def decode_treenary_string(tree, treenary_string, node_name, branch_length):
    """
    Decodes a Treenary string and adds a node to the tree.

    Args:
        tree (ete3.Tree): The root tree to build upon.
        treenary_string (str): The Treenary string (e.g., "112").
        node_name (str): The name of the node.
        branch_length (float): The branch length for this node.
    """
    current_node = tree

    for char in treenary_string:
        if char == "1":
            if len(current_node.children) < 1:
                current_node.add_child(name=None)
            current_node = current_node.children[0]  # Go to left child
        elif char == "2":
            if len(current_node.children) < 2:
                current_node.add_child(name=None)
            current_node = current_node.children[1]  # Go to right child

    current_node.name = node_name
    current_node.dist = branch_length
