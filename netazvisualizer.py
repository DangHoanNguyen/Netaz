import json
from graphviz import Digraph
import sys


def construct_graph_json(file):
    data = []
    nodes = []
    edges = []
    with open(file, "r") as fin:
        data = json.load(fin)

    for segment in data:

        # Constructing nodes
        node_s = {
            "id": segment["sip"],
            "label": segment["sip"],
        }
        node_d = {
            "id": segment["dip"],
            "label": segment["dip"],
        }
        if node_s not in nodes:
            nodes.append(node_s)

        if node_d not in nodes:
            nodes.append(node_d)

        # Constructing edges
        edge = {
            "source": segment["sip"],
            "target": segment["dip"],
            "description": segment["protocol"],
        }
        edges.append(edge)

    return nodes, edges


def main(file):

    nodes, edges = construct_graph_json(file)
    dot = Digraph()

    for node in nodes:
        dot.node(node["id"], label=node["label"])
    
    for edge in edges:
        dot.edge(edge["source"], edge["target"], label=edge["description"])
    
    dot.render("graph_output", format="png", cleanup=True)
    
    print("Graph created and saved as 'graph_output.png'")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 netazvisualizer.py <logdata.json>")
        sys.exit(1)
    main(sys.argv[1])
