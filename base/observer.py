from abc import ABC, abstractmethod


class Observer[T](ABC):
    """Abstract base class representing an observer that acts upon the events"""

    @abstractmethod
    def update(self, event: T) -> None: ...
