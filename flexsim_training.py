import sys
import gym
import time
from flexsim_env import FlexSimEnv
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import PPO, DQN
from stable_baselines3.common.env_util import make_vec_env

sys.modules["gym"] = gym

def main():
    print("Initializing FlexSim environment...")

    # Create a FlexSim OpenAI Gym Environment
    env = FlexSimEnv(
        flexsimPath = "C:/Program Files/FlexSim 2023/program/flexsim.exe",
        modelPath = "D:/PHD_abbass/Flexsim_simulation/Robot_operators_one_room_RL_autosave_Copie_autosave.fsm",
        verbose = True,
        visible = False
    
        )
    #observation = env.reset()
    #print("The observation space data type from flexsim:", observation.dtype)
    check_env(env) # Check that an environment follows Gym API.
    time.sleep(1)
    # Training a baselines3 PPO model in the environment
    model = PPO("MlpPolicy", env, verbose=1)
    
    model.learning_rate = 0.1
    print('learning rate:', model.learning_rate)
    print("Training model...")
    model.learn(total_timesteps=5000)
    
    # save the model

    print("Saving model...")
    model.save("Robot_operators_one_room_RL_autosave_Copie_autosave")

    input("Waiting for input to do some test runs...")

    # Run test episodes using the trained model
    for i in range(2):
        env.seed(i)
        observation = env.reset()
        env.render()
        done = False
        rewards = []
        while not done:
            action, _states = model.predict(observation)
            observation, reward, done, info = env.step(action)
            env.render()
            rewards.append(reward)
            if done:
                cumulative_reward = sum(rewards)
                print("Reward: ", cumulative_reward, "\n")
    env._release_flexsim()

    input("Waiting for input to close FlexSim...")
    env.close()

if __name__ == "__main__":
    main()