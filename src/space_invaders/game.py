"""Main game loop and coordination between the game modules."""

import random

import pygame

from . import config
# TODO 2: Import Starfield, Invader, Player, and Projectile from their local modules.


class Game:
    """Own the window, game state, sprites, and main event loop."""

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(config.TITLE)
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)
        self.large_font = pygame.font.Font(None, 76)
        self.small_font = pygame.font.Font(None, 22)
        self.background = Starfield()
        self.running = True
        self.started = False
        self.game_over = False
        self.reset_round()

    def reset_round(self) -> None:
        """Start a fresh game with a new player and invader formation."""
        self.player = Player()
        self.player_shots = pygame.sprite.Group()
        self.enemy_shots = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.score = 0
        self.lives = 3
        self.wave = 1
        self.enemy_direction = 1
        self.enemy_shot_timer = 0.0
        self._create_formation()


    def _create_formation(self) -> None:
        """Create a centered grid of invaders."""
        # TODO 8: The two lines below calculate the formation's total width
        # and the left edge that centers it. Check the parentheses carefully.
        formation_width = config.ENEMY_COLUMNS * 64
        left = (config.WIDTH - formation_width) // 2
        for row in range(config.ENEMY_ROWS):
            for column in range(config.ENEMY_COLUMNS):
                self.enemies.add(
                    Invader(left + column * 64, 115 + row * 52, row)
                )

    def run(self) -> None:
        """Run until the player quits."""
        while self.running:
            delta_seconds = min(self.clock.tick(config.FPS) / 1000, 0.05)
            self._handle_events()
            self.background.update(delta_seconds)
            if self.started and not self.game_over:
                self._update_game(delta_seconds)
            self._draw()
        pygame.quit()

    def _handle_events(self) -> None:
        """Handle window events and the game's keyboard controls."""
        # TODO 9a: Loop over pygame.event.get().
        # If event.type is pygame.QUIT, set self.running = False.
        # TODO 9b: Use elif event.type == pygame.KEYDOWN to handle keys.
        # Compare event.key with pygame.K_ESCAPE, pygame.K_RETURN,
        # pygame.K_SPACE, and pygame.K_r. Enter or Space starts if not started.
        # TODO 9c: For the key cases, use if/elif so one press does one action:
        # (1) Escape quits; (2) if not started, Enter/Space starts;
        # (3) if game_over, R resets and starts; (4) if started and not
        # game_over, Space fires. For firing, call
        # player.shoot(pygame.time.get_ticks()) and add the returned shot
        # to player_shots only when it is not None.
        pass

    def _update_game(self, delta_seconds: float) -> None:
        """Advance sprites, formation movement, and collision-driven state."""
        # TODO 10a: Read held keys with pygame.key.get_pressed(). Update the
        # player and both projectile groups using delta_seconds.
        # TODO 10b: Move each enemy horizontally by direction * speed *
        # delta_seconds. Speed can be 42 + (wave - 1) * 9. If the leftmost
        # enemy reaches 18 or the rightmost reaches WIDTH - 18, reverse
        # enemy_direction and move every enemy down by config.ENEMY_DROP.
        # Hint: Find edges with min(enemy.rect.left for enemy in enemies) and
        # max(enemy.rect.right for enemy in enemies).
        # If an enemy's rect.bottom >= player.rect.top, set game_over = True.
        # TODO 10c: Add delta_seconds to enemy_shot_timer. When it reaches
        # config.ENEMY_SHOT_INTERVAL, reset it to 0, choose an enemy with
        # random.choice(self.enemies.sprites()), and add a downward Projectile
        # to enemy_shots. Its arguments are the enemy's centerx, bottom,
        # config.ENEMY_BULLET_SPEED, and config.PINK. Do this only when enemies
        # remain.
        # TODO 10d: Update score from
        # pygame.sprite.groupcollide(enemies, player_shots, True, True).
        # If pygame.sprite.spritecollide(player, enemy_shots, True) is not
        # empty, subtract one life. Set game_over if lives reaches zero.
        # TODO 10e: If no enemies remain and the game is not over, add one to
        # wave, reset enemy_direction to 1, and call _create_formation().
        pass

    def _draw(self) -> None:
        """Render the starfield, sprites, HUD, and any screen overlays."""
        # TODO 11a: Fill self.screen using config.BACKGROUND, then call
        # self.background.draw(self.screen).
        # TODO 11b: If started, draw the enemies and both shot groups with
        # their .draw(self.screen) methods. Draw the player's image unless
        # game_over with self.screen.blit(self.player.image, self.player.rect),
        # then call self._draw_hud().
        # TODO 11c: Otherwise show a title and instructions using
        # self._draw_centered(text, font, color, y). For example, draw the
        # title at y=250 with large_font and the start instruction at y=390
        # with font. If game_over, show "GAME OVER" and "Press R to play again".
        # TODO 11d: Finish the frame with pygame.display.flip().
        pass

    def _draw_hud(self) -> None:
        """Draw score, lives, and wave number."""
        self.screen.blit(
            self.font.render(f"SCORE  {self.score:05d}", True, config.WHITE), (24, 20)
        )
        self.screen.blit(
            self.font.render(f"WAVE  {self.wave}", True, config.CYAN), (config.WIDTH // 2 - 45, 20)
        )
        self.screen.blit(
            self.font.render(f"LIVES  {self.lives}", True, config.GREEN),
            (config.WIDTH - 145, 20),
        )

    def _draw_centered(
        self,
        text: str,
        font: pygame.font.Font,
        color: tuple[int, int, int],
        y: int,
    ) -> None:
        """Draw text centered horizontally at a chosen vertical position."""
        image = font.render(text, True, color)
        self.screen.blit(image, image.get_rect(center=(config.WIDTH // 2, y)))
