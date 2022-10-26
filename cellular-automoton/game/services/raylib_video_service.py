import os
import pathlib
import pyray
from constants.values import *
from game.shared.color import Color


class RaylibVideoService:
    """ A Raylib implementation of VideoService."""

    def __init__(self, title = "", width = 640, height = 480, color = BLACK):
        self._title = title
        self._width = width
        self._height = height
        self._color = color
        self._fonts = {}
        self._textures = {}
        
    def clear_buffer(self):
        raylib_color = self._to_raylib_color(self._color)
        pyray.begin_drawing()
        pyray.clear_background(raylib_color)

    def draw_image(self, image, x, y):
        filepath = image.get_filename()
        # fixed os dependent filepath
        filepath = str(pathlib.Path(filepath))
        texture = self._textures[filepath]
        raylib_position = pyray.Vector2(x, y)
        scale = image.get_scale()
        rotation = image.get_rotation()
        tint = self._to_raylib_color(Color(255,255,255)) 
        pyray.draw_texture_ex(texture, raylib_position, rotation, scale, tint)
         
    def draw_rectangle(self, x, y, width, height, color, filled = True):
        raylib_color = self._to_raylib_color(color)

        if filled:
            pyray.draw_rectangle(x, y, width, height, raylib_color)
        else:
            pyray.draw_rectangle_lines(x, y, width, height, raylib_color)
        
    def flush_buffer(self):
        pyray.end_drawing()

    def initialize(self):
        pyray.set_target_fps(FRAME_RATE * GRANUALITY)
        pyray.init_window(self._width, self._height, self._title)

    def is_window_open(self):
        return not pyray.window_should_close()

    def load_fonts(self, directory):
        filepaths = self._get_filepaths(directory, [".otf", ".ttf"])
        for filepath in filepaths:
            if filepath not in self._fonts.keys():
                font = pyray.load_font(filepath)
                self._fonts[filepath] = font

    def load_images(self, directory):
        filepaths = self._get_filepaths(directory, [".png", ".gif", ".jpg", ".jpeg", ".bmp"])
        for filepath in filepaths:
            if filepath not in self._textures.keys():
                texture = pyray.load_texture(filepath)
                self._textures[filepath] = texture

    def release(self):
        pyray.close_window()
        
    def unload_fonts(self):
        for font in self._fonts.values():
            pyray.unload_font(font)
        self._fonts.clear()

    def unload_images(self):
        for texture in self._textures.values():
            pyray.unload_texture(texture)
        self._textures.clear()

    def _get_filepaths(self, directory, filter):
        filepaths = []
        for file in os.listdir(directory):
            filename = os.path.join(directory, file)
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filename = str(pathlib.Path(filename))
                filepaths.append(filename)
        return filepaths

    def _to_raylib_color(self, color):
        r, g, b, a = color.to_tuple()
        return pyray.Color(r, g, b, a)