import networkx as nx
import matplotlib.pyplot as plt

# Function to create a NetworkX graph from the data in the provided text file
def create_graph_from_txt(filename):
    # Create an empty directed graph
    G = nx.DiGraph()
    
    # Read the data from the text file
    with open(filename, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            # Split the line into source, target, and weight
            source, target, weight = line.strip().split('\t')
            # Add edges to the graph
            G.add_edge(source, target, weight=int(weight))
    
    return G

# File paths for the two networks
file1 = "confl1.txt"
file2 = "coop1.txt"

# Create NetworkX graph objects for each network
network1 = create_graph_from_txt(file1)
network2 = create_graph_from_txt(file2)

# Plot the first network
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
nx.draw(network1, with_labels=True, node_color='skyblue', node_size=500, font_size=8, arrowsize=10)
plt.title("Network 1")

# Plot the second network
plt.subplot(1, 2, 2)
nx.draw(network2, with_labels=True, node_color='lightcoral', node_size=500, font_size=8, arrowsize=10)
plt.title("Network 2")

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()
