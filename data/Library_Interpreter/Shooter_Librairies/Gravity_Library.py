from data.Library_Interpreter.Library import Library


class Gravity_Library(Library):

    def __init__(self,game):
        super().__init__('gravity')
        self.game = game

    def summon(self,arr):
        if arr[1] == 'player':
            self.game.player.del_gravity()
        if arr[1] == 'monsters':
            for monster in self.game.all_monsters:
                monster.is_good = True