import networkx as nx
import numpy as np

def load_network(filename):
    """Load network from a text file."""
    G = nx.Graph()
    with open(filename, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            node1, node2, _ = line.strip().split('\t')
            G.add_edge(node1, node2)
    return G

def calculate_metrics(G):
    """Calculate various network metrics."""
    metrics = {}

    # Degree centrality
    degree_centrality = nx.degree_centrality(G)
    metrics['Degree Centrality'] = degree_centrality

    # Betweenness centrality
    betweenness_centrality = nx.betweenness_centrality(G)
    metrics['Betweenness Centrality'] = betweenness_centrality

    # Clustering coefficient
    clustering_coefficient = nx.clustering(G)
    metrics['Clustering Coefficient'] = clustering_coefficient

    # Density of the overall network
    density = nx.density(G)
    metrics['Density'] = density

    # Average Degree
    avg_degree = np.mean([val for _, val in degree_centrality.items()])
    metrics['Average Degree'] = avg_degree

    # Check if the graph is connected before calculating average shortest path length
    if nx.is_connected(G):
        # Average shortest path length
        avg_shortest_path_length = nx.average_shortest_path_length(G)
        metrics['Average Shortest Path Length'] = avg_shortest_path_length
    else:
        metrics['Average Shortest Path Length'] = 'Graph is not connected'

    # Average Clustering
    avg_clustering = nx.average_clustering(G)
    metrics['Average Clustering'] = avg_clustering

    # Local efficiency
    local_efficiency = nx.local_efficiency(G)
    metrics['Local Efficiency'] = local_efficiency

    # Global efficiency
    global_efficiency = nx.global_efficiency(G)
    metrics['Global Efficiency'] = global_efficiency

    return metrics


if __name__ == "__main__":
    # Load networks
    network1_file = 'confl1.txt'
    network2_file = 'coop1.txt'
    network1 = load_network(network1_file)
    network2 = load_network(network2_file)

    # Calculate metrics for both networks
    metrics_network1 = calculate_metrics(network1)
    metrics_network2 = calculate_metrics(network2)

    # Display metrics for network 1
    print("Metrics for Network 1:")
    for metric, value in metrics_network1.items():
        print(f"{metric}: {value}")

    # Display metrics for network 2
    print("\nMetrics for Network 2:")
    for metric, value in metrics_network2.items():
        print(f"{metric}: {value}")
