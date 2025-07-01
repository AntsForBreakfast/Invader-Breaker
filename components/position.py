from dataclasses import dataclass

from base.component import Component


@dataclass(slots=True)
class Position(Component):
    x: float
    y: float
