from flexsim_env import FlexSimEnv
import tensorflow as tf
import numpy as np
import gym
import math
from tensorflow import keras
from collections import deque
import random

def main():
    env = FlexSimEnv(
        flexsimPath = "C:/Program Files/FlexSim 2023/program/flexsim.exe",
        modelPath = "D:/PHD_abbass/Flexsim_simulation/ChangeoverTimesRL.fsm",
        verbose = True,
        visible = True
        )
    env.seed(1)
    observation = env.reset()
    print(observation)
    env.render()
    done = False
    for i in range(1000):

        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        env.render()
    env._release_flexsim()
    input("Waiting for input to close FlexSim...")
    env.close()

if __name__ == "__main__":
    main()