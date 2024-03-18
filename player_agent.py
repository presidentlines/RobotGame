import pygame
import numpy as np

from constants import BLACK, WHITE, RED, BLUE


# Define player and obstacle classes
class Player:
    def __init__(
        self,
        x=10,
        y=10,
        player_size=20,
        screen_width=800,
        screen_height=600,
        player_speed=20,
    ):
        self.x = x
        self.y = y

        self.max_x = screen_width - player_size
        self.max_y = screen_height - player_size

        self.player_speed = player_speed
        self.player_size = player_size

        if x is None:
            self.x = np.random.choice(np.arange(0 + self.player_size, self.max_x))
        if y is None:
            self.y = np.random.choice(np.arange(0 + self.player_size, self.max_y))

        self.color = WHITE

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.player_size)

    def move(self, direction):
        if direction == "up":
            self.y -= self.player_speed
        elif direction == "down":
            self.y += self.player_speed
        elif direction == "left":
            self.x -= self.player_speed
        elif direction == "right":
            self.x += self.player_speed

        # Ensure player stays within boundaries chatgpt logic
        self.x = max(0, min(self.x, self.max_x))
        self.y = max(0, min(self.y, self.max_y))
