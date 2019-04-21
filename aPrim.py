import random

class GraphM :

    def __init__ (self, n, g):
        self.matrix = []
        for i in range (n):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append(0)
        for i in range(n):
            for j in range(i+1, n):
                if random.random() < (g/100):
                    self.matrix[i][j] = random.randint(1,1000)
                    self.matrix[j][i] = self.matrix[i][j]


    def __str__(self):
        out = ""
        for i in range (len(self.matrix)):
            pom = ""
            for j in range(len(self.matrix)):
                pom = pom + str(self.matrix[i][j]) + " "
            out = out + "\n" + pom
        return out

    def prim (self, start):
        VMST = [start]
        EMST = []
        edges = []
        for i in range(len(self.matrix)):
            if self.matrix[start][i] != 0:
                edges.append(Edge(start, i, self.matrix[start][i]))
        while len(EMST) < len(self.matrix)-1:

            E = Edge()
            count = 0
            while count < len(edges):
                if edges[count].x in VMST and edges[count].y in VMST:
                    edges.remove(edges[count])
                else:
                    if edges[count].val < E.val:
                        E = edges[count]
                    count +=1


            if not edges:
                break

            edges.remove(E)
            VMST.append(E.y)
            EMST.append(E)

            for i in range(len(self.matrix)):
                if self.matrix[E.y][i] != 0:
                    edges.append(Edge(E.y, i, self.matrix[E.y][i]))
        return EMST



class Edge:
    def __init__(self,x = -1 ,y =-1 , val = 9999):
        self.x = x
        self.y = y
        self.val = val

    def __str__(self):
        out =  "[("+str(self.x) + "," + str(self.y)+");"  + str(self.val) + "]"
        return out

class dEdge:
    def __init__(self ,y =-1 , val = 9999):
        self.y = y
        self.val = val
    def __str__(self):
        out =  "[(" + str(self.y)+");"  + str(self.val) + "]"
        return out


class GraphL:
    def __init__ (self, matrix):
        self.list = []
        l = len(matrix.matrix)
        for  i in range(l):
            self.list.append([])
            for j in range(l):
                val = matrix.matrix[i][j]
                if  val != 0:
                   self.list[i].append(dEdge(j, val))

    def __str__(self):
        l = len(self.list)
        out = ""
        for i in range (l):
            pom = str(i)+ ":  "
            li = len(self.list[i])
            for j in range(li):
                pom = pom + str(self.list[i][j]) + " "
            out = out + "\n" + pom
        return out

    def prim(self, start):
        VMST = [start]
        EMST = []
        edges = []
        for i in range(len(self.list[start])):
                edges.append(Edge(start, self.list[start][i].y, self.list[start][i].val))
        while len(EMST) < len(self.list) - 1:
            E = Edge()
            count = 0
            while count < len(edges):
                if edges[count].x in VMST and edges[count].y in VMST:
                    edges.remove(edges[count])
                else:
                    if edges[count].val < E.val:
                        E = edges[count]
                    count += 1

            if not edges:
                break
            edges.remove(E)
            VMST.append(E.y)
            EMST.append(E)
            for i in range(len(self.list[E.y])):
                    edges.append(Edge(E.y, self.list[E.y][i].y, self.list[E.y][i].val))
        return EMST


HelloWorld = GraphM(10,30)
print(HelloWorld)
HelloWorldL = GraphL(HelloWorld)
print(HelloWorldL)


print("Macierz")
out = HelloWorld.prim(0)
for i in out:
    print(i)

print("Lista")

out = HelloWorldL.prim(0)
for i in out:
    print(i)
