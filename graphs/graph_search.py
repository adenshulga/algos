from collections import deque
# from queue import Queue
# 4 4
# 1 2 1
# 2 3 2
# 3 4 5
# 4 1 4

edges_list = [(0, 1),
(0, 2),
(2, 3),
(2, 4),
(3, 5),
(4, 5),]



graph = {
    0 : [1,2],
    1 : [0],
    2 : [0,3,4],
    3 : [2,5],
    4 : [2,5],
    5 : [3,4]
}



def BFS(graph: dict[list]):
    '''
    Метод Винни-Пуха, пойдем сначала к соседям, потом к соседям соседей

    мы всех посещаем по очереди, в очередь складываем соседей вершины в которой стоим

    если были в этой вершине, то ничего не делаем, если не было, кладем всех соседей в очередь

    сложность: O(V + E) если через список смежности, так как надо посмтореть всех соседей у всех
    '''

    v = len(graph)

    dist = [None for _ in range(v)]
    parent = [None for _ in range(v)]

    # been_here = [[0 for _ in range(v)] for _ in range(v)]

    start_index = next(iter(graph))
    dist[start_index] = 0
    parent[start_index] = start_index

    queue = deque()
    queue.append(start_index)
    # been_here[start_index][start_index] = 0

    while queue:
        vertice = queue.popleft()
        neighbours = graph[vertice]
        for neighb in neighbours:
            if dist[neighb] is None:
                queue.append(neighb)
                dist[neighb] = dist[vertice] + 1
                parent[neighb] = vertice

    return dist, parent

def weighted_BFS(graph: ... ):
    pass

print(graph)

dist, parent = BFS(graph)
print(dist)
print(parent)


def DFS():
    pass















