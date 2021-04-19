import heapq

mygraph = {
    'A': {'B': 1, 'C': 6},
    'B': {'C': 3, 'D': 2},
    'C': {'E': 5, 'F': 9},
    'D': {'E': 8},
    'E': {},
    'F': {'A': 10}
}

def dijkstra(graph, start):
    dists = {node: float('inf') for node in graph}
    dists[start] = 0
    queue = []
    heapq.heappush(queue, [dists[start], start])

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        if dists[cur_node] < cur_dist:
            continue

        for adj, weight in graph[cur_node].items():
            dist = cur_dist + weight

            if dist < dists[adj]:
                dists[adj] = dist
                heapq.heappush(queue, [dist, adj])

        print(dists)
    return dist

dijkstra(mygraph, 'A')