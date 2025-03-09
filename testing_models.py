import sys
import gym
from flexsim_env import FlexSimEnv
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import PPO, DQN
from stable_baselines3.common.env_util import make_vec_env


def main():
    env = FlexSimEnv(
        flexsimPath = "C:/Program Files/FlexSim 2023/program/flexsim.exe",
        modelPath = "D:/PHD_abbass/Flexsim_simulation/Robot_operators_one_room_RL.fsm",
        verbose = False,
        visible = True
    
        )
    model = PPO.load("robot_distance_cost_harvested_reward")

    for i in range(1):
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