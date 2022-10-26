from game.directing.director import Director
from game.services.raylib_video_service import RaylibVideoService
from constants.values import *

director = Director(RaylibVideoService(TITLE, WIDTH, HEIGHT))
director.start()