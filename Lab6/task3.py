import heapq

def shortest_max_weight(graph, start, dest):
    dist = [float('inf')] * (len(graph) + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)
        if node == dest:
            return d

        for nb, wt in graph[node]:
            new_d = max(d, wt)
            if new_d < dist[nb]:
                dist[nb] = new_d
                heapq.heappush(pq, (new_d, nb))

    return -1

inp = open('Lab6/input3.txt', 'r')
out = open('Lab6/output3.txt', 'w')

n, m = map(int, inp.readline().strip().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, inp.readline().strip().split())
    graph[u].append((v, w))

min_danger = shortest_max_weight(graph, 1, n)

if min_danger == -1:
    print("Impossible", file=out)
else:
    print(min_danger, file=out)

inp.close()
out.close()
