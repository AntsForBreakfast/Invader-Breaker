import pygame

from ecs import Ecs
from event_listener import EventListener
from renderer import PygameRenderer
from renderables.rectangle import Rectangle
from components.position import Position
from components.size import Size
from components.color import Color
from components.velocity import Velocity
from components.speed import Speed
from components.boundary import Boundary
from components.path import Path
from tags import Controllable
from systems.movement import MovementSystem
from systems.boundary import BoundarySystem
from systems.path import PathSystem
from observers.movement import MovementObserver
from observers.quit import QuitObserver

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

        # Worlds
        self.world_id, self.world = self.ecs.new_world()

        # Events
        self.event_listener.add_observer(QuitObserver())
        self.event_listener.add_observer(MovementObserver(self.world))

        # Entities
        self.aliens = [
            [self.world.new_entity() for _ in range(5 if i % 2 == 0 else 6)]
            for i in range(5)
        ]
        self.platform = self.world.new_entity()

        # Systems
        self.ecs.add_system(MovementSystem())
        self.ecs.add_system(BoundarySystem())
        self.ecs.add_system(PathSystem())

        # Components
        for i, alien_row in enumerate(self.aliens, 1):
            for j, alien_id in enumerate(alien_row, 1):
                pos_y = 15 * i

                if i % 2 != 0:
                    pos_x = 50 * j
                    speed = Speed(30, 30)
                    path = Path(
                        (
                            ((0, 1), (pos_x, pos_y + 5)),
                            ((-1, 0), (pos_x-5 , pos_y + 5)),
                            ((0, -1), (pos_x-5, pos_y)),
                            ((1, 0), (pos_x, pos_y)),
                        )
                    )
                else:
                    pos_x = -25 + 50 * j
                    speed = Speed(20, 20)
                    path = Path(
                        (
                            ((1, 0), (pos_x + 35, pos_y)),
                            ((0, 1), (pos_x + 35, pos_y + 35)),
                            ((-1, 0), (pos_x, pos_y + 35)),
                            ((0, -1), (pos_x, pos_y)),
                        )
                    )

                
                self.world.add_components(
                    alien_id,
                    (
                        Position(pos_x, pos_y),
                        Velocity(0, 0),
                        speed,
                        Size(5, 5),
                        Color(50, 50, 50),
                        path,
                    ),
                )

        self.world.add_components(
            self.platform,
            [
                Position(self.screen.get_width() / 2 - 50, 165),
                Size(100, 5),
                Velocity(0, 0),
                Color(100, 100, 100),
                Speed(100, 0),
                Boundary(5, DISPLAY_SIZE[0] - 105, 0, 0),
                Controllable(),
            ],
        )

        # Renderables
        for alien_row in self.aliens:
            for alien_id in alien_row:
                self.renderer.add_renderable(alien_id, Rectangle())

        self.renderer.add_renderable(self.platform, Rectangle())

    def update(self) -> None:
        delta_time = self.clock.tick(FPS) / 1000
        self.ecs.update(self.world, delta_time)

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
