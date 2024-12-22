import pandas as pd

def parse_ancestral_prob_file(file_path):
    """
    Parses a file with node probabilities for each site.

    Args:
        file_path (str): Path to the input file containing node probabilities.

    Returns:
        dict: A dictionary where keys are node names and values are lists of (site, probabilities).
    """
    data = pd.read_csv(file_path, sep="\t")

    nodes = {}

    for _, row in data.iterrows():
        node_name = row["Node"] 
        site = row["Site"]  
        probabilities = row.iloc[3:].to_dict()  

        if node_name not in nodes:
            nodes[node_name] = []
        nodes[node_name].append((site, probabilities))

    return nodes


def generate_node_sequences(probabilities):
    """
    Generates sequences for nodes based on probabilities in the desired format.

    Args:
        probabilities (dict): Node probabilities parsed from the input file.

    Returns:
        dict: A dictionary where keys are node names and values are formatted sequences.
    """
    sequences = {}

    for node, sites in probabilities.items():
        sequence = []
        for site, probs in sites:
            sorted_probs = sorted(probs.items(), key=lambda x: x[1], reverse=True)
            top_amino, top_prob = sorted_probs[0]

            if top_prob > 0.999:
                sequence.append(top_amino.replace('p_', ''))

            else:
                compressed = f"{top_amino.replace('p_', '')}(" + \
                    ",".join(f"{aa.replace('p_', '')}:{p:.2f}" for aa, p in sorted_probs if p > 0.01) + ")"
                sequence.append(compressed)
        sequences[node] = ''.join(sequence)

    return sequences



def save_node_sequences_as_fasta(output_path, sequences):
    with open(output_path, "w") as output_file:
        for name, sequence in sequences.items():
            output_file.write(f">{name}\n{sequence}\n")

def parse_msa_fasta(file_path):
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
                current_organism = line[1:].split()[0].split('|')[-1]
                current_sequence = []
            else:
                current_sequence.append(line)

        if current_organism:
            sequences[current_organism] = "".join(current_sequence)

    return sequences

