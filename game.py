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
from systems.movement import PlatformMovementSystem
from systems.boundary import PlatformBoundarySystem
from observers.movement import PlatformMovementObserver
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
        self.event_listener.add_observer(PlatformMovementObserver(self.world))

        # Entities
        self.aliens = [
            [self.world.new_entity() for _ in range(5 if i % 2 == 0 else 6)]
            for i in range(5)
        ]
        self.platform = self.world.new_entity()

        # Systems
        self.ecs.add_system(PlatformMovementSystem(self.platform))
        self.ecs.add_system(PlatformBoundarySystem(self.platform))

        # Components
        alien_size = Size(5, 5)
        alien_color = Color(50, 50, 50)
        alien_velocity = Velocity(0, 0)
        alien_speed = Speed(50, 50)
        # alien_path = Path(

        # )
        platform_position = Position(self.screen.get_width() / 2 - 50, 165)
        platform_size = Size(100, 5)
        platform_velocity = Velocity(0, 0)
        platform_color = Color(100, 100, 100)
        platform_speed = Speed(100, 0)
        platform_boundary = Boundary(5, DISPLAY_SIZE[0] - 105, 0, 0)

        for i, alien_row in enumerate(self.aliens, 1):
            for j, alien_id in enumerate(alien_row, 1):
                x = 50 * j if i % 2 != 0 else -25 + 50 * j
                y = 15 * i
                alien_position = Position(x, y)

                self.world.add_components(
                    alien_id, [alien_position, alien_velocity, alien_speed, alien_size, alien_color]
                )

        self.world.add_components(
            self.platform,
            [
                platform_position,
                platform_size,
                platform_velocity,
                platform_color,
                platform_speed,
                platform_boundary,
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
