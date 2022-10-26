from threading import Thread
from game.memory.board import Board
from constants.rules import RULES
from constants.values import *
from game.memory.cell import Cell

from game.services.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib_mouse_service import RaylibMouseService
from game.services.raylib_video_service import RaylibVideoService




class Director:
    def __init__(self, video_service: RaylibVideoService) -> None:
        self._board = Board(RULES.default, COLUMNS, ROWS)
        self._video_service = video_service
        self._mouse_service = RaylibMouseService()
        self._keyboard_service = RaylibKeyboardService()
        self._paused = False

    def start(self):
        self._video_service.initialize()
        self._video_service.clear_buffer()
        t = 0
        while self._video_service.is_window_open():
            self._get_inputs()
            if t >= GRANUALITY:
                self._do_updates()
                t = 0
            t += 1
            self._do_outputs()
            self._video_service.flush_buffer()

        self._video_service.release()

    def _get_inputs(self):
        if self._keyboard_service.is_key_pressed("p"):
            self._paused = not self._paused
        if self._mouse_service.is_button_down("left"):
            self._change_cell_state(*self._mouse_service.get_coordinates())

    def _do_updates(self):
        if not self._paused:
            self._board.excecute()

    def _do_outputs(self):
        for i in range(COLUMNS):
            for j in range(ROWS):
                symbol = self._board[i][j].symbol
                color = RULES.states[symbol].color
                self._video_service.draw_rectangle(j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE, color)

        self._video_service.flush_buffer()

    def _change_cell_state(self, mx, my):
        x = mx//CELL_SIZE
        y = my//CELL_SIZE
        flag = False
        for i in RULES.states:
            if flag:
                self._board[y][x].symbol = i
                break
            elif i == self._board[y][x].symbol:
                flag = True
        else: # no break
            for i in RULES.states:
                self._board[y][x].symbol = i
                break
