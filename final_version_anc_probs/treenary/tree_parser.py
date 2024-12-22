from ete3 import Tree

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


def parse_ancTree(file_path):
    """
    Parses a Newick-format ancestralTree file.

    Args:
        file_path (str): Path to the ancestralTree file.

    Returns:
        Tree: An ete3 Tree object representing the phylogenetic tree.
    """
    try:
        with open(file_path, 'r') as file:
            tree_string = file.read().strip()
        tree = Tree(tree_string, format=1)  # Newick format
        return tree
    except Exception as e:
        raise ValueError(f"Error parsing ancestralTree from {file_path}: {e}")
