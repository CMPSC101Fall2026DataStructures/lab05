"""Player ship controls and firing behavior."""

import pygame

from . import config
# TODO 3: Import Projectile from this package's projectile module.


class Player(pygame.sprite.Sprite):
    """The ship controlled by the player."""

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((54, 42), pygame.SRCALPHA)
        pygame.draw.polygon(
            self.image,
            config.CYAN,
            [(27, 0), (52, 36), (40, 34), (34, 24), (20, 24), (14, 34), (2, 36)],
        )
        pygame.draw.rect(self.image, config.WHITE, (21, 28, 12, 5), border_radius=2)
        self.rect = self.image.get_rect(midbottom=(config.WIDTH // 2, config.HEIGHT - 28))
        self.position_x = float(self.rect.x)
        self.last_shot = 0

    def update(self, keys: pygame.key.ScancodeWrapper, delta_seconds: float) -> None:
        """Move horizontally and keep the ship inside the playfield."""
        # TODO 7a: Get left_pressed and right_pressed from keys using
        # K_LEFT or K_a, and K_RIGHT or K_d. Keys are indexed like keys[key].
        # TODO 7b: Find direction: int(right_pressed) - int(left_pressed).
        # Add direction * config.PLAYER_SPEED * delta_seconds to position_x,
        # then set rect.x = round(position_x).
        # TODO 7c: Keep rect.left at least 12 and rect.right at most WIDTH - 12.
        # After clamping the rect, copy rect.x back to position_x.
        pass

    def shoot(self, now_ms: int) -> Projectile | None:
        """Return a player shot when the firing cooldown has elapsed."""
        # TODO 3 imports Projectile; TODO 7d uses it here.
        # If now_ms - last_shot is less than config.PLAYER_COOLDOWN_MS,
        # return None. Otherwise save now_ms in last_shot and return:
        # Projectile(self.rect.centerx, self.rect.top,
        #            -config.PLAYER_BULLET_SPEED, config.CYAN)
        return None
