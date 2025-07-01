from abc import ABC, abstractmethod


class Renderable(ABC):
    """Abstract base class for renderable objects."""

    @abstractmethod
    def render(self) -> None: ...
