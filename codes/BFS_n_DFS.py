n = int(input("Enter no of elements: "))
l={}
root =0 
for i in range(n):
    if(i==0):
        root=input("Enter the start element: ")
        l[root]=[]
        m=int(input("Enter no of adjacent node: "))
        for j in range(m):
            print("Enter the node",j+1,":")
            a=input()
            l[root].append(a)
    else:
        x=input("Enter the another element: ")
        l[x]=[]
        m=int(input("Enter no of adjacent node: "))
        for j in range(m):
            print("Enter the node",j+1,":")
            a=input()
            l[x].append(a)


visited = set()
queue = []


def bfs(graph,node):
    visited.add(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m,end = " ")

        for neighour in graph[m]:
            if neighour not in visited:
                visited.add(neighour)
                queue.append(neighour)

def dfs(graph,node):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        for neighours in graph[node]:
            dfs(visited,graph,neighours)

while(True):

    print("****************** MENU ********************")
    p=int(input("Enter 1 for BFS , 2 for DFS : "))
    if p == 1:
        print("BFS: ")
        bfs(l,root)
    elif p == 2:
        print("DFS : ")
        dfs(l,root)
    else :
        print("invalid input")

