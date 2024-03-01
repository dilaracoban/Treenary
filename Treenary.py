import numpy as np
import ete3 as ete

## Read a newick tree file given by the user, and ladderize the tree

treefile = "A0A075B6H7.raxml.bestTree" #input("Enter the name of the file containing the newick tree: ")
file1 = open(treefile,"r")
nwk_tree = file1.read()

if nwk_tree.count("(") != nwk_tree.count(",") - 1:
    print("The tree has an unequal number of internal nodes and leaves. Please provide a valid newick tree.")
    #exit()

# ladderize the tree

t = ete.Tree(nwk_tree)
t.ladderize()
rp = t.get_midpoint_outgroup()
t.set_outgroup(rp)

# t is the tree, now convert it back to nwk  format as s
s = t.write(format=1)

print(s.count("("))
print(s.count(")")) 
print(s.count(","))

## check to ensure no 3 branches are coming out of a node
if s.count("(") != s.count(","):
    print("The tree has an unequal number of internal nodes and leaves. Please provide a valid newick tree.")
    #exit()

print(t)

# define another class nwkNode that has elements: string id, string sequence, string distance, and a string that represents the position of the node in the tree
class nwkNode:
    def __init__(self, id, distance, position):
        self.id = id
        self.distance = distance
        self.position = position
        self.sequence = ""


IDs = []
code = ''
nwkNodes = []

# A function to find position string of a node from newick format
nodeCount = 0

# read s from beginning. If you see "(" then add 1 to code, (its a leaf)
# if you see "," then delete the last number from code and add 2 to code, (its a leaf)
# if you see ")" then delete the last number from code and add 0 to code, (its a node)

for i in range(len(s)):
    if s[i] == '(':
        code += '1'
    if s[i] == ',':
        code = code[:-1] + '2'
    if s[i] == ')':
        code = code[:-1] + '0'

        # if you see a letter after '(' then create a new nwkNode element, add it in nwkNodes list with element.position = code, element.sequence = "Leaf", element.distance = "" and add the following letters to the id until ':' is seen then if you see a letter after ":" then add the the following letters to the last node.distance in nwkNodes until ')' or ',' is seen
# if you see a letter after ',' then create a new nwkNode element, add it in nwkNodes list with element.position = code, element.sequence = "Leaf", element.distance = "" and add the following letters to the id until ':' is seen then if you see a letter after ":" then add the the following letters to the last node.distance in nwkNodes until ')' or ',' is seen
# if you see a ':' after ')' then create a nwkNode element element.id = 'None' = code, element.sequence = "Node",add the the following letters to the last node.distance in nwkNodes until ')' or ',' is seen
# if you see a letter after ':' then add the the following letters to the last node.distance in nwkNodes until ')' or ',' is seen
    if s[i] == '(' and s[i+1].isalpha():
        nwkNodes.append(nwkNode(s[i+1], "", code))
        i += 2
        while s[i] != ':' and s[i] != ')' and s[i] != ',':
            nwkNodes[nodeCount].id += s[i]
            i += 1
        if s[i] == ':':
            i += 1
            while s[i] != ')' and s[i] != ',':
                nwkNodes[nodeCount].distance += s[i]
                i += 1
        nodeCount += 1
## Open MSA file and read sequences

fastafile = "A0A075B6H7_nogap_msa.fasta" #input("Enter the name of the file containing the MSA: ")
file2 = open(fastafile,"r")
lines = file2.readlines()

# If the line starts with >  it is a header, if it starts with a letter it is a sequence
#find that header in nwkNodes id's and add the sequence to that nwkNode.sequence

for line in lines:
    if line[0] == '>':
        for n in nwkNodes:
            if n.id in line:
                n.sequence = lines[lines.index(line)+1].strip()

# save n.id, n.sequence, n.distance, n.position into a file A0A075B6H7.treenary
for n in nwkNodes:
    print(n.id, n.sequence, n.distance, n.position)

# A0A075B6H7.treenary
file3 = open("A0A075B6H7.treenary","w")
for n in nwkNodes:
    file3.write(n.id + " " + n.sequence + " " + n.distance + " " + n.position + "\n")
file3.close()

