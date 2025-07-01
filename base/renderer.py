from abc import ABC, abstractmethod

from .renderable import Renderable


class Renderer(ABC):
    """Abstract base class for managing and rendering renderable entities"""

    def __init__(self):
        self._renderables: dict[int, Renderable] = {}

    def add_renderable(self, entity_id: int, renderable: Renderable) -> None:
        self._renderables[entity_id] = renderable

    @abstractmethod
    def render(self) -> None: ...
