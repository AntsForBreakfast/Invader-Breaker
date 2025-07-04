import pygame

from world import World
from base.observer import Observer
from components.velocity import Velocity
from components.speed import Speed

class PlatformMovementObserver(Observer[pygame.Event]):
    def __init__(self, world:World) -> None:
        super().__init__()
        self.world:World = world
        self._pressed: dict[int, bool] = {
            pygame.K_w: False,
            pygame.K_s: False,
            pygame.K_d: False,
            pygame.K_a: False,
        }

    def update(self, event: pygame.Event) -> None:
        for components in self.world.query_components((Velocity, Speed)):
            velocity, speed = components[Velocity], components[Speed]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and not self._pressed[pygame.K_a]:
                    velocity.x = speed.x
                    self._pressed[pygame.K_d] = True

                if event.key == pygame.K_a and not self._pressed[pygame.K_d]:
                    velocity.x = -speed.x
                    self._pressed[pygame.K_a] = True

                if event.key == pygame.K_w and not self._pressed[pygame.K_s]:
                    velocity.y = -speed.y
                    self._pressed[pygame.K_w] = True

                if event.key == pygame.K_s and not self._pressed[pygame.K_w]:
                    velocity.y = speed.y
                    self._pressed[pygame.K_s] = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d and not self._pressed[pygame.K_a]:
                    velocity.x = 0
                    self._pressed[pygame.K_d] = False

                if event.key == pygame.K_a and not self._pressed[pygame.K_d]:
                    velocity.x = 0
                    self._pressed[pygame.K_a] = False

                if event.key == pygame.K_w and not self._pressed[pygame.K_w]:
                    velocity.x = 0
                    self._pressed[pygame.K_w] = False

                if event.key == pygame.K_s and not self._pressed[pygame.K_s]:
                    velocity.y = 0 
                    self._pressed[pygame.K_s] = False