from data.Library_Interpreter.Library import Library


class Summon_Library(Library):

    def __init__(self,game):
        super().__init__('summon')
        self.game = game

    def summon(self,arr):
        if arr[1] == "thunder":
            self.game.spawn_nuage()
        if arr[1] == 'wave':
            self.game.spawn_wave()
