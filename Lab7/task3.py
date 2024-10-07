def add_edge(parents, sizes, u, v):
    if find_parent(parents, u) != find_parent(parents, v):
        sizes[find_parent(parents, u)] += sizes[find_parent(parents, v)]
    
    parents[find_parent(parents, v)] = find_parent(parents, u)

def find_parent(parents, u):
    if u == parents[u]:
        return u
    parents[u] = find_parent(parents, parents[u])
    return parents[u]

input_file = open('Lab7/input3.txt', 'r')
output_file = open('Lab7/output3.txt', 'w')

n, k = map(int, input_file.readline().strip().split())
parents = [i for i in range(n + 1)]
sizes = [1] * (n + 1)

for _ in range(k):
    u, v = map(int, input_file.readline().strip().split())
    add_edge(parents, sizes, u, v)
    print(sizes[find_parent(parents, u)], file=output_file)
