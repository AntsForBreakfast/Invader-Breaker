from dataclasses import dataclass

from base.component import Component

type Direction = tuple[int, int]
type Destination = tuple[float, float]


@dataclass(slots=True)
class Path(Component):
    waypoints: tuple[tuple[Direction, Destination], ...]
    active_waypoint: int = 0

    @property
    def direction(self) -> Direction:
        return self.waypoints[self.active_waypoint][0]

    @property
    def destination(self) -> Destination:
        return self.waypoints[self.active_waypoint][1]
