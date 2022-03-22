class Dictionnary:
    def __init__(self, arr):
        self.arr = arr

    def printLibs(self):
        for i in self.arr:
            print(i.printLibName())