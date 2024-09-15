"""
This module provides functions to represent different types of graph structures.
"""
class VersatileDigraph:
    '''Class for versatile digraph implementation'''
    def __init__(self):
        """Initialization"""
        self.nodes = {}
        self.edges = {}

    def add_edge(self, start_node_id, end_node_id, start_node_value=0,
                 end_node_value=0, edge_name=None, edge_weight=0):
        """Add an edge between two nodes."""
        if start_node_id not in self.nodes:
            self.add_node(start_node_id, start_node_value)
        if end_node_id not in self.nodes:
            self.add_node(end_node_id, end_node_value)
        if start_node_id not in self.edges:
            self.edges[start_node_id] = {}
        if edge_name is None:
            edge_name = f"{start_node_id}->{end_node_id}"
        # Check if the edge name already exists for the given start node
        if edge_name in self.edges[start_node_id]:
            raise ValueError(f"Edge name '{edge_name}' already exists for node '{start_node_id}'")
        self.edges[start_node_id][edge_name] = (end_node_id, edge_weight)
    def get_nodes(self):
        """Return a list of nodes in the graph."""
        return list(self.nodes.keys())
    def add_node(self, node_id, node_value=0):
        """Return a list of nodes in the graph."""
        if node_id not in self.nodes:
            self.nodes[node_id] = node_value
    def get_node_value(self, node_id):
        """Return the value of the node."""
        return self.nodes.get(node_id, None)
    def get_edge_weight(self, start_node, end_node):
        """Return the weight of the edge between two nodes."""
        if start_node in self.edges:
            for _, (dest, weight) in self.edges[start_node].items():
                if dest == end_node:
                    return weight
        return None
    def print_graph(self):
        """Print the graph as a output."""
        for node_id, node_value in self.nodes.items():
            print(f"Node {node_id} with value {node_value}")
        for start_node, edges in self.edges.items():
            for edge_name, (end_node, weight) in edges.items():
                print(f"Edge from {start_node} to {end_node} with weight {weight} and name {edge_name}")
