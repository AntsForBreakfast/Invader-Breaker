from abc import ABC, abstractmethod

from world import World


class System(ABC):
    """
    Abstract base class for systems that process entities with specific components
    and apply game logic each update cycle.
    """

    @abstractmethod
    def update(self, world: World, delta_time: float) -> None: ...
