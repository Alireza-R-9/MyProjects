import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph, pos, path=None):
    plt.figure(figsize=(12, 8))
    node_colors = []
    node_sizes = []
    labels = {}

    for node in graph.nodes:
        # Create labels with node numbers
        labels[node] = f"{node} ({graph.nodes[node].get('label', '')})"

        if graph.nodes[node].get('label') == 'Router':
            node_colors.append('red')
            node_sizes.append(1000)
        else:
            node_colors.append('skyblue')
            node_sizes.append(700)

    nx.draw(graph, pos, with_labels=True, labels=labels, node_color=node_colors, node_size=node_sizes,
            edge_color='gray')

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='r', width=2)

    edge_labels = nx.get_edge_attributes(graph, 'label')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.show()


def calculate_path_metrics(graph, path):
    total_weight = 0
    total_delay = 0
    for i in range(len(path) - 1):
        edge_data = graph.get_edge_data(path[i], path[i + 1])
        total_weight += edge_data['weight']
        total_delay += edge_data['delay']
    return total_weight, total_delay


# Get the number and type of topologies from the user
num_topologies = int(input("Enter the number of topologies: "))

graph = nx.Graph()
router_id = 0
graph.add_node(router_id, label='Router')

for topology_index in range(num_topologies):
    topology_type = input(f"Enter the type of topology {topology_index + 1} (bus/star/ring/mesh): ").strip().lower()
    if topology_type == 'bus':
        # Create bus topology
        nodes = int(input("Enter the number of nodes in the bus: "))
        start_index = len(graph.nodes)
        for i in range(start_index, start_index + nodes):
            graph.add_node(i)
            if i > start_index:
                graph.add_edge(i, i - 1, weight=1, delay=1, bandwidth=10, label='W:1 D:1 B:10')
        graph.add_edge(router_id, start_index, weight=1, delay=1, bandwidth=10, label='W:1 D:1 B:10')
    elif topology_type == 'star':
        # Create star topology
        nodes = int(input("Enter the number of nodes in the star: "))
        start_index = len(graph.nodes)
        for i in range(start_index + 1, start_index + nodes):
            graph.add_node(i)
            graph.add_edge(start_index, i, weight=1, delay=1, bandwidth=10, label='W:1 D:1 B:10')
        graph.add_edge(router_id, start_index, weight=1, delay=1, bandwidth=10, label='W:1 D:1 B:10')
    elif topology_type == 'ring':
        # Create ring topology
        nodes = int(input("Enter the number of nodes in the ring: "))
        start_index = len(graph.nodes)
        for i in range(start_index, start_index + nodes):
            graph.add_node(i)
            if i > start_index:
                graph.add_edge(i, i - 1, weight=1, delay=1, bandwidth=10, label='W:1 D:1 B:10')
        graph.add_edge(start_index, start_index + nodes - 1, weight=1, delay=1, bandwidth=10, label='W:1 D:1 B:10')
        graph.add_edge(router_id, start_index, weight=1, delay=1, bandwidth=10, label='W:1 D:1 B:10')
    elif topology_type == 'mesh':
        # Create mesh topology
        nodes = int(input("Enter the number of nodes in the mesh: "))
        start_index = len(graph.nodes)
        for i in range(start_index, start_index + nodes):
            graph.add_node(i)
            for j in range(start_index, i):
                graph.add_edge(i, j, weight=1, delay=1, bandwidth=10, label='W:1 D:1 B:10')
        graph.add_edge(router_id, start_index, weight=1, delay=1, bandwidth=10, label='W:1 D:1 B:10')

    # Draw the graph after adding each topology
    pos = nx.spring_layout(graph)  # determine node positions
    draw_graph(graph, pos)

# Display the list of nodes to the user
print("List of nodes in the graph: ", list(graph.nodes))

# Get the message type from the user
message_type = input("Enter the type of message to be sent (data/voice/video): ").strip().lower()

# Determine the routing criteria based on the message type
if message_type == 'data':
    importance = 'weight'
elif message_type == 'voice':
    importance = 'delay'
elif message_type == 'video':
    importance = 'bandwidth'
else:
    importance = 'weight'

# Get the source and destination nodes from the user
start_node = int(input("Enter the source node: "))
end_node = int(input("Enter the destination node: "))

# Calculate the best path based on the message type
if importance == 'weight':
    path = nx.dijkstra_path(graph, start_node, end_node, weight='weight')
elif importance == 'delay':
    path = nx.dijkstra_path(graph, start_node, end_node, weight='delay')
else:
    path = nx.dijkstra_path(graph, start_node, end_node, weight='bandwidth')

# Calculate total weight and delay for the chosen path
total_weight, total_delay = calculate_path_metrics(graph, path)

# Display the results to the user
print(f"The best path from {start_node} to {end_node} for {message_type} message: {path}")
print(f"Total path weight: {total_weight}")
print(f"Total path delay: {total_delay} ms")

# Visualize the graph with the chosen path
draw_graph(graph, pos, path)
