# Reinforcement-Learning

This implementation is part of a course project for the “Introduction to Artificial Intelligence” course, fall 2020.
The goal is for an agent to find the shortest path possible to a designated destination in a grid world environment with static obstacles. This path is aimed to be find in a learning procedure while the agent interacts with the environment. Therefore, the path that results in the maximum gained reward is learned.
Two algorithms of Q-learning and SARSA in the context of Reinforcement learning are used for this path planning problem. These algorithms are implemented in python are tested on the two following environments. (the second environment is taken from ref[1] for the purpose of performance comparison)
Four different actions of up/down/left/right were considered at each cell.  
The main formulation for the Q-table update is:
Q(s,a) □(←) Q(s,a)+ α[r+γ  max┬a⁡〖Q(s^',a)-Q(s,a)〗]
