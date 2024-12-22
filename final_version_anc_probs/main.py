from treenary.cli import parse_args
from treenary.tree_parser import parse_bestTree, parse_ancTree
from treenary.treenary_encoder import encode_bestTree, write_treenary_with_msa
from treenary.anc_treenary_encoder import encode_ancTree, combine_node_and_leaf_sequences
from treenary.revert_treenary import decode_treenary_file
from treenary.probabilistic_parser import parse_ancestral_prob_file, generate_node_sequences, parse_msa_fasta, save_node_sequences_as_fasta


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
    

    if args.anc:
        print("Using ancestralTree parser and encoder...")
        tree = parse_ancTree(args.input)
        encoded_data = encode_ancTree(tree)

        node_sequences = None
        if args.node_file:
            print(f"Parsing Node Probabilities file: {args.node_file}")
            probabilities = parse_ancestral_prob_file(args.node_file)
            node_sequences = generate_node_sequences(probabilities)
            save_node_sequences_as_fasta("node_sequences.fasta", node_sequences)
            node_sequences = parse_msa_fasta("node_sequences.fasta")

        leaf_sequences = None
        if args.msa_file:
            print(f"Parsing MSA file: {args.msa_file}")
            leaf_sequences = parse_msa_fasta(args.msa_file)

        if node_sequences and leaf_sequences:
            combined_sequences = combine_node_and_leaf_sequences(node_sequences, leaf_sequences)
            write_treenary_with_msa(args.output, encoded_data, combined_sequences)
            return
        
        elif node_sequences:
            print("Node sequences provided but no leaf sequences. Writing Treenary file with only node sequences.")
            write_treenary_with_msa(args.output, encoded_data, node_sequences)
            return
        
        elif leaf_sequences:
            print("Leaf sequences provided but no node sequences. Writing Treenary file with only leaf sequences.")
            write_treenary_with_msa(args.output, encoded_data, leaf_sequences)
            return


        

    else:
        print("Using bestTree parser and encoder...")
        tree = parse_bestTree(args.input)

        # Apply rooting and ladderizing if specified
        if args.midpoint or args.root_at:
            apply_rooting(tree, args.root_at, args.midpoint)

        if args.ladderize:
            apply_ladderizing(tree, args.ladderize)

        encoded_data = encode_bestTree(tree)

        # Parse MSA file if provided
        sequences = None
        if args.msa_file:
            print(f"Parsing MSA file: {args.msa_file}")
            sequences = parse_msa_fasta(args.msa_file)

        # Write the output
        if sequences:
            write_treenary_with_msa(args.output, encoded_data, sequences)
        else:
            write_treenary_with_msa(args.output, encoded_data)

    print(f"Encoded data saved to {args.output}")


if __name__ == "__main__":
    main()
