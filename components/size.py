from dataclasses import dataclass

from base.component import Component


@dataclass(slots=True)
class Size(Component):
    width: float
    height: float
