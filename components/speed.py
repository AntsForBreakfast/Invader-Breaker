from dataclasses import dataclass

from base.component import Component

@dataclass(slots=True)
class Speed:
	x: float
	y: float