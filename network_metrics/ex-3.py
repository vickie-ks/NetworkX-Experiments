import networkx as nx

# Load the networks from files
collaboration_graph = nx.read_edgelist("collaboration.txt", nodetype=int, data=(('weight',float),))
conflict_graph = nx.read_adjlist("conflict.csv", delimiter=",")

# Calculate network metrics
collaboration_density = nx.density(collaboration_graph)
collaboration_avg_degree = sum(dict(collaboration_graph.degree()).values()) / len(collaboration_graph)
collaboration_clustering_coefficient = nx.average_clustering(collaboration_graph)
collaboration_avg_shortest_path = nx.average_shortest_path_length(collaboration_graph)

conflict_density = nx.density(conflict_graph)
conflict_avg_degree = sum(dict(conflict_graph.degree()).values()) / len(conflict_graph)
conflict_clustering_coefficient = nx.average_clustering(conflict_graph)
conflict_avg_shortest_path = nx.average_shortest_path_length(conflict_graph)

print("Collaboration Network Metrics:")
print("==============================")
print("Density:", collaboration_density)
print("Average Degree:", collaboration_avg_degree)
print("Clustering Coefficient:", collaboration_clustering_coefficient)
print("Average Shortest Path Length:", collaboration_avg_shortest_path)

print("\n\nConflict Network Metrics:")
print("=========================")
print("Density:", conflict_density)
print("Average Degree:", conflict_avg_degree)
print("Clustering Coefficient:", conflict_clustering_coefficient)
print("Average Shortest Path Length:", conflict_avg_shortest_path)


### Command to Run: python3 ex-3.py > output.txt