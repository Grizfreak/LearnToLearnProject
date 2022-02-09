class Library:
    def hello(self):
        print('hello')

    def __init__(self, id):
        self.id = id

    def printLibName(self):
        print(self.id)

    def isUsable(self,name):
        if name == self.id: return True
        else: return False

    def summon(self,arr):
        print('No reason to display something')