from world import World
from base.system import System
from components.position import Position
from components.velocity import Velocity

class PlatformMovementSystem(System):
    def __init__(self, platform_id:int) -> None:
        self.platform_id: int = platform_id

    def update(self, world:World, delta_time:float) -> None:
        for components in world.query_components_from(self.platform_id, (Position, Velocity)):
            position, velocity = components[Position], components[Velocity]
            position.x += velocity.x * delta_time
            position.y += velocity.y * delta_time
