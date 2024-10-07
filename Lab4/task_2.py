class AdjNode():
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph():
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [None] * self.num_vertices

    def add_edge(self, source, destination):
        new_node = AdjNode(destination)
        if self.adj_list[source] is None:
            self.adj_list[source] = new_node
        else:
            last = self.adj_list[source]
            while last.next:
                last = last.next
            last.next = new_node

    def get_adjacency_list(self):
        adjacency_dict = {}
        for i in range(self.num_vertices):
            adjacency_dict[str(i)] = []
            current_node = self.adj_list[i]
            while current_node:
                adjacency_dict[str(i)].append(str(current_node.vertex))
                current_node = current_node.next
        return adjacency_dict

visited = []
queue = []

def bfs(visited, adjacency_list, start_node):
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        f2.write(str(current_node) + " ")

        for neighbor in adjacency_list[str(current_node)]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

txt = open('Lab4/Input2.txt', 'r')
f2 = open("Lab4/Output2.txt", "w")
first_line = txt.readline().strip()
first_line = first_line.split(' ')
num_vertices = int(first_line[0])
num_edges = int(first_line[1])

g = Graph(num_vertices + 1)
for i in range(num_edges):
    temp = txt.readline().strip().split(' ')
    source = int(temp[0])
    destination = int(temp[1])
    g.add_edge(source, destination)

adjacency_list = g.get_adjacency_list()
bfs(visited, adjacency_list, '1')