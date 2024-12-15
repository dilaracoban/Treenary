# Directory structure and initial file creation

import os

# Define the project structure
project_structure = {
    "treenary_project": {
        "main.py": """\
from treenary.cli import parse_args
from treenary.tree_parser import parse_bestTree
from treenary.treenary_encoder import encode_bestTree
from treenary.anc_tree_parser import parse_ancTree
from treenary.anc_treenary_encoder import encode_ancTree

def main():
    args = parse_args()

    # Parse and encode based on tree type
    if args.anc:
        print(\"Using ancestralTree parser and encoder...\")
        tree = parse_ancTree(args.input)
        encoded_data = encode_ancTree(tree)
    else:
        print(\"Using bestTree parser and encoder...\")
        tree = parse_bestTree(args.input)
        encoded_data = encode_bestTree(tree)

    # Write output to the specified file
    with open(args.output, \"w\") as output_file:
        for name, (treenary_string, branch_length) in encoded_data.items():
            output_file.write(f\"{name}, {treenary_string}, {branch_length}\n\")
    print(f\"Encoded data saved to {args.output}\")

if __name__ == '__main__':
    main()
""",
        "treenary": {
            "__init__.py": """\
# This package contains core functionalities for the Treenary Project.
""",
            "tree_parser.py": """\
from ete3 import Tree

def parse_bestTree(file_path):
    \"\"\"\
    Parses a Newick-format bestTree file.

    Args:
        file_path (str): Path to the bestTree file.

    Returns:
        Tree: An ete3 Tree object representing the phylogenetic tree.
    \"\"\"
    try:
        with open(file_path, 'r') as file:
            tree_string = file.read().strip()
        tree = Tree(tree_string, format=1)  # Newick format
        return tree
    except Exception as e:
        raise ValueError(f\"Error parsing bestTree from {file_path}: {e}\")
""",
            "treenary_encoder.py": """\
def encode_bestTree_node(tree, target_name):
    \"\"\"\
    Encodes a single node in the bestTree by generating its Treenary string.

    Args:
        tree (Tree): An ete3 Tree object.
        target_name (str): Name of the target organism (leaf node).

    Returns:
        str: The Treenary string for the target node.
    \"\"\"
    node = tree.search_nodes(name=target_name)
    if not node:
        raise ValueError(f\"Target organism '{target_name}' not found in the tree.\")
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
    \"\"\"\
    Encodes all leaf nodes in the bestTree.

    Args:
        tree (Tree): An ete3 Tree object.

    Returns:
        dict: A dictionary mapping organism names to their Treenary strings and branch lengths.
              Format: {name: (treenary_string, branch_length)}
    \"\"\"
    encoded_data = {}
    for leaf in tree.iter_leaves():
        treenary_string = encode_bestTree_node(tree, leaf.name)
        branch_length = leaf.dist  # Distance from the parent node
        encoded_data[leaf.name] = (treenary_string, branch_length)
    return encoded_data
""",
            "anc_tree_parser.py": """\
# Placeholder for parsing ancestralTree files
""",
            "anc_treenary_encoder.py": """\
# Placeholder for encoding Treenary strings for ancestralTree
""",
            "cli.py": """\
import argparse

def parse_args():
    \"\"\"\
    Parse command-line arguments for the Treenary Project.

    Returns:
        argparse.Namespace: Parsed arguments.
    \"\"\"
    parser = argparse.ArgumentParser(description=\"Encode phylogenetic trees into Treenary strings.\")
    parser.add_argument(\"-i\", \"--input\", required=True, help=\"Path to the input tree file.\")
    parser.add_argument(\"-o\", \"--output\", required=True, help=\"Path to save the encoded output.\")
    parser.add_argument(\"-anc\", action=\"store_true\", help=\"Use ancestralTree parser and encoder.\")
    return parser.parse_args()
"""
        },
        "tests": {
            "test_tree_parser.py": """\
def test_parse_bestTree():
    # Placeholder: Add unit test for parse_bestTree function.
    pass
""",
            "test_treenary_encoder.py": """\
def test_encode_bestTree_node():
    # Placeholder: Add unit test for encode_bestTree_node function.
    pass

def test_encode_bestTree():
    # Placeholder: Add unit test for encode_bestTree function.
    pass
""",
            "test_anc_tree_parser.py": """\
# Placeholder for testing ancestralTree parser
""",
            "test_anc_treenary_encoder.py": """\
# Placeholder for testing ancestralTree encoder
"""
        },
        "data": {
            "example_bestTree.txt": """\
# Example bestTree data format placeholder
""",
            "example_ancestralTree.txt": """\
# Example ancestralTree data format placeholder
""",
            "example_output.csv": """\
# Example output data placeholder
"""
        },
        "requirements.txt": """\
argparse
pytest
ete3
""",
        "setup.py": """\
from setuptools import setup, find_packages

setup(
    name='treenary_project',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'treenary=main:main'
        ]
    },
    install_requires=[
        'argparse',
        'ete3'
    ],
    author='Your Name',
    description='Command-line tool for encoding phylogenetic tree nodes into Treenary strings.',
)
""",
        "README.md": """\
# Treenary Project

This project encodes phylogenetic tree nodes into Treenary strings for machine learning applications.

## Usage
To run the program:
```bash
python main.py -i data/example_bestTree.txt -o data/example_output.csv
```
To handle ancestral trees, use the `-anc` flag:
```bash
python main.py -i data/example_ancestralTree.txt -o data/example_output.csv -anc
```
""",
        "LICENSE": """\
# Placeholder for project license.
"""
    }
}

# Helper function to create directories and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as file:
                file.write(content)

# Create the project
create_structure('.', project_structure)
