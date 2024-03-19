import pygame
import numpy as np

from constants import (
    BLACK,
    RED,
    BLUE,
    WHITE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    PLAYER_SIZE,
    INCREMENT,
)


# Define player and obstacle classes
class Player:
    def __init__(
        self,
        x,
        y,
    ):
        self.x = x
        self.y = y

        self.color = WHITE
        self.player_size = PLAYER_SIZE

    def draw(self, screen, state):
        pygame.draw.circle(screen, self.color, (state[0], state[1]), self.player_size)
