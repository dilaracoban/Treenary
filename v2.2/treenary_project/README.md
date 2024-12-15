# Treenary Project v2.1

This version also includes conversting back to Trees from treenary files in addition to the functionality inhertited from v1.

## Usage

1. For BestTree Files
Run the program without any additional options to parse a bestTree file:

python main.py -i ../aperta/A0A075B6H7.raxml.bestTree -o outputs/filename.Treenary
-i: Input tree file (Newick format, RAxML bestTree).
-o: Output file path.
Example Output:

Organism1, 11220, 0.03
Organism2, 11212, 0.07
2. For AncestralTree Files
Use the -anc option to parse an ancestralTree file:

python main.py -i ../aperta/A0A075B6H7.raxml.ancestralTree -o outputs/filename.Treenary -anc
3. Including MSA Protein Sequences
To include protein sequences from an MSA FASTA file, provide the -msa option:

python main.py -i ../aperta/A0A075B6H7.raxml.bestTree -msa ../aperta/A0A075B6H7_nogap_msa.fasta -o outputs/filename.Treenary
Example Output:

Organism1, 11220, 0.03, MVQSPK...
Organism2, 11212, 0.07, MTDLQP...
4. Reverting Treenary Files Back to Trees
To convert a Treenary file back into a tree structure (ETE3 format or Newick file), use the -rev option:

python main.py -i ../outputs/trial1810 -o ../rev_outputs/v2_1814 -rev
-i: Input Treenary file.
-o: Output file path (Newick format).
-rev: Flag to enable reverse conversion.
