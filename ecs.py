from world import World
from base.system import System
from system_manager import SystemManager


class Ecs:
    def __init__(self) -> None:
        self._system_manager: SystemManager = SystemManager()
        self._worlds: dict[int, World] = {}
        self._world_id: int = 0

        self.active_world: World | None = None

    def add_system(self, system: System) -> None:
        self._system_manager.add_system(system)

    def new_world(self) -> tuple[int, World]:
        self._world_id += 1
        self._worlds[self._world_id] = World()

        return (self._world_id, self._worlds[self._world_id])

    def update(self, world: World, delta_time: float) -> None:
        self._system_manager.update(world, delta_time)
