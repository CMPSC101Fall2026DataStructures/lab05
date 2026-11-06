"""Animated starfield for the game background."""

import random

import pygame

from . import config


class Starfield:
    """A lightweight, randomly generated scrolling star background."""

    def __init__(self) -> None:
        # TODO 4a: Make an empty list for the stars, then repeat STAR_COUNT times.
        # Each star can be a list like [x, y, radius, speed].
        # Use random.randrange(WIDTH/HEIGHT), random.choice((1, 2, 3)),
        # and random.uniform(18, 90) to choose each star's values.
        self.stars = []

    def update(self, delta_seconds: float) -> None:
        """Scroll stars down and wrap them to the top of the screen."""
        # TODO 4b: Loop through self.stars. A star is [x, y, radius, speed].
        # Add speed * delta_seconds to its y value (index 1).
        # If y is greater than config.HEIGHT, pick a new x and set y to 0.
        pass

    def draw(self, surface: pygame.Surface) -> None:
        """Draw all stars with brightness based on their size."""
        # TODO 4c: Loop through self.stars and draw one circle per star.
        # Call pygame.draw.circle(surface, color, (round(x), round(y)), radius).
        # A simple color is (180, 200, 255). The star values are at indexes
        # 0 (x), 1 (y), and 2 (radius).
        pass
