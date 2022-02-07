# This is a sample Python script.
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from Library import Library
from Summon_Library import Summon_Library
from Interpreter import Interpreter
from Dictionnary import Dictionnary
from Test_Library import Test_Library

if __name__ == '__main__':
    summon = Summon_Library()
    test = Test_Library()
    dictionnary_usable = Dictionnary([summon,test])
    interpreter = Interpreter(dictionnary_usable)
    interpreter.interprete_command(input("Send me you command :"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
