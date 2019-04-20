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

    def print (self):
        for i in range (len(self.matrix)):
            pom = ""
            for j in range(len(self.matrix)):
                pom = pom + str(self.matrix[i][j]) + " "
            print (pom)


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

    def print (self):
        l = len(self.list)
        for i in range (l):
            pom = str(i)+ ":  "
            li = len(self.list[i])
            for j in range(li):
                pom = pom + str(self.list[i][j]) + " "
            print (pom)

HelloWorld = GraphM(10,60)
HelloWorld.print()
HelloWorldL = GraphL(HelloWorld)
HelloWorldL.print()