# Reinforcement-Learning

This implementation is part of a course project for the “Introduction to Artificial Intelligence” course, fall 2020.

The goal is for an agent to find the shortest path possible to a designated destination in a grid world environment with static obstacles. This path is aimed to be find in a learning procedure while the agent interacts with the environment. Therefore, the path that results in the maximum gained reward is learned.

Two algorithms of Q-learning and SARSA in the context of Reinforcement learning are used for this path planning problem. These algorithms are implemented in python are tested on the two following environments. (the second environment is taken from ref[1] for the purpose of performance comparison)

Four different actions of up/down/left/right were considered at each cell.  

The main formulation for the Q-table update is:

Q(s,a) ← Q(s,a)+ α [r+ γ max⁡ Q(s',a)- Q(s,a)]

Q(s,a): The action value for a state-action pair

s: current state

a: action

s': next state

r: reward

α: learning rate

γ: discount factor

The outputs of running the main.py script are as follows:

•	The optimal path’s cell coordinates step by step with the corresponding action at each step

•	The length of the optimal path which is the shortest path form the start cell to the goal cell

•	Graphs comparing the performance of the Q-learning algorithm with the SARSA algorithm

•	Graphs that show the effect of different learning rates on the performance of the algorithm 

•	Graphs that show the effect of different discount factor on the performance of the algorithm 

All the above outputs are generated for both environment 1 and environment 2

