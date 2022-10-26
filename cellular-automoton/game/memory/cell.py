from constants.rules import RULES
from game.shared.color import Color


class Cell:
    def __init__(self, symbol, color) -> None:
        self.color = color
        self.symbol = symbol
        self.fcolor = color
        self.fsymbol = symbol

    def excecute(self, neighbors):
        value = RULES.states[self.symbol].f(neighbors)
        new_state = RULES.states[value]
        self.fcolor = new_state.color
        self.fsymbol = value

    def update(self):
        self.color = self.fcolor
        self.symbol = self.fsymbol