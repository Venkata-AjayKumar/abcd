import numpy as np


class Experience(object):
    """Struct to encapsulate the experience of a single turn."""

    def __init__(self, state, action, reward, next_state, game_over, next_state_available_actions):
        """Initialize Experience

        Args:
          state: Shape (4, 4) numpy array, the state before the action was executed
          action: Number in range(4), action that was taken
          reward: Number, experienced reward
          next_state: Shape (4, 4) numpy array, the state after the action was executed
          game_over: boolean, whether next_state is a terminal state
          next_state_available_actions: Available actions from the next state
        """
        self.state = state
        self.action = action
        self.reward = reward
        self.next_state = next_state
        self.game_over = game_over
        self.next_state_available_actions = next_state_available_actions

    def __str__(self):
        return str((self.state, self.action, self.reward, self.next_state,
                    self.game_over, self.next_state_available_actions))

    def __repr__(self):
        return self.__str__()

    def get_id(self):
        return np.concatenate((self.state.ravel(), [self.action], self.next_state.ravel()))
