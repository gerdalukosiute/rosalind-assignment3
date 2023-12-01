from Bio import Phylo
from io import StringIO

class Node:
    def __init__(self, par):
        self.p = par
        self.s = set()
        self.lab = ''
        self.sonlabs = set()

def build_tree(newick_tree):
    nodes = []
    tree = Phylo.read(StringIO(newick_tree), "newick")
    root = Node(None)

    def parse_clade(clade, parent):
        node = Node(parent)
        node.lab = clade.name if clade.name else ''
        nodes.append(node)
        for child in clade.clades:
            node.s.add(parse_clade(child, node))
        return node
    
    parse_clade(tree.root, root)
    return nodes

def count_labels(cur):
    trt = set()
    for son in cur.s:
        trt.update(count_labels(son))
    if cur.lab:
        trt.add(cur.lab)
    cur.sonlabs = trt
    return trt

def generate_character_table(nodes, all_labels):
    character_table = []
    for j in nodes:
        if len(j.sonlabs) not in (0, 1, len(all_labels) - 1, len(all_labels)):
            character_array = map(int, map(j.sonlabs.__contains__, all_labels))
            character_table.append("".join(map(str, character_array)))
    return character_table

def main(newick_tree):
    nodes = build_tree(newick_tree)
    all_labels = sorted(count_labels(nodes[0]))
    character_table = generate_character_table(nodes, all_labels)
    for row in character_table:
        print(row)

if __name__ == "__main__":
    newick_tree = "#paste newick tree here"
    main(newick_tree)