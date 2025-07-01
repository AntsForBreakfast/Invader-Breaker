from dataclasses import dataclass

from base.component import Component


@dataclass(slots=True)
class Velocity(Component):
    x: float
    y: float
