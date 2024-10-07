def depth_first_search(graph, vertex, visited, stack):
    visited[vertex] = True

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            depth_first_search(graph, neighbor, visited, stack)

    stack.append(vertex)


def transpose_graph(graph):
    transposed = {vertex: [] for vertex in graph}
    for vertex in graph:
        for neighbor in graph[vertex]:
            transposed[neighbor].append(vertex)

    return transposed


def depth_first_search_scc(graph, vertex, visited, scc):
    visited[vertex] = True
    scc.append(vertex)

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            depth_first_search_scc(graph, neighbor, visited, scc)


def strongly_connected_components(num_vertices, edges):
    graph = {vertex: [] for vertex in range(1, num_vertices + 1)}
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * (num_vertices + 1)
    stack = []

    for vertex in range(1, num_vertices + 1):
        if not visited[vertex]:
            depth_first_search(graph, vertex, visited, stack)

    transposed_graph = transpose_graph(graph)
    visited = [False] * (num_vertices + 1)
    result = []

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            scc = []
            depth_first_search_scc(transposed_graph, vertex, visited, scc)
            result.append(scc)

    return result

def print_strongly_connected_components(components):
    for component in components:
        print(*component, file=output_file)

input_file = open('Lab5/input3.txt', 'r')
output_file = open('Lab5/output3.txt', 'w')

num_vertices, num_edges = map(int, input_file.readline().strip().split())

edges_list = []
for i in range(num_edges):
    edge_tuple = tuple(map(int, input_file.readline().strip().split()))
    edges_list.append(edge_tuple)

result = strongly_connected_components(num_vertices, edges_list)
print_strongly_connected_components(result)
