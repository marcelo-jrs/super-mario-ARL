from level_generator_env import LevelGenerationEnv
from q_learning_agent import QLearningAgent

def main():
    # Initialize environment and agent
    env = LevelGenerationEnv(width=20, height=16, max_ground_height=3)  # Level portion size
    agent = QLearningAgent(state_size=20, action_size=4)

    # Training loop
    for episode in range(10):  # You can increase this number for longer training
        state = 0  # Start at the first tile position
        env.reset()
        total_reward = 0
        
        print(f"\n--- Episode {episode + 1} ---")
        
        for t in range(env.width):  # Generate 1 full portion of level (20 columns)
            # Agent chooses an action
            action = agent.choose_action(state)
            
            # Environment responds to the action
            next_state, reward, done, _ = env.step(action)
            
            # Agent learns from the action's reward
            agent.update_q_value(state, action, reward, state + 1)
            
            state += 1
            total_reward += reward
            
            if done:
                break

        # Display the generated level after each episode
        env.render()
        print(f"Total Reward: {total_reward}")

if __name__ == "__main__":
    main()
