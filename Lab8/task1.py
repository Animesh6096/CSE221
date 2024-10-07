import heapq

total_cost = 0

def add_edge(parents, u, v, w):
    global total_cost
    if find_parent(parents, u) != find_parent(parents, v):
        total_cost += w
    parents[find_parent(parents, v)] = find_parent(parents, u)

def find_parent(parents, u):
    if u == parents[u]:
        return u
    parents[u] = find_parent(parents, parents[u])
    return parents[u]

input_file = open('Lab8/input1.txt', 'r')
output_file = open('Lab8/output1.txt', 'w')

n, m = map(int, input_file.readline().strip().split())
parents = [i for i in range(n+1)]
edges = []

for i in range(m):
    u, v, w = map(int, input_file.readline().strip().split())
    heapq.heappush(edges, (w, u, v))
while edges:
    w, u, v = heapq.heappop(edges)
    add_edge(parents, u, v, w)
print(total_cost, file=output_file)
