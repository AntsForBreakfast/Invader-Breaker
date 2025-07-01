from dataclasses import dataclass

from base.component import Component


@dataclass(slots=True)
class Color(Component):
    r: int
    g: int
    b: int

    @property
    def rgb(self) -> tuple[int, int, int]:
        return (self.r, self.g, self.b)
