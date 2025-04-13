# 🍄 FlexSim + Reinforcement Learning: Mushroom Harvesting Optimization

This repository demonstrates the integration of **FlexSim** simulation software with **Reinforcement Learning (RL)** using Python and `stable-baselines3`, to optimize mushroom production. A robot agent is trained to harvest mushrooms efficiently within a simulated environment.

## 📦 Main Components

- **`flexsim_env.py`**  
  Defines the `FlexSimEnv` class, a custom environment that subclasses `gym.Env`. It communicates with FlexSim via sockets, enabling RL interaction with the simulation.

- **`flexsim_training.py`**  
  Provides a simple `main()` function that:
  - Initializes the `FlexSimEnv`
  - Trains an RL agent using `stable-baselines3`
  - Saves and evaluates the trained model

- **`flexsim_inference.py`**  
  Hosts a lightweight inference server using `FlexSimInferenceServer` (a subclass of `BaseHTTPRequestHandler`).  
  Loads the saved model and handles HTTP requests to return an action based on observations.  
  ⚠️ *This is a basic example and not production-ready. For real-world deployments, enhance security and robustness.*

## 🧠 RL Framework

- [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3) (e.g., PPO, A2C)
- [Gym](https://github.com/openai/gym)

## 🚀 Use Case

A robotic harvesting agent learns to optimize decisions in a mushroom farm simulation powered by FlexSim. This showcases the potential of combining discrete-event simulation and reinforcement learning for smart manufacturing and agricultural automation.

---
