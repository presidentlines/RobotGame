import numpy as np
import pandas as pd
import player_agent as agent
import pygame

from constants import RED, WHITE, BLUE, BLACK


class Obstacle:
    def __init__(
        self,
        x,
        y,
        obstacle_size=20,
        screen_width=800,
        screen_height=600,
        obstacle_speed=13,
    ):

        self.max_x = screen_width - obstacle_size
        self.max_y = screen_height - obstacle_size

        self.min_x = 0 + obstacle_size
        self.min_y = 0 + obstacle_size

        self.obstacle_speed = obstacle_speed
        self.obstacle_size = obstacle_size

        if x is None:
            x = np.random.choice(np.arange(self.min_x, self.max_x))
        self.x = x

        if y is None:
            y = np.random.choice(np.arange(self.min_y, self.max_y))
        self.y = y

        self.color = BLUE

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.obstacle_size)

    def move_towards(self, player):
        # Simplistic approach: move directly towards the player
        dx = player.x - self.x
        dy = player.y - self.y

        def horiz_move():
            self.x += self.obstacle_speed * (1 if dx > 0 else -1)

        def vert_move():
            self.y += self.obstacle_speed * (1 if dy > 0 else -1)

        # 80% chance we move in the direction closest to the agent
        move_correctly = np.random.uniform() > 0.2

        # If we are further away in x then we are in y
        if move_correctly and abs(dx) > abs(dy):
            horiz_move()
        elif move_correctly and abs(dy) > abs(dx):
            vert_move()
        else:
            horiz_move() if np.random.uniform() > 0.5 else vert_move()

        # Ensure obstacle stays within boundaries (similar to player)
        self.x = max(self.min_x, min(self.x, self.max_x))
        self.y = max(self.min_y, min(self.y, self.max_y))

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
