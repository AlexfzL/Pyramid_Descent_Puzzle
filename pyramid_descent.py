import sys


class PD:
    def __init__(self):
        self.root = None
        self.target = 0
        self.P = []
        self.path = ""

    def readFile(self, f_name="pyramid_sample_input.txt"):
        f = open(f_name, mode='r')
        t = f.readline()
        self.target = int(t.split()[1])
        for l in f:
            row = l.split(",")
            for i in range(len(row)):
                row[i] = int(row[i])
            self.P.append(row)

    def findPath(self, target, i=0, j=0, pathSoFar=""):
        if j > i:
            return
        if i >= len(self.P):
            return

        if i == len(self.P)-1:
            if self.P[i][j] == target:
                self.path = pathSoFar

        if target % self.P[i][j] == 0:
            self.findPath(target / self.P[i][j], i+1, j, pathSoFar+"L")
            self.findPath(target / self.P[i][j], i+1, j+1, pathSoFar+"R")


if __name__ == "__main__":
    pd = PD()
    pd.readFile(sys.argv[1])
    # print(pd.P)
    # print(pd.target)
    pd.findPath(pd.target)
    print("The path is", pd.path)
    f = open(sys.argv[2], mode="w")
    f.write(pd.path)
