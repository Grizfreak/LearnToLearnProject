from Library import Library


class Test_Library(Library):

    def __init__(self):
        super().__init__('test')


    def summon(self):
        print('Salut je teste que tout fonctionne parfaitement bien')