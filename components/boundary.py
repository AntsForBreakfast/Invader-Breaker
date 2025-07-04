from dataclasses import dataclass

from base.component import Component


@dataclass(slots=True)
class Boundary(Component):
    min_x: float
    max_x: float
    min_y: float
    max_y: float