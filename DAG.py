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
                if j == i+1 or  (random.random() + 2/n) < (g/100):
                    self.matrix[i][j] = 1
        for i in range(n):
            x = random.randint(0,n-1)
            y = random.randint(0,n-1)
            if x != y:
                self.matrix[x], self.matrix[y] =  self.matrix[y],  self.matrix[x]
                if self.matrix[x][x] ==1:
                    self.matrix[x][x] = 0
                    self.matrix[x][y] = 1
                elif self.matrix[y][y] ==1:
                    self.matrix[y][y] = 0
                    self.matrix[y][x] = 1



    def __str__(self):
        out = ""
        for i in range (len(self.matrix)):
            pom = ""
            for j in range(len(self.matrix)):
                pom = pom + str(self.matrix[i][j]) + " "
            out = out + "\n" + pom
        return out

    def _TS(self, IN, Sort, step, v):
        step +=1
        IN[v] = step
        for  i in range(len(self.matrix)):
            if self.matrix[v][i] != 0 and IN[i] == -1:
                self._TS(IN, Sort, step, i)
        Sort.insert(0,v)


    def TS(self,start):
        IN = [-1]*len(self.matrix)
        step = 0
        Sort = []
        self._TS(IN, Sort, step,start)
        return Sort





class Edge:
    def __init__(self,u,v, val):
        self.x = x
        self.y = y
        self.val = val


class GraphL:
    def __init__ (self, matrix):
        self.list = []
        l = len(matrix.matrix)
        for  i in range(l):
            self.list.append([])
            for j in range(l):
                val = matrix.matrix[i][j]
                if  val != 0:
                   self.list[i].append(j)

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

    def _TS(self,IN, Sort, step, v):
        step +=1
        IN[v] = step
        for  i in range(len(self.list[v])):
            if IN[self.list[v][i]] == -1:
               self._TS(IN, Sort, step, self.list[v][i])
        Sort.insert(0,v)


    def TS(self,start):
        IN = [-1]*len(self.list)
        step = 0
        Sort = []
        self._TS(IN, Sort, step, start)
        return Sort

HelloWorld = GraphM(10,60)
print(HelloWorld)
HelloWorldL = GraphL(HelloWorld)
print(HelloWorldL)

print(HelloWorld.TS(0))
print(HelloWorldL.TS(0))