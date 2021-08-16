from collections import deque
 
class Graph:
    def __init__(self, edges, N):
        self.adjList = [[] for _ in range(N)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
def BFS(graph, v, discovered):
    q = deque()
    discovered[v] = True
 
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for u in graph.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)
 
 
if __name__ == '__main__':
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vertex 0, 13, and 14 are single nodes
    ]
 
    N = 15
 
    graph = Graph(edges, N)
 
    discovered = [False] * N

    for i in range(N):
        if not discovered[i]:
            BFS(graph, i, discovered)