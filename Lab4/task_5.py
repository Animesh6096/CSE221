class AdjNode():
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph():
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [None] * self.num_vertices

    def add_edge(self, source, destination):
        new_node = AdjNode(destination)
        if self.graph[source] is None:
            self.graph[source] = new_node
        else:
            last = self.graph[source]
            while last.next:
                last = last.next
            last.next = new_node

    def prepare_adjacency_list(self):
        adjacency_dict = {}
        for i in range(self.num_vertices):
            adjacency_dict[i] = []
            temp = self.graph[i]
            while temp:
                adjacency_dict[i].append(temp.vertex)
                temp = temp.next
        self.graph = adjacency_dict
        return self.graph

def breadth_first_search_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        new_path = [1]
        print("Shortest path =", *new_path, file=f2)
        return new_path

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    print("Shortest path =", *new_path, file=f2)
                    return new_path
            explored.append(node)

    print("Path doesn't exist", file=f2)

f1 = open('Lab4\Input5.txt', 'r')
f2 = open('Lab4\Output5.txt', 'w')
first_line = f1.readline().strip()
first_line = first_line.split(' ')
num_vertices = int(first_line[0])
num_edges = int(first_line[1])
goal_node = int(first_line[2])

g = Graph(num_vertices + 1)
for i in range(num_edges):
    temp = f1.readline().strip().split(' ')
    source = int(temp[0])
    destination = int(temp[1])
    g.add_edge(source, destination)

graph = g.prepare_adjacency_list()
size = breadth_first_search_shortest_path(graph, 1, goal_node)
print("Time:", len(size) - 1, file=f2)