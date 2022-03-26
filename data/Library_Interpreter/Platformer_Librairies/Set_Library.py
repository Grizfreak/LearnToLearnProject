from data.Library_Interpreter.Library import Library


class Set_Library(Library):

    def __init__(self, player):
        super().__init__('set')
        self.player = player

    def summon(self, arr):
        if arr[1] == 'jump':
            self.player.set_jumpBoost(int(arr[2]))
        elif arr[1] == 'speed':
            self.player.set_speed(int(arr[2]))
        else:
            print('unable to find matches')
        self.player.changeSprite()