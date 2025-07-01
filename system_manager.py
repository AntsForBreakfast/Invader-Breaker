from base.system import System
from world import World


class SystemManager:
    """Registers and manages systems, running their update methods each frame"""

    def __init__(self) -> None:
        self._systems: dict[type[System], System] = {}

    def add_system(self, system: System) -> None:
        self._systems[type(system)] = system

    def update(self, world: World, dt: float) -> None:
        for system in self._systems.values():
            system.update(world, dt)
