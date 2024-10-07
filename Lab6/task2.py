import heapq

def shortest_path(g, s):
    d = [float('inf')] * (len(g) + 1)
    d[s] = 0
    pq = [(0, s)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > d[node]:
            continue

        for nbr, w in g[node]:
            new_dist = dist + w
            if new_dist < d[nbr]:
                d[nbr] = new_dist
                heapq.heappush(pq, (new_dist, nbr))

    return d

def meeting_point(g, s, t):
    ad = shortest_path(g, s)
    bd = shortest_path(g, t)

    min_time = float('inf')
    meet_node = -1

    for i in range(1, len(g)):
        if ad[i] < float('inf') and bd[i] < float('inf'):
            if ad[i] >= bd[i] and ad[i] < min_time:
                min_time = ad[i]
                meet_node = i
            elif ad[i] <= bd[i] and bd[i] < min_time:
                min_time = bd[i]
                meet_node = i
    return min_time, meet_node

inp = open('Lab6/input2.txt', 'r')
out = open('Lab6/output2.txt', 'w')

n, m = map(int, inp.readline().strip().split())
g = [[] for i in range(n + 1)]

for i in range(m):
    u, v, w = map(int, inp.readline().strip().split())
    g[u].append((v, w))
s, t = map(int, inp.readline().strip().split())

time, i = meeting_point(g, s, t)
if i == -1:
    print("Impossible", file=out)
else:
    print("Time", time, file=out)
    print("Node", i, file=out)
