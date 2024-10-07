import heapq

def dijkstra(graph, start_node):
    distances = [float('inf')] * (len(graph) + 1)
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)
        if dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = dist + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances

def find_meet_point(graph, source, target):
    source_distances = dijkstra(graph, source)
    target_distances = dijkstra(graph, target)

    min_time = float('inf')
    meet_node = -1

    for i in range(1, len(graph)):
        if source_distances[i] < float('inf') and target_distances[i] < float('inf'):
            if source_distances[i] >= target_distances[i] and source_distances[i] < min_time:
                min_time = source_distances[i]
                meet_node = i
            elif source_distances[i] <= target_distances[i] and target_distances[i] < min_time:
                min_time = target_distances[i]
                meet_node = i
    return min_time, meet_node

input_file = open('Lab6/input2.txt', 'r')
output_file = open('Lab6/output2.txt', 'w')

num_nodes, num_edges = map(int, input_file.readline().strip().split())
graph = [[] for _ in range(num_nodes + 1)]

for _ in range(num_edges):
    u, v, w = map(int, input_file.readline().strip().split())
    graph[u].append((v, w))
source_node, target_node = map(int, input_file.readline().strip().split())

time_taken, meeting_node = find_meet_point(graph, source_node, target_node)
if meeting_node == -1:
    print("Impossible", file=output_file)
else:
    print("Time", time_taken, file=output_file)
    print("Node", meeting_node, file=output_file)

input_file.close()
output_file.close()
