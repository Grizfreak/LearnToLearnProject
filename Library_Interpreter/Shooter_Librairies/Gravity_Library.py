from Library_Interpreter.Library import Library


class Gravity_Library(Library):

    def __init__(self,game):
        super().__init__('gravity')
        self.game = game

    def gravity(self,arr):
        print("entered")
        if arr[1] == "player":
            self.game.player.del_gravity()
        if arr[1] == "monsters":
            for monster in self.game.all_monsters:
                monster.is_good = True