import numpy as np
import pandas as pd
import player_agent as agent
import pygame

from constants import (
    RED,
    WHITE,
    BLUE,
    BLACK,
    OBSTACLE_SIZE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    INCREMENT,
)


class Obstacle:
    def __init__(self, x, y, color):
        self.obstacle_size = OBSTACLE_SIZE

        self.x = x
        self.y = y

        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.obstacle_size)
