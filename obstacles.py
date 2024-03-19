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

    # # Function to generate random valid positions for obstacles
    # def generate_valid_position(self, agen):
    #     while True:
    #         x = np.random.randint(0, SCREEN_WIDTH - obstacle_SIZE)
    #         y = np.random.randint(0, SCREEN_HEIGHT - obstacle_SIZE)
    #         # Check if position collides with any existing object
    #         for obj in objects:
    #             if (
    #                 abs(obj.x - x) < obstacle_SIZE + PLAYER_SIZE
    #                 and abs(obj.y - y) < obstacle_SIZE + PLAYER_SIZE
    #             ):
    #                 continue  # Position collides, try again
    #         return (x, y)
