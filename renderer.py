import pygame

from base.renderable import Renderable
from base.component import Component


class PygameRenderer:
    def __init__(self, screen: pygame.Surface):
        self.screen: pygame.Surface = screen

        self._renderables: dict[int, Renderable] = {}

    def add_renderable(self, entity_id: int, renderable: Renderable) -> None:
        self._renderables[entity_id] = renderable

    def clear(self, color: tuple[int, int, int]) -> None:
        self.screen.fill(color)

    def update(self) -> None:
        pygame.display.flip()

    def render(self, entity_id: int, components: dict[type[Component], Component]):
        self._renderables[entity_id].render(self.screen, components)
