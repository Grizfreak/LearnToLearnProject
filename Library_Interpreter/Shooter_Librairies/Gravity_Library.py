from Library_Interpreter.Library import Library


class Gravity_Library(Library):

    def __init__(self,game):
        super().__init__('gravity')
        self.game = game

    def gravity(self,arr):
        if arr[1] == "player":
            self.game.player.del_gravity()