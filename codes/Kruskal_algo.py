def kruskal(graph):
    mst = []  # minimum spanning tree
    visited2 = set()  # for storing visited elements for cycle checking
    visited = []
    edges = []
    for node in graph.keys():
        visited.append(node)
        for to, cost in graph[node].items():
            if to not in visited:
                edges.append((cost, node, to))
    edges.sort()
    i = 0
    while i < len(edges):
        cost, frm, to = edges[i]
        if frm not in visited2 or to not in visited2:  # if one of the nodes is not in visited2, they will not form a cycle
            mst.append((frm, to, cost))
            visited2.add(frm)
            visited2.add(to)
        i += 1
    return mst


def create_graph():
    graph = {}
    vertex_count = int(input("Enter the number of vertices: "))
    for i in range(vertex_count):
        vertex = input("Enter vertex: ")
        neighbors_count = int(input(f"Enter the number of neighbors for vertex {vertex}: "))
        neighbors = {}
        for j in range(neighbors_count):
            neighbor = input(f"Enter neighbor {j+1}: ")
            cost = int(input(f"Enter cost for the edge ({vertex} - {neighbor}): "))
            neighbors[neighbor] = cost
        graph[vertex] = neighbors
    return graph


while True:
    print("1. Find Minimum Spanning Tree")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        graph = create_graph()
        mst = kruskal(graph)
        print("Minimum Spanning Tree:")
        for edge in mst:
            print(edge)
        print()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.\n")
