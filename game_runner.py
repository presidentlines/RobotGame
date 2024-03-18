import numpy as np
import pandas as pd
import pygame

from obstacles import Obstacle
from player_agent import Player

from constants import BLACK

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 20
OBSTACLE_SIZE = 20
PLAYER_SPEED = 5
OBSTACLE_SPEED = 3


class GameRunner:
    def __init__(self):
        pass

    def run(self):

        # Initialize Pygame
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Obstacle Chase!")
        clock = pygame.time.Clock()

        # How fast the game runs
        fps = 10

        # Initialize player and obstacles
        player = Player()

        # Create random arrays of ints spaced at 30 points away from each other to initialize values of x and y
        random_xs = np.random.choice(
            np.linspace(50, SCREEN_WIDTH - OBSTACLE_SIZE, 30).astype(int),
            3,
            replace=False,
        )
        random_ys = np.random.choice(
            np.linspace(50, SCREEN_HEIGHT - OBSTACLE_SIZE, 30).astype(int),
            3,
            replace=False,
        )
        obstacles = [
            Obstacle(x=random_xs[i], y=random_ys[i]) for i in range(3)
        ]  # Create 3 obstacles

        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pressed = pygame.key.get_pressed()
            if pressed:
                breakpoint()
                dt = clock.tick(fps)
                screen.fill(BLACK)
                {obstacle.draw(screen) for obstacle in obstacles}
                player.draw(screen)

                {obstacle.move_towards(player) for obstacle in obstacles}
                # Get player input
                if keys[pygame.K_UP]:
                    player.move("up")
                if keys[pygame.K_DOWN]:
                    player.move("down")
                if keys[pygame.K_LEFT]:
                    player.move("left")
                if keys[pygame.K_RIGHT]:
                    player.move("right")
                pygame.display.flip()


if __name__ == "__main__":
    game_runner = GameRunner()
    game_runner.run()
