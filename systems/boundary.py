from world import World
from base.system import System
from components.position import Position
from components.boundary import Boundary

class PlatformBoundarySystem(System):
    def __init__(self, platform_id: int) -> None:
        self.platform_id: int = platform_id

    def update(self, world:World, delta_time:float) -> None:
        for components in world.query_components_from(self.platform_id, (Position, Boundary)):
            position, boundary = components[Position], components[Boundary]
            position.x = max(boundary.min_x, min(position.x, boundary.max_x))