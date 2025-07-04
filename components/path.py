from dataclasses import dataclass

from base.component import Component

type Direction = tuple[int, int]
type Distance = float

@dataclass(slots=True)
class Path(Component):
    waypoints: list[tuple[Direction, Distance]]
    active_waypoint: int = 0