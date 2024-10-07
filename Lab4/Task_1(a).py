class Graph():
    def __init__(self,size):
        self.adjMatrix=[]
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size=size

    def add_edge(self,v1,v2,w):
        if v1==v2:
            print("Same vertex",file=f2)
        self.adjMatrix[v1][v2]=w
    
    def print_matrix(self):
        for i in range(self.size):
            for a in range(self.size):
                f2.write(str(self.adjMatrix[i][a]))
            f2.write("\n")


f1 = open('Lab4\Input1a.txt','r')
f2 = open("Lab4\Output1a.txt","w")
x = (f1.readline()).strip()
n = int(x[0]) # matrix size +1
m = int(x[2]) #number of iteration 

g = Graph(n+1)
for i in range(m):
  temp = (f1.readline()).strip()
  temp = temp.split(' ')
  g.add_edge(int(temp[0]),int(temp[1]),int(temp[2]))
g.print_matrix()