import pygame

from ecs import Ecs
from event_listener import EventListener
from renderer import PygameRenderer
from components.position import Position
from components.size import Size
from components.color import Color
from components.velocity import Velocity
from observers.quit import Quit
from renderables.rectangle import Rectangle
from constants import (
    DISPLAY_SIZE,
    FPS,
)


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE, pygame.SCALED)
        self.clock = pygame.time.Clock()

        # Init
        self.ecs = Ecs()
        self.event_listener = EventListener[pygame.Event]()
        self.renderer = PygameRenderer(self.screen)

        # Events
        self.event_listener.add_observer(Quit())

        # Worlds
        self.world_id, self.world = self.ecs.new_world()

        # Entities
        self.aliens = [[self.world.new_entity() for _ in range(5)] for _ in range(5)]
        self.platform = self.world.new_entity()

        # Components
        for i, alien_row in enumerate(self.aliens, 1):
            for j, alien in enumerate(alien_row, 1):
                self.world.add_components(
                    alien, [Position(50 * j, 15 * i), Size(10, 10), Color(50, 50, 50)]
                )

        self.world.add_components(
            self.platform,
            [
                Position(self.screen.get_width() / 2 - 50, 165),
                Size(100, 5),
                Velocity(1, 0),
                Color(100, 100, 100),
            ],
        )

        # Renderables
        for alien_row in self.aliens:
            for alien_id in alien_row:
                self.renderer.add_renderable(alien_id, Rectangle())

        self.renderer.add_renderable(self.platform, Rectangle())

    def update(self) -> None:
        self.clock.tick(FPS)

    def render(self) -> None:
        self.renderer.clear([255, 255, 255])

        # Aliens
        for alien_row in self.aliens:
            for alien_id in alien_row:
                self.renderer.render(alien_id, self.world.get_components(alien_id))

        # Platform
        self.renderer.render(self.platform, self.world.get_components(self.platform))

        self.renderer.update()

    def run(self) -> None:
        while True:
            self.event_listener.update(pygame.event.get())
            self.update()
            self.render()
