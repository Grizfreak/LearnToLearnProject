from Library_Interpreter.Library import Library
from platformer.GravityState import GravityState


class Gravity_Library(Library):

    def __init__(self, player):
        super().__init__('gravity')
        self.player = player

    def summon(self, arr):
        if arr[1] == 'left':
            print('left')
            self.player.gameConstants.gravity = GravityState.LEFT
        elif arr[1] == 'right':
            self.player.gameConstants.gravity = GravityState.RIGHT
        elif arr[1] == 'bottom':
            self.player.gameConstants.gravity = GravityState.BOTTOM
        elif arr[1] == 'top':
            self.player.gameConstants.gravity = GravityState.TOP
        else:
            print('unable to find matches')
