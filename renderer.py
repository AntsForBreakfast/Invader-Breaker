import pygame

from base.renderable import Renderable
from base.component import Component
from base.renderer import Renderer


class PygameRenderer(Renderer):
    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.screen: pygame.Surface = screen

    def clear(self, color: tuple[int, int, int]) -> None:
        self.screen.fill(color)

    def update(self) -> None:
        pygame.display.flip()

    def render(self, entity_id: int, components: dict[type[Component], Component]):
        self._renderables[entity_id].render(self.screen, components)
