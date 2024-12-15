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

## Version History


### First Version Summary (v1.0)
The first version of the application focused on understanding the position of organisms within a phylogenetic tree. Key features included:
- Converting **tree nodes** (leaf or ancestral) into **Treenary strings**.
- Generating machine-learning-ready vector representations of these strings.
- Optionally including **protein sequences** from MSA files to enrich the output.

**Usage Examples (v1.0):**
1. For **bestTree files**:
```bash
python main.py -i ../aperta/A0A075B6H7.raxml.bestTree -o outputs/filename.Treenary
```

2. For **ancestralTree files**:
```bash
python main.py -i ../aperta/A0A075B6H7.raxml.ancestralTree -o outputs/filename.Treenary -anc
```

3. To include **MSA protein sequences**:
```bash
python main.py -i ../aperta/A0A075B6H7.raxml.bestTree -msa ../aperta/A0A075B6H7_nogap_msa.fasta -o outputs/filename.Treenary
```
---

### Second Version Enhancements (v2.1)
In version 2.1, reverse functionality was introduced to allow users to convert Treenary files back into tree structures:

#### New Features in v2.1:
- **Reverse Conversion**: Convert Treenary files back into ETE3-compatible tree structures.
- Output the reconstructed tree in **Newick format**.

**Usage for Reverse Conversion:**
```bash
python main.py -i ../outputs/trial1810 -o ../rev_outputs/v2_1814 -rev
```
- `-i`: Input Treenary file.
- `-o`: Output file path (Newick format).
- `-rev`: Flag to enable reverse conversion.

---

### Third Version: Advanced Tree Manipulation (v2.2)
In version 2.2, additional **tree manipulation functionalities** were introduced for **bestTree files** before Treenary encoding. These include **rooting** and **ladderizing** options using the ETE3 library.

#### New Features in v2.2:
1. **Rooting Options**:
   - Root the tree at a **specific node** using `--root_at`.
   - Apply **midpoint rooting** using `--midpoint`.

2. **Ladderizing Options**:
   - **Ascending Ladderization**: Smaller subtrees appear first (`--ladderize ascending`).
   - **Descending Ladderization**: Larger subtrees appear first (`--ladderize descending`).

3. **Flexible CLI Integration**:
   - Rooting and ladderizing are applied **before encoding** the tree into Treenary format.
   - These options are exclusive to **bestTree files**.

#### Updated Workflow for BestTree Files:
1. Parse the tree.
2. Apply rooting (if specified):
   - **Root at a node**: `--root_at Node1`
   - **Midpoint rooting**: `--midpoint`
3. Apply ladderizing (if specified):
   - **Ascending**: `--ladderize ascending`
   - **Descending**: `--ladderize descending`
4. Generate Treenary strings after the modifications.

**Usage Examples for v2.2:**

1. **Root at a Specific Node**:
```bash
python main.py -i ../aperta/A0A075B6H7.raxml.bestTree -o outputs/rooted_tree.Treenary --root_at Node1
```

2. **Midpoint Rooting**:
```bash
python main.py -i ../aperta/A0A075B6H7.raxml.bestTree -o outputs/midpoint_rooted_tree.Treenary --midpoint
```

3. **Ladderize in Ascending Order**:
```bash
python main.py -i ../aperta/A0A075B6H7.raxml.bestTree -o outputs/ladderized_ascending_tree.Treenary --ladderize ascending
```

4. **Combine Rooting and Ladderizing**:
```bash
python main.py -i ../aperta/A0A075B6H7.raxml.bestTree -o outputs/rooted_ladderized_tree.Treenary --midpoint --ladderize descending
```

---

### Summary of Version Differences
| **Version** | **Features**                                                                                       |
|-------------|--------------------------------------------------------------------------------------------------|
| **v1.0**    | - Treenary string generation for bestTree and ancestralTree files.                               |
|             | - Optionally include protein sequences from MSA files.                                           |
| **v2.1**    | - Added reverse functionality to convert Treenary files back to tree structures (ETE3/Newick).   |
| **v2.2**    | - Added rooting options (specific node, midpoint rooting) for bestTree files.                   |
|             | - Added ladderizing options (ascending and descending) for bestTree files.                      |
|             | - Applied rooting/ladderizing **before** Treenary encoding.                                      |

---

### Future Considerations
- Extend rooting and ladderizing functionalities to ancestralTree files.
- Integrate additional tree manipulation tools (e.g., subtree extraction, rerooting on user-defined criteria).
- Explore tree visualization options directly from Treenary files.



## License

This project is bachelor thesis for ENS492 Graduation Project - Implementation Course in Sabanci University. Project supervisor is Ogun Adebali


## Author and Contributors
- **Dilara Coban**  
- **Contact**: dilara.coban@sabanciuniv.edu 
- **GitHub**: [dilaracoban](https://github.com/dilaracoban)

- **Ogun Adebali**  
- **Contact**: ogun.adebali@sabanciuniv.edu


