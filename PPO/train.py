import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from level_generation_env import LevelGenerationEnv

def make_env(env_id, width, height, max_ground_height):
    """
    Utility function to create a new environment instance.
    """
    def _init():
        return LevelGenerationEnv(width=width, height=height, max_ground_height=max_ground_height)
    return _init

def main():
    # Set environment parameters
    width = 20
    height = 16
    max_ground_height = 3

    # Create the vectorized environment with 4 unique instances of LevelGenerationEnv
    env = make_vec_env(make_env('LevelGenerationEnv', width, height, max_ground_height), n_envs=4)

    # Create the PPO agent
    model = PPO("MlpPolicy", env, verbose=1)

    # Train the model
    model.learn(total_timesteps=10000)

    # Save the model
    model.save("ppo_mario_level_generator")

    # Test the trained model on a single instance of the environment
    test_env = LevelGenerationEnv(width=width, height=height, max_ground_height=max_ground_height)
    obs, _ = test_env.reset()

    for step in range(test_env.width):
        action, _states = model.predict(obs)
        obs, rewards, done, _, _ = test_env.step(action)
        test_env.render()
        if done:
            break

if __name__ == "__main__":
    main()
