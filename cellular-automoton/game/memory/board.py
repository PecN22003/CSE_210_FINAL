from game.memory.cell import Cell


class Board:
    def __init__(self, default_value, size, ysize = None) -> None:
        if ysize is None:
            ysize = size
        self._board = self._initialize_board(default_value, size, ysize)

    def __getitem__(self, value):
        return self._board[value]

    def _initialize_board(self, default_value, size, ysize):
        board = []
        for i in range(size):
            board.append([])
            for _ in range(ysize):
                board[i].append(Cell(default_value.symbol, default_value.color))
        return board

    def check_neighbors(self, x, y):
        neighbors = {}
        for i in range(-1, 2):
            y_coord = (i + y) % len(self._board)
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                x_coord = (j + x) % len(self._board[y_coord])
                current_cell = self._board[y_coord][x_coord].symbol
                if not current_cell in neighbors:
                    neighbors[current_cell] = 0
                neighbors[current_cell] += 1
        sum = 0
        for i in neighbors:
            sum += neighbors[i]
        assert sum == 8 
        return neighbors

    def excecute(self):
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                cell = self._board[i][j]
                cell.excecute(self.check_neighbors(j, i))
        for row in self._board:
            for cell in row:
                cell.update()
                
