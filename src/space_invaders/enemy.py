"""Invader sprite definitions."""

import pygame

from . import config


class Invader(pygame.sprite.Sprite):
    """A colorful alien in the marching formation."""

    def __init__(self, x: int, y: int, row: int) -> None:
        super().__init__()
        # TODO 6a: Create a transparent image:
        # self.image = pygame.Surface((42, 34), pygame.SRCALPHA)
        # TODO 6b: Pick a row color with this pattern:
        # colors = (config.PINK, config.GREEN, config.YELLOW, config.CYAN)
        # color = colors[row % len(colors)]
        # TODO 6c: Use pygame.draw.rect/circle/line to draw a body and eyes.
        # TODO 6d: Set self.rect = self.image.get_rect(topleft=(x, y)).
