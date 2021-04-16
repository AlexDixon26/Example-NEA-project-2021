from abc import ABC, abstractmethod

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        print("Running GUI")

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()
        

    def run(self):
        while not self.__game.winner:
            print(self.__game)
            row = int(input("enter the row: "))
            col = int(inputer("enter the column: "))
            self.__game.play(row,col)