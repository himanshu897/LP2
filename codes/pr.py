import heapq

def dj(graph,start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = [(0,start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_dist > distances[current_node]:
            continue

        for neighbor,weight in graph[current_node].items():
            distance = current_dist + weight

            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(queue(distance,neighbor))

    return distances

def create_graph():
    graph = {}
    vertex_count = int(input("Enter no of vertices: "))
    for i in range(vertex_count):
        vertex = input("Enter vertex: ")
        neighor_count = int(input("Enter the no of neigbhors: "))
        neighbors = {}
        for j in range(neighor_count):
            neighbor = input("Enter the number : ")
            cost = int(input("cost: "))
            neighbors[neighbor] = cost
        graph[vertex]=neighbors

    return graph

graph = create_graph()
start=input("Starting node: ")

dist=dj(graph,start)
print(dist)


