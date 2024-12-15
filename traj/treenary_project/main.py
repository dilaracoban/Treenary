from treenary.cli import parse_args
from treenary.tree_parser import parse_bestTree, parse_fasta
from treenary.treenary_encoder import encode_bestTree, pad_treenary_strings, write_padded_treenary_with_msa
from treenary.anc_tree_parser import parse_ancTree
from treenary.anc_treenary_encoder import encode_ancTree

def main():
    args = parse_args()

    # Parse and encode based on tree type
    if args.anc:
        print("Using ancestralTree parser and encoder...")
        tree = parse_ancTree(args.input)
        encoded_data = encode_ancTree(tree)
    else:
        print("Using bestTree parser and encoder...")
        tree = parse_bestTree(args.input)
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
