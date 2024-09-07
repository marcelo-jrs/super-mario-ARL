# q_learning_agent.py
import numpy as np
import random

class QLearningAgent:
    def __init__(self, state_size, action_size, alpha=0.4, gamma=0.9, epsilon=0.2):
        self.state_size = state_size
        self.action_size = action_size
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.q_table = np.zeros((state_size, action_size))

    def choose_action(self, state):
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.action_size - 1)  # Explore
        else:
            return np.argmax(self.q_table[state])  # Exploit

    def update_q_value(self, state, action, reward, next_state):
        # Handle last state to prevent index out of bounds
        if next_state < self.state_size:  # Ensure next_state is within bounds
            best_next_action = np.argmax(self.q_table[next_state])
            self.q_table[state, action] = (1 - self.alpha) * self.q_table[state, action] + \
                                          self.alpha * (reward + self.gamma * self.q_table[next_state, best_next_action])
        else:
            # If it's the last state, just update with the reward and no next state consideration
            self.q_table[state, action] = (1 - self.alpha) * self.q_table[state, action] + self.alpha * reward
