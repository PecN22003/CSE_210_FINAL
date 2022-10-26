from game.shared.color import Color
from constants.values import *


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

    # Dead: If exactly two neighbors are alive, become alive, else stay dead
    State(" ", lambda x: "A" if x.get("A", 0) == 2 else " ", BLACK)
)

brians_brain = Ruleset(" ",
    # Alive: become Dying
    State("A", lambda _: "D", RED),

    # Dying: become Dead
    State("D", lambda _: " ", DARKRED),

    # Dead: If exactly two neighbors are alive, become alive, else stay dead
    State(" ", lambda x: "A" if x.get("A", 0) == 2 else " ", BLACK)
)

wire_world = Ruleset(" ",
    # Nothing: Stay nothing
    State(" ", lambda _: " ", GREY),

    # Wire: if one or two neighbors are alive, become alive else, stay dead
    State("WIRE", lambda x: "ALIVE" if x.get("ALIVE", 0) == 1 or x.get("ALIVE", 0) == 2 else "WIRE", BLACK),

    # Alive: become Dying
    State("ALIVE", lambda _: "DYING", YELLOW),

    # Dying: become Dead
    State("DYING", lambda _: "WIRE", DARKYELLOW)
)

day_and_night = Ruleset(" ", # don't try too hard to read this one, it is code golfed, but if you insist...
    # Dead: become alive if 3, 5, 7, or 8 neighbors are alive, otherwise, stay dead
    State(" ", lambda x: "A" if not (3 != x.get("A") != 5) or not (7 != x.get("A") != 8) else " ", BLACK),

    # Alive: become dead if 3, 5, 7, or 8 neighbors are dead, otherwise, stay alive
    State("A", lambda x: " " if not (3 != x.get(" ") != 5) or not (7 != x.get(" ") != 8) else "A", BLACK)
)

# CUSTOM_RULESET = Ruleset([DEFAULT VALUE],
#     State([VALUE], lambda x: [condition, using x.get([VALUE], 0) to get number of neighbors),
#     [as many states as you want]
# )

RULES = game_of_life