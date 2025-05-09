import sys


def prim_mst(graph, V):
    # Key values to pick minimum weight edge
    key = [sys.maxsize] * V

    # To store MST parent nodes
    parent = [None] * V

    # Track if vertex is in MST
    mst_set = [False] * V

    # Start from vertex 0
    key[0] = 0
    parent[0] = -1  # Root node has no parent

    for _ in range(V):
        # Find the minimum key vertex not in MST
        min_key = sys.maxsize
        u = -1
        for v in range(V):
            if not mst_set[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        # Add selected vertex to MST
        mst_set[u] = True

        # Update keys of adjacent vertices
        for v in range(V):
            if 0 < graph[u][v] < key[v] and not mst_set[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Print the MST
    print("\nEdge \tWeight")
    total_weight = 0
    for i in range(1, V):
        print(f"{parent[i]} - {i} \t{key[i]}")
        total_weight += key[i]
    print(f"\nTotal Weight of MST: {total_weight}")


# --------------------------
# Main Program: User Inputs
# --------------------------

try:
    V = int(input("Enter the number of vertices: "))

    # Initialize adjacency matrix with zeros
    graph = [[0 for _ in range(V)] for _ in range(V)]

    E = int(input("Enter the number of edges: "))

    print("\nEnter each edge as: start_vertex end_vertex weight (0-based indexing)")
    for _ in range(E):
        while True:
            try:
                u, v, w = map(int, input("Edge: ").split())
                if 0 <= u < V and 0 <= v < V and w >= 0:
                    graph[u][v] = w
                    graph[v][u] = w  # Undirected graph
                    break
                else:
                    print(f"Invalid input. Please enter valid vertices (0 to {V - 1}) and non-negative weight.")
            except ValueError:
                print("Please enter three integers: u v w")

    # Run Prim's algorithm
    prim_mst(graph, V)

except ValueError:
    print("Invalid input. Please enter integer values only.")



"""
Enter the number of vertices: 5
Enter the number of edges: 7

Enter each edge as: start_vertex end_vertex weight (0-based indexing)
Edge: 0 1 2
Edge: 0 3 6
Edge: 1 2 3
Edge: 1 3 8
Edge: 1 4 5
Edge: 2 4 7
Edge: 3 4 9

Edge   Weight
0 - 1     2
1 - 2     3
0 - 3     6
1 - 4     5

Total Weight of MST: 16
"""