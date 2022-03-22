from data.Library_Interpreter.StatesEnum import State


class Interpreter:

    # State: used to know the state of the game
    # Dictionnary : used to know Library usable

    def __init__(self, dictionnary):
        self.state = State.MENU
        self.dictionnary = dictionnary

    def interprete_command(self, response):
        match = 0
        arr = response.lower().split()

        for i in self.dictionnary.arr:
            if i.isUsable(arr[0]):
                i.summon(arr)
                match += 1
                break
        if match == 0: print('unable to find any matches')
