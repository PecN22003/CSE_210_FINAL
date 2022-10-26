from game.shared.color import Color
from constants.values import *


""" 
input format: a dictionary with keys-value pairs
[key]: num neighbors
"""

class State:
    def __init__(self, symbol: str, f, color: Color) -> None:
        self.symbol = symbol
        self.f = f
        self.color = color


class Ruleset:
    def __init__(self, default: str, *args) -> None:
        self.states = {}
        for i in args:
            self.states[i.symbol] = i
        self.default = self.states[default]


def elem(d: dict, value):
    return int(d.get(value))

game_of_life = Ruleset(" ", 
    # Alive: if 2 or 3 neighbors are alive, remain alive, otherwise, die
    State("A", lambda x: "A" if x.get("A", 0) == 2 or x.get("A", 0) == 3 else " ", GREEN),

    # Dead: if exactly 3 neighbors are alive, become alive, else, remain dead
    State(" ", lambda x: "A" if x.get("A", 0) == 3 else " ", BLACK)
)

seeds = Ruleset(" ",
    # Alive: become Dead
    State("A", lambda _: " ", WHITE),
    State(" ", lambda x: "A" if x.get("A", 0) == 2 else " ", BLACK)
)

brians_brain = Ruleset(" ",
    State("A", lambda _: "D", RED),
    State("D", lambda _: " ", DARKRED),
    State(" ", lambda x: "A" if x.get("A", 0) == 2 else " ", BLACK)
)

wire_world = Ruleset(" ",
    State(" ", lambda _: " ", GREY),
    State("WIRE", lambda x: "ALIVE" if x.get("ALIVE", 0) == 1 or x.get("ALIVE", 0) == 2 else "WIRE", BLACK),
    State("ALIVE", lambda _: "DYING", YELLOW),
    State("DYING", lambda _: "WIRE", DARKYELLOW)
)

RULES = seeds