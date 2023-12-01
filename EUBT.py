class tree_node():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return "internal_{}".format(id(self))

class tree_edge():
    def __init__(self, node1, node2):
        self.nodes = [node1, node2]
    def __str__(self):
        return "{}--{}".format(*self.nodes)

class binary_tree():
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
    def __str__(self):
        return "tree_{} edges: {}".format(id(self), [str(x) for x in self.edges])
    def copy(self):
        node_mapping = {node: tree_node(node.name) for node in self.nodes}
        new_nodes = list(node_mapping.values())
        new_edges = [tree_edge(node_mapping[edge.nodes[0]], node_mapping[edge.nodes[1]]) for edge in self.edges]
        new_tree = binary_tree(new_nodes, new_edges)
        return new_tree

def enumerate_trees(leaves):
    if len(leaves) == 2:
        leaf1, leaf2 = leaves
        t = binary_tree()
        t.nodes = [tree_node(leaf1), tree_node(leaf2)]
        t.edges = [tree_edge(t.nodes[0], t.nodes[1])]
        return [t]
    elif len(leaves) > 2:
        old_trees = enumerate_trees(leaves[:-1])
        new_leaf_name = leaves[-1]
        new_trees = []

        for old_tree in old_trees:
            for i in range(len(old_tree.edges)):
                new_tree = old_tree.copy()
                edge_to_split = new_tree.edges[i]
                old_node1, old_node2 = edge_to_split.nodes
                new_tree.edges.remove(edge_to_split)
                internal_node = tree_node(None)
                new_tree.nodes.append(internal_node)
                new_leaf_node = tree_node(new_leaf_name)
                new_tree.nodes.append(new_leaf_node)
                new_tree.edges.append(tree_edge(old_node1, internal_node))
                new_tree.edges.append(tree_edge(old_node2, internal_node))
                new_tree.edges.append(tree_edge(new_leaf_node, internal_node))
                new_trees.append(new_tree) 
        return new_trees

def newick_format(tree_in):
    tree = tree_in.copy()

    if len(tree.nodes) == 1:
        return "{};".format(tree.nodes[0])
    elif len(tree.nodes) == 2:
        return "({},{});".format(*tree.nodes)
    elif len(tree.nodes) > 2:
        for candidate_node in tree.nodes:
            if candidate_node.name is not None:
                continue
            adjacent_edges = [edge for edge in tree.edges if candidate_node in edge.nodes]
            adjacent_nodes = [node for edge in adjacent_edges for node in edge.nodes if node in edge.nodes and node is not candidate_node]
            adjacent_leaves = [node for node in adjacent_nodes if node.name is not None]
            if len(adjacent_leaves) == 2 or len(adjacent_leaves) == 3:
                leaf1, leaf2 = adjacent_leaves[0: 2]
                edges_to_cut = [edge for edge in adjacent_edges if leaf1 in edge.nodes or leaf2 in edge.nodes]
                candidate_node.name = "({},{})".format(leaf1, leaf2)
                tree.nodes.remove(leaf1)
                tree.nodes.remove(leaf2)
                for edge in edges_to_cut: tree.edges.remove(edge)
                return newick_format(tree)

def convert_string_to_list(taxa_string):
    leaves = taxa_string.split()
    return leaves

if __name__ == '__main__':
    leaves_str = "#paste dataset here"
    leaves = convert_string_to_list(leaves_str)
    trees = enumerate_trees(leaves)
    for tree in trees: 
        print(newick_format(tree))