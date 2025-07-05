from abc import ABC, abstractmethod

import pygame

from base.component import Component


class Renderable(ABC):
    """Abstract base class for renderable objects."""

    @abstractmethod
    def render(
        self, surface: pygame.Surface, data: dict[type[Component], Component]
    ) -> None: ...
