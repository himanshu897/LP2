class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_safe(self, v, color, c):
        for i in range(self.vertices):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_color_util(self, m, color, v):
        if v == self.vertices:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_color_util(m, color, v + 1):
                    return True
                color[v] = 0

    def graph_coloring(self, m):
        color = [0] * self.vertices
        if not self.graph_color_util(m, color, 0):
            return False

        print("Graph coloring possible using at most", m, "colors.")
        print("Color assignments:")
        for i in range(self.vertices):
            print("Vertex", i, ":", color[i])
        return True


def create_graph():
    num_vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(num_vertices)
    print("Enter the adjacency matrix (0 for no edge, 1 for an edge):")
    for i in range(num_vertices):
        row = list(map(int, input().split()))
        g.graph[i] = row
    return g


def menu():
    print("Menu:")
    print("1. Create a graph")
    print("2. Perform graph coloring")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    return choice


def main():
    g = None
    while True:
        choice = menu()

        if choice == 1:
            g = create_graph()
        elif choice == 2:
            if g is None:
                print("Create a graph first!")
            else:
                num_colors = int(input("Enter the number of colors to use: "))
                g.graph_coloring(num_colors)
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == '__main__':
    main()
