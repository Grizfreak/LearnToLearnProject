from Library_Interpreter.Library import Library


class Shield_Library(Library):

    def __init__(self,game):
        super().__init__('shield')
        self.game = game

    def summon(self,arr):
        if arr[1] == 'activate':
            self.game.player.is_shielded = True
            self.game.player.actived_shield()