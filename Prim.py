import random
import time
import heapq

class Edge:
    def __init__(self,x = -1 ,y =-1 , val = 9999):
        self.val = val
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        out =  "[("+str(self.x) + "," + str(self.y)+");"  + str(self.val) + "]"
        return out


class dEdge:
    def __init__(self ,y =-1 , val = 9999):
        self.val = val
        self.y = y

    def __str__(self):
        out =  "[(" + str(self.y)+");"  + str(self.val) + "]"
        return out

    def __lt__(self, other):
        return self.val < other.val


class Node:

    def __init__(self, val = 0):

        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def search(self, val):
        if val < self.val:
            if self.left is None:
                return 0
            return self.left.search(val)
        elif val > self.val:
            if self.right is None:
                return 0
            return self.right.search(val)
        else:
            return 1

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

    def prim(self, start):
        VMST = Node(start)
        EMST = []
        edges = []
        for i in range(len(self.matrix)):
            if self.matrix[start][i] != 0:
                heapq.heappush(edges, Edge(start, i, self.matrix[start][i]))
        while len(EMST) < len(self.matrix) - 1:

            while edges:
                E = heapq.heappop(edges)
                if not (VMST.search(E.y)):
                    break

            if not edges:
                break

            VMST.insert(E.y)
            EMST.append(E)

            for i in range(len(self.matrix)):
                if self.matrix[E.y][i] != 0:
                    heapq.heappush(edges, Edge(E.y, i, self.matrix[E.y][i]))
        return EMST


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
        VMST = Node(start)
        EMST = []
        edges = []
        for i in range(len(self.list[start])):
            heapq.heappush(edges, Edge(start, self.list[start][i].y, self.list[start][i].val))
        while len(EMST) < len(self.list) - 1:
            while edges:
                E = heapq.heappop(edges)
                if not (VMST.search(E.y)):
                    break

            if not edges:
                break

            VMST.insert(E.y)
            EMST.append(E)

            for i in range(len(self.list[E.y])):
                heapq.heappush(edges, Edge(E.y, self.list[E.y][i].y, self.list[E.y][i].val))
        return EMST


outM = open("PRIM30M.txt", 'w')
outL = open("PRIM30L.txt", 'w')

for i in range (1,16):
    matrix = GraphM(500*i, 30)
    list = GraphL(matrix)

    startTime = time.time()
    matrix.prim(0)
    endTime = time.time()
    Time = endTime - startTime
    del matrix
    outM.write("MST dla M:" + str(Time) + "\n")

    startTime = time.time()
    list.prim(0)
    endTime = time.time()
    Time = endTime - startTime
    outL.write("MST dla L:" + str(Time) + "\n")
    print(str(i))
    del list
outM.close()
outL.close()
