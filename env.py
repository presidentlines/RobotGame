import numpy as np
import pandas as pd
from constants import INCREMENT


class Environment:
    def __init__(self):
        self.states = {}
        for i in range(4):
            for j in range(4):
                self.states[(i, j)] = (INCREMENT * i + 100, INCREMENT * j + 100)

        self.negative_states = [(1, 3), (1, 2), (3, 2)]
        self.reward_state = (3, 3)

        self.curr_state = (0, 0)

    def get_terminal_states(self):
        pass

    def get_state(self) -> tuple[int, int]:
        return self.curr_state

    def reset(self) -> tuple[int, int]:
        self.curr_state = (0, 0)
        return self.states[(0, 0)]

    def execute_action(self, action: str) -> tuple[int, tuple[int, int], bool]:
        """
        Returns reward, next state, finished
        """
        print(action)
        if action == "LEFT":
            if self.curr_state[0] == 0:
                return -1, self.curr_state, False

            x_state = self.curr_state[0] - 1
            y_state = self.curr_state[1]

        elif action == "RIGHT":
            if self.curr_state[0] == 3:
                return -1, self.curr_state, False

            x_state = self.curr_state[0] + 1
            y_state = self.curr_state[1]

        elif action == "UP":
            if self.curr_state[1] == 0:
                return -1, self.curr_state, False

            x_state = self.curr_state[0]
            y_state = self.curr_state[1] - 1

        elif action == "DOWN":
            if self.curr_state[1] == 3:
                return -1, self.curr_state, False

            x_state = self.curr_state[0]
            y_state = self.curr_state[1] + 1

        self.curr_state = (x_state, y_state)

        if self.curr_state in self.negative_states:
            return -10, self.curr_state, True
        if self.curr_state in self.reward_state:
            return 10, self.curr_state, True

        return -1, self.curr_state, False
