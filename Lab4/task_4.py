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
        if self.graph[source] == None:
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
            current_node = self.graph[i]
            while current_node:
                adjacency_dict[i].append(current_node.vertex)
                current_node = current_node.next
        self.graph = adjacency_dict

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.is_cyclic_util(neighbour, visited, rec_stack) == True:
                    return True
            elif rec_stack[neighbour] == True:
                return True
        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * (self.num_vertices + 1)
        rec_stack = [False] * (self.num_vertices + 1)
        for node in range(self.num_vertices):
            if visited[node] == False:
                if self.is_cyclic_util(node, visited, rec_stack) == True:
                    return True
        return False

f1 = open('Lab4/Input4.txt', 'r')
f2 = open('Lab4/Output4.txt', 'w')
first_line = f1.readline().strip()
first_line = first_line.split(' ')
num_vertices = int(first_line[0])
num_edges = int(first_line[1])

g = Graph(num_vertices + 1)
for i in range(num_edges):
    temp = f1.readline().strip().split(' ')
    source = int(temp[0])
    destination = int(temp[1])
    g.add_edge(source, destination)

g.prepare_adjacency_list()
if g.is_cyclic():
    print("YES", file=f2)
else:
    print("NO", file=f2)