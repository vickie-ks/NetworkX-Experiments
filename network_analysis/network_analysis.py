import networkx as nx

G = nx.Graph()

with open('/1stNetworkUpload.txt', 'r') as file:
    for line in file:
        node_1, node_2, weight = map(int, line.split())
        if weight == 1:
            G.add_edge(node_1, node_2, weight=weight)

total_connections = dict(G.degree())

at_least_1_connection = [node for node, connections in total_connections.items() if connections >= 1]
at_least_5_connections = [node for node, connections in total_connections.items() if connections >= 5]

at_least_1_connection.sort()
at_least_5_connections.sort()

print("Nodes with at least 1 connection:", at_least_1_connection)
print("Nodes with at least 5 connections:", at_least_5_connections)

"""
Command to run: python3 ex-2.py > output.txt
"""