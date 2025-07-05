from world import World
from base.system import System
from components.speed import Speed
from components.position import Position
from components.velocity import Velocity
from components.path import Path


class PathSystem(System):
    def update(self, world: World, delta_time: float) -> None:
        for components in world.query_components((Position, Velocity, Speed, Path)):
            position = components[Position]
            velocity = components[Velocity]
            speed = components[Speed]
            path = components[Path]

            # path has to have start and end , raise error?
            if len(path.waypoints) < 2:
                continue

            # Reached the end of the path, go back to start

            if path.active_waypoint >= len(path.waypoints):
                path.active_waypoint = 0

            velocity.x = speed.x * path.direction[0]
            velocity.y = speed.y * path.direction[1]


            # Reached the destination, switch to next
            if abs(position.x - path.destination[0]) < 1 and abs(position.y - path.destination[1]) < 1:
                path.active_waypoint += 1
