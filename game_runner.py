import numpy as np
import pandas as pd
import pygame
import plotly.graph_objects as go
from time import sleep

from obstacles import Obstacle
from player_agent import Player

import env

from constants import (
    BLACK,
    RED,
    BLUE,
    GREEN,
    WHITE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    OBSTACLE_SIZE,
    PLAYER_SIZE,
)


class GameRunner:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Obstacle Chase!")
        self.clock = pygame.time.Clock()

        self.environment = env.Environment()
        # How fast the game runs
        self.fps = 5

        self.num_rows = 4
        self.num_cols = 4

        # Initialize player and obstacles
        player_x, player_y = self.environment.states[(0, 0)]
        self.player = Player(x=player_x, y=player_y)

        self.obstacles = []
        obstacle1_x, obstacle1_y = self.environment.states[(1, 3)]
        obstacle2_x, obstacle2_y = self.environment.states[(1, 2)]
        obstacle3_x, obstacle3_y = self.environment.states[(3, 2)]
        obstacle4_x, obstacle4_y = self.environment.states[(3, 3)]

        self.obstacles.append(Obstacle(x=obstacle1_x, y=obstacle1_y, color=RED))
        self.obstacles.append(Obstacle(x=obstacle2_x, y=obstacle2_y, color=RED))
        self.obstacles.append(Obstacle(x=obstacle3_x, y=obstacle3_y, color=RED))
        self.obstacles.append(Obstacle(x=obstacle4_x, y=obstacle4_y, color=GREEN))

    def run_game(self):
        # Game loop
        running = True
        while running:

            game_end = False
            curr_state = self.environment.reset()
            cum_rewards = [0]

            while not game_end and running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                possibilities = [
                    pygame.K_UP,
                    pygame.K_DOWN,
                    pygame.K_LEFT,
                    pygame.K_RIGHT,
                ]
                keys = pygame.key.get_pressed()
                if any([keys[p] for p in possibilities]):
                    event = pygame.event.get()
                    dt = self.clock.tick(self.fps)
                    # Get player input
                    if keys[pygame.K_UP]:
                        reward, next_state, game_end = self.environment.execute_action(
                            "UP"
                        )
                    if keys[pygame.K_DOWN]:
                        reward, next_state, game_end = self.environment.execute_action(
                            "DOWN"
                        )
                    if keys[pygame.K_LEFT]:
                        reward, next_state, game_end = self.environment.execute_action(
                            "LEFT"
                        )
                    if keys[pygame.K_RIGHT]:
                        reward, next_state, game_end = self.environment.execute_action(
                            "RIGHT"
                        )
                    sleep(0.1)

                    curr_state = next_state
                    cum_rewards.append(cum_rewards[-1] + reward)

                    if game_end:
                        self.plot_rewards(cum_rewards)

                self.draw_game_screen(self.environment.states[curr_state])

    def draw_game_screen(self, curr_location):
        self.screen.fill(BLACK)
        self.draw_lines(
            num_rows=self.num_rows, num_cols=self.num_cols, grid_color=WHITE
        )
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        self.player.draw(self.screen, curr_location)
        pygame.display.flip()

    def plot_rewards(self, rewards):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(range(len(rewards))), y=rewards))
        fig.update_layout(title_text="Cumulative Rewards")
        fig.update_yaxes(title_text="Rewards")
        fig.update_xaxes(title_text="Iterations")
        fig.show()

    def draw_lines(self, num_rows, num_cols, grid_color):
        cell_size = 197
        margin = 5
        # Draw grid lines
        for row in range(num_rows + 1):
            y = row * cell_size + margin
            pygame.draw.line(
                self.screen, grid_color, (margin, y), (SCREEN_WIDTH - margin, y)
            )
        for col in range(num_cols + 1):
            x = col * cell_size + margin
            pygame.draw.line(
                self.screen, grid_color, (x, margin), (x, SCREEN_HEIGHT - margin)
            )


if __name__ == "__main__":
    game_runner = GameRunner()
    game_runner.run_game()
