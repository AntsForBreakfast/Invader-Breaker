from world import World
from base.system import System
from components.position import Position
from components.velocity import Velocity
from tags import Controllable


class MovementSystem(System):
    def update(self, world: World, delta_time: float) -> None:
        for components in world.query_components((Position, Velocity)):
            position = components[Position]
            velocity = components[Velocity]

            position.x += velocity.x * delta_time
            position.y += velocity.y * delta_time
