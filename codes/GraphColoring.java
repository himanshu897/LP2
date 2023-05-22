import java.util.Scanner;

public class GraphColoring {
    private int V;
    private boolean[][] graph;
    private int[] color;

    public GraphColoring(int V) {
        this.V = V;
        this.graph = new boolean[V][V];
        this.color = new int[V];
    }

    public void createGraph() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of vertices in the graph: ");
        V = scanner.nextInt();

        graph = new boolean[V][V];

        System.out.println("Enter the adjacency matrix (0 for no edge, 1 for an edge):");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                graph[i][j] = scanner.nextInt() == 1;
            }
        }
    }

    public void graphColoring() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of colors to use: ");
        int m = scanner.nextInt();

        for (int i = 0; i < V; i++) {
            color[i] = 0;
        }

        if (graphColoringUtil(m, 0)) {
            System.out.println("Graph coloring possible using at most " + m + " colors.");
            System.out.println("Color assignments:");
            for (int i = 0; i < V; i++) {
                System.out.println("Vertex " + i + ": " + color[i]);
            }
        } else {
            System.out.println("Graph coloring not possible using " + m + " colors.");
        }
    }

    private boolean graphColoringUtil(int m, int v) {
        if (v == V) {
            return true;
        }

        for (int c = 1; c <= m; c++) {
            if (isSafe(v, c)) {
                color[v] = c;
                if (graphColoringUtil(m, v + 1)) {
                    return true;
                }
                color[v] = 0;
            }
        }
        return false;
    }

    private boolean isSafe(int v, int c) {
        for (int i = 0; i < V; i++) {
            if (graph[v][i] && color[i] == c) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        GraphColoring graphColoring = null;
        int choice;

        while (true) {
            System.out.println("Menu:");
            System.out.println("1. Create a graph");
            System.out.println("2. Perform graph coloring");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    graphColoring = new GraphColoring(0);
                    graphColoring.createGraph();
                    break;
                case 2:
                    if (graphColoring == null) {
                        System.out.println("Create a graph first!");
                    } else {
                        graphColoring.graphColoring();
                    }
                    break;
                case 3:
                    System.out.println("Exiting...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice! Try again.");
            }
        }
    }
}
