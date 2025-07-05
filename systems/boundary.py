from world import World
from base.system import System
from components.position import Position
from components.boundary import Boundary


class BoundarySystem(System):
    def update(self, world: World, delta_time: float) -> None:
        for components in world.query_components((Position, Boundary)):
            position, boundary = components[Position], components[Boundary]
            position.x = max(boundary.min_x, min(position.x, boundary.max_x))
