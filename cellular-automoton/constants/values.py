from game.shared.color import Color

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0)
WHITE = Color(255)
GREY = Color(127)
PURPLE = Color(255, 0, 255)
GREEN = Color(0, 255, 0)
RED = Color(255, 0, 0)
DARKRED = Color(127, 0, 0)
YELLOW = Color(255, 255, 0)
DARKYELLOW = Color(127, 127, 0)

# GLOBALS
WIDTH = 1000
HEIGHT = 800
CELL_SIZE = 20
ROWS = int(WIDTH / CELL_SIZE)
COLUMNS = int(HEIGHT / CELL_SIZE)
FRAME_RATE = 4
TITLE = "A Cellular Automaton"
GRANUALITY = 5
