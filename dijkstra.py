from queue import PriorityQueue

graph = {
    "matrix": [
        [0, 4, 0, 0, 0, 0, 7, 0, 0],
        [4, 0, 9, 0, 0, 0, 11, 20, 0],
        [0, 9, 0, 6, 2, 0, 0, 0, 0],
        [0, 0, 6, 0, 10, 5, 0, 0, 0],
        [0, 0, 2, 10, 0, 15, 0, 1, 5],
        [0, 0, 0, 5, 15, 0, 0, 0, 12],
        [7, 11, 0, 0, 0, 0, 0, 1, 0],
        [0, 20, 0, 0, 1, 0, 1, 0, 3],
        [0, 0, 0, 0, 5, 12, 0, 3, 0]
    ],
    "nodes": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'E', 'F']
}


def neighbors(node, matrix):
    adjacents_nodes = list()
    for i in range(len(matrix[node])):
        adjacent_node = i
        if matrix[node][adjacent_node] != 0:
            adjacents_nodes.append(adjacent_node)
    return adjacents_nodes


def weight_nodes(nodeA, nodeB, matrix):
    return matrix[nodeA][nodeB]


def dijkstra(graph, root):
    graphMatrix = graph["matrix"]
    nodesLabel = graph["nodes"]
    # initialization
    pq = PriorityQueue()
    dist = [float('inf') for i in range(len(nodesLabel))]
    parent = [None for i in range(len(nodesLabel))]
    dist[root] = 0
    pq.put((0, root))

    while not pq.empty():
        d, node = pq.get()  # extract node with the smallest distance from the root
        for neighbor in neighbors(node, graphMatrix):
            weight = weight_nodes(node, neighbor, graphMatrix)
            if dist[node] + weight < dist[neighbor]:  # relax neighbor
                dist[neighbor] = dist[node] + weight
                parent[neighbor] = node
                pq.put((dist[neighbor], neighbor))

    #print(nodesLabel, end="\n")
    print(dist, parent)
    # display the shortest path from root to node
    nodes_dest = 7
    node = nodes_dest
    while node != root:
        print(node)
        node = parent[node]

dijkstra(graph, 0)
