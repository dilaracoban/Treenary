# Treenary Project

The **Treenary Project** is a command-line tool that encodes phylogenetic tree nodes into machine-learnable **Treenary strings**. These strings uniquely represent the position of organisms or nodes within a phylogenetic tree. The project supports both **bestTree** and **ancestralTree** formats and optionally integrates protein sequences from MSA (Multiple Sequence Alignment) files.

---

## Goal

Understanding the position of organisms within a phylogenetic tree is critical for the clinical significance of genetic mutations. This tool:
- Converts **tree nodes** (leaf or ancestral) into **Treenary strings**.
- Generates machine-learning-ready vector representations.
- Optionally includes **protein sequences** from MSA files to enrich the output.

---

## Features
- Support for both **bestTree** and **ancestralTree** files in Newick format.
- Generation of **Treenary strings** padded to uniform lengths.
- Integration of protein sequences using MSA FASTA files.
- Outputs data in an easy-to-read CSV-style format.

---

## Installation

Clone the repository and install the dependencies:

##### git clone https://github.com/dilaracoban/Treenary
##### cd traj/treenary_project
##### pip install -r requirements.txt



---

## Usage

### 1. For BestTree Files
Run the program without any additional options to parse a **bestTree** file:

##### python main.py -i ../aperta/A0A075B6H7.raxml.bestTree -o outputs/filename.Treenary


- `-i`: Input tree file (Newick format, RAxML bestTree).
- `-o`: Output file path.

**Example Output**:

Organism1, 11220, 0.03
Organism2, 11212, 0.07



---

### 2. For AncestralTree Files
Use the `-anc` option to parse an **ancestralTree** file:

##### python main.py -i ../aperta/A0A075B6H7.raxml.ancestraltTree -o outputs/filename.Treenary -anc



---

### 3. Including MSA Protein Sequences
To include protein sequences from an MSA **FASTA** file, provide the `-msa` option:

##### python main.py -i ../aperta/A0A075B6H7.raxml.bestTree -msa ../aperta/A0A075B6H7_nogap_msa.fasta -o outputs/filename.Treenary


**Example Output**:

Organism1, 11220, 0.03, MVQSPK... Organism2, 11212, 0.07, MTDLQP...

---

## Dependencies
- Python 3.8+
- [ETE3](http://etetoolkit.org/) for tree parsing.
- argparse (built-in Python module).

Install dependencies using:

##### pip install -r requirements.txt



---

## License

This project is bachelor thesis for ENS492 Graduation Project - Implementation Course in Sabanci University. Project supervisor is Ogun Adebali.
---

## Author and Contributors
- **Dilara Coban**  
- **Contact**: dilara.coban@sabanciuniv.edu 
- **GitHub**: [dilaracoban](https://github.com/dilaracoban)

- **Ogun Adebali**  
- **Contact**: ogun.adebali@sabanciuniv.edu


