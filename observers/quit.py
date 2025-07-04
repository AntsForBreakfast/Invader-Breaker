import sys

import pygame

from base.observer import Observer


class QuitObserver(Observer[pygame.Event]):
    def update(self, event: pygame.Event) -> None:
        if (
            event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
        ):
            pygame.quit()
            sys.exit()
