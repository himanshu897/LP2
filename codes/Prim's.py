def prim(graph, start):
    mst = []  # minimum spanning tree
    visited = set([start])
    edges = [
        (cost, start, to)
        for to, cost in graph[start].items()
    ]
    edges.sort()
    while edges:
        cost, frm, to = edges.pop(0)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    edges.append((cost, to, to_next))
            edges.sort()
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
        start = input("Enter the starting vertex: ")
        mst = prim(graph, start)
        print("Minimum Spanning Tree:")
        for edge in mst:
            print(edge)
        print()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.\n")
