import pygame

from base.renderable import Renderable
from base.component import Component
from components.color import Color
from components.position import Position
from components.size import Size


class Rectangle(Renderable):
    def render(self, surface: pygame.Surface, data: dict[type[Component], Component]):
        pygame.draw.rect(
            surface,
            data[Color].rgb,
            (data[Position].x, data[Position].y, data[Size].width, data[Size].height),
        )
