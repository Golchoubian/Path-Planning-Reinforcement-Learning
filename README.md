# Reinforcement-Learning

This implementation is part of a course project for the “Introduction to Artificial Intelligence” course, fall 2020.

The goal is for an agent to find the shortest path possible to a designated destination in a grid world environment with static obstacles. This path is aimed to be find in a learning procedure while the agent interacts with the environment. Therefore, the path that results in the maximum gained reward is learned.

Two algorithms of Q-learning and SARSA in the context of Reinforcement learning are used for this path planning problem. These algorithms are implemented in python are tested on the two following environments. (the second environment is taken from Ref[1] for the purpose of performance comparison)

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


Ref[1]: Wang, Xiaoqi, Lina Jin, and Haiping Wei. "The Shortest Path Planning Based on Reinforcement Learning." In Journal of Physics: Conference Series, vol. 1584, no. 1, p. 012006. IOP Publishing, 2020.

•	Graphs comparing the performance of the Q-learning algorithm with the SARSA algorithm

•	Graphs that show the effect of different learning rates on the performance of the algorithm 

•	Graphs that show the effect of different discount factor on the performance of the algorithm 

All the above outputs are generated for both environment 1 and environment 2

An example output for comparison between Q_learning and SARSA algorithm on environment 1 is given below:

The optimal path is:
[0 0]
Right
[0 1]
Right
[0 2]
Right
[0 3]
Down
[1 3]
Right
[1 4]
Down
[2 4]
Down
[3 4]
Right
[3 5]
Right
[3 6]
Right
[3 7]
Right
[3 8]
Down
[4 8]
Down
[5 8]
Left
[5 7]
Down
[6 7]
Left
[6 6]

The length of the optimal path is:
16


