from typing import Iterable

from base.observer import Observer


class EventListener[E]:
    def __init__(self) -> None:
        self._observers: list[Observer[E]] = []

    def add_observer(self, observer: Observer[E]) -> None:
        self._observers.append(observer)

    def notify_observer(self, event: E) -> None:
        for observer in self._observers:
            observer.update(event)

    def update(self, events: Iterable[E]) -> None:
        for event in events:
            self.notify_observer(event)
