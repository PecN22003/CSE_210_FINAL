from game.scripting.action import Action
from constants.values import *


class DrawCellAction(Action):
    def __init__(self, video_service):
        self.video_service = video_service
        super().__init__()

    def excecute(self, x, y, color):
        self.video_service.draw_rectangle(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE, color)

    