import random
import time

class GraphM:

    def __init__(self, n, g):
        self.matrix = []

        for i in range(n):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append(0)
        for i in range(n):
            for j in range(i + 1, n):
                if j == i + 1 or (random.random() + 2 / n) < (g / 100):
                    self.matrix[i][j] = 1
        for i in range(n):
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            if x != y:
                self.matrix[x], self.matrix[y] = self.matrix[y], self.matrix[x]
                for i in range(n):
                    self.matrix[i][x], self.matrix[i][y] = self.matrix[i][y], self.matrix[i][x]

    def __str__(self):
        out = ""
        for i in range(len(self.matrix)):
            pom = ""
            for j in range(len(self.matrix)):
                pom = pom + str(self.matrix[i][j]) + " "
            out = out + "\n" + pom
        return out

    def start(self):
        for i in range(len(self.matrix)):
            bool = 1
            for j in range(len(self.matrix)):
                if self.matrix[j][i] == 1:
                    bool = 0
                    break
            if bool == 1:
                return i


    def _TS(self, IN, Sort, step, v):
        step += 1
        IN[v] = step
        for i in range(len(self.matrix)):
            if self.matrix[v][i] != 0 and IN[i] == -1:
                self._TS(IN, Sort, step, i)
        Sort.insert(0, v)

    def TS(self, start):
        IN = [-1] * len(self.matrix)
        step = 0
        Sort = []
        self._TS(IN, Sort, step, start)
        return Sort


class Edge:
    def __init__(self, u, v, val):
        self.x = x
        self.y = y
        self.val = val


class GraphL:
    def __init__(self, matrix):
        self.list = []
        l = len(matrix.matrix)
        for i in range(l):
            self.list.append([])
            for j in range(l):
                val = matrix.matrix[i][j]
                if val != 0:
                    self.list[i].append(j)

    def __str__(self):
        l = len(self.list)
        out = ""
        for i in range(l):
            pom = str(i) + ":  "
            li = len(self.list[i])
            for j in range(li):
                pom = pom + str(self.list[i][j]) + " "
            out = out + "\n" + pom
        return out

    def _TS(self, IN, Sort, step, v):
        step += 1
        IN[v] = step
        for i in range(len(self.list[v])):
            if IN[self.list[v][i]] == -1:
                self._TS(IN, Sort, step, self.list[v][i])
        Sort.insert(0, v)

    def TS(self, start):
        IN = [-1] * len(self.list)
        step = 0
        Sort = []
        self._TS(IN, Sort, step, start)
        return Sort


outM = open("TSM.txt", 'w')
outL = open("TSL.txt", 'w')

for i in range (1,16):
    matrix = GraphM(1000*i, 60)
    list = GraphL(matrix)
    start = matrix.start()

    startTime = time.time()
    matrix.TS(start)
    endTime = time.time()
    Time = endTime - startTime
    outM.write("Ts dla M:" + str(Time) + "\n")

    startTime = time.time()
    list.TS(start)
    endTime = time.time()
    Time = endTime - startTime
    outL.write("Ts dla L:" + str(Time) + "\n")
    print(str(i))
outM.close()
outL.close()
