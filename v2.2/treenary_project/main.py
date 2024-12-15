from treenary.cli import parse_args
from treenary.tree_parser import parse_bestTree, parse_fasta
from treenary.treenary_encoder import encode_bestTree, pad_treenary_strings, write_padded_treenary_with_msa
from treenary.anc_tree_parser import parse_ancTree
from treenary.anc_treenary_encoder import encode_ancTree
from treenary.revert_treenary import decode_treenary_file


def apply_rooting(tree, root_at, midpoint):
    """
    Apply rooting to the tree.
    """
    if midpoint:
        print("Applying midpoint rooting...")
        midpoint_outgroup = tree.get_midpoint_outgroup()
        tree.set_outgroup(midpoint_outgroup)
    elif root_at:
        print(f"Rooting the tree at node: {root_at}")
        try:
            tree.set_outgroup(tree & root_at)
        except:
            raise ValueError(f"Node '{root_at}' not found in the tree.")


def apply_ladderizing(tree, direction):
    """
    Apply ladderizing to the tree.
    """
    if direction == "ascending":
        print("Ladderizing tree in ascending order...")
        tree.ladderize(direction=1)
    elif direction == "descending":
        print("Ladderizing tree in descending order...")
        tree.ladderize(direction=-1)



def main():
    args = parse_args()

    if args.rev:
        print(f"Reverting Treenary file: {args.input}")
        tree = decode_treenary_file(args.input)
        tree.write(outfile=args.output, format=1)  # Save as Newick format
        print(f"Reconstructed tree saved to {args.output}")
        return

    # Parse and encode based on tree type
    if args.anc:
        print("Using ancestralTree parser and encoder...")
        tree = parse_ancTree(args.input)
        encoded_data = encode_ancTree(tree)
    else:
        print("Using bestTree parser and encoder...")
        tree = parse_bestTree(args.input)

        # Apply rooting and ladderizing (v3 trial) if specified
        if args.midpoint or args.root_at:
            apply_rooting(tree, args.root_at, args.midpoint)

        if args.ladderize:
            apply_ladderizing(tree, args.ladderize)

        encoded_data = encode_bestTree(tree)


    # Pad Treenary strings
    padded_data = pad_treenary_strings(encoded_data)

    # Parse MSA file if provided
    sequences = None
    if args.msa_file:
        print(f"Parsing MSA file: {args.msa_file}")
        sequences = parse_fasta(args.msa_file)

    # Write the output
    write_padded_treenary_with_msa(args.output, padded_data, sequences)
    print(f"Encoded data saved to {args.output}")

if __name__ == '__main__':
    main()
