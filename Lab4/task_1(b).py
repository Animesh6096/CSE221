class AdjNode():
    def __init__(self, value, weight):
        self.vertex = value
        self.next = None
        self.weight = weight

class Graph():
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination, weight):
        new_node = AdjNode(destination, weight)
        if self.graph[source] is None:
            self.graph[source] = new_node
        else:
            last = self.graph[source]
            while last.next:
                last = last.next
            last.next = new_node

    def print_graph(self):
        for i in range(self.V):
            f2.write(str(i) + " :")
            temp = self.graph[i]
            while temp:
                f2.write(str((temp.vertex, temp.weight)))
                temp = temp.next
            f2.write("\n")

f1 = open('Lab4\Input1a.txt', 'r')
f2 = open('Lab4\Output1b.txt', 'w')
first_line = f1.readline().strip()
first_line = first_line.split(' ')
num_vertices = int(first_line[0])
num_edges = int(first_line[1])

g = Graph(num_vertices + 1)
for i in range(num_edges):
    temp = f1.readline().strip().split(' ')
    source = int(temp[0])
    destination = int(temp[1])
    weight = int(temp[2])
    g.add_edge(source, destination, weight)
    
g.print_graph()