# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:00:48 2020

@author: mahsa
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def Q_learning(env , x_start, x_goal, gamma, alpha, epsilon, max_Iter, max_step, wall_penalty, goal_state_reward):

        
    # Create the Q_table
    # Anamogous to the environment's dimension and a third dimension of size 4 for the four possible actions 
    # first serious of the x_env*y_env array: action UP
    # second serious of the x_env*y_env array: action LEFT
    # third serious of the x_env*y_env array: action RIGHT
    # fourth serious of the x_env*y_env array: action DOWN
    Q_table = np.zeros((4,np.shape(env)[0],np.shape(env)[1]))
    print("The Q_table is:")
    print(Q_table)
    
    x = np.array([0,0])
    Iter = 0
    num_Iter = []
    num_step = []
    path_reward = []
    cumulative_steps = []
    Q_table_before =  np.zeros((4,np.shape(env)[0],np.shape(env)[1]))
    Q_table_after =  np.zeros((4,np.shape(env)[0],np.shape(env)[1]))
    Q_change = 10 # an arbitrary large number to start the loop
      
    total_steps = 0
        
    
    while (Iter <= max_Iter):# and Q_change>0.0001):
    
        x[:] = x_start
        step = 0
        GoalReached = False
        total_r = 0
        Q_table_before[:] = Q_table
        
        while True:
            # Select an action according to epsilon-greedy policy
            rand_n = random.random()
            if rand_n <= epsilon:
               # Then choose a randon action for exploration
               act_index = random.randint(0,3) 
            else:     
               help_var = Q_table[:,x[0],x[1]]
               max_val = max(help_var)
               act_index = np.argmax(help_var)
               
               
            if act_index == 0: # action: Up   
               displ = [-1,0]
            
            elif act_index == 1: # action: Left
               displ = [0,-1]
            
            elif act_index == 2: # action: Right
               displ = [0,1]
            
            else: # action: Down
               displ = [1,0]
               
            x_tran = x + displ
            
            # Check if this displacement is allowed due to the boundaries and block cell
            if (x_tran[0]<0 or x_tran[0]>=np.shape(env)[0] or x_tran[1]<0 or x_tran[1]>=np.shape(env)[1] ):
                # Then the selected action will caues a collison with the boundary
                r = wall_penalty
                x_new = x # The agent will stay at its original position
                Q_new = r
            
            elif env[x_tran[0],x_tran[1]] == 1:
                # Then the selected action causes a collision with the blocked cells
                r = wall_penalty
                x_new = x # The agent will stay at its original position
                Q_new = r
            
            else: # The transition is possible
                x_new = x_tran
                if (x_new == x_goal).all():
                   r = goal_state_reward # The goal is reached!
                   GoalReached = True
                   Q_new = r
                else:
                   r = -1 # to encourage getting to the goal soon
                   Q_new = r + gamma*max(Q_table[:,x_new[0],x_new[1]])
                   
                   
            Q_table[act_index,x[0],x[1]] += alpha*(Q_new - Q_table[act_index,x[0],x[1]])
            x[:] = x_new
            step += 1
            total_r += r
            total_steps += 1
                
            if (GoalReached == True or step>max_step):
               print("Interation #:")
               print(Iter)
               print("Number of steps:")
               print(step)
               print("************************************************************")
               break
             
        num_step.append(step)
        path_reward.append(total_r)
        cumulative_steps.append(total_steps)
        Iter += 1
        num_Iter.append(Iter)
        Q_table_after[:] = Q_table
        Q_change = np.max(np.absolute(Q_table_after - Q_table_before))
        print("The max Q_change is:")
        print(Q_change)
        
    
    # Having the final Q_table now extract the optimal path
    print("The optimal path is:")
    x_opt_path = np.array([0,0])
    x_opt_path[:] = x_start
    goal_reached = False
    print(x_opt_path)
    
    opt_path_len = 0
    while (goal_reached == False and opt_path_len < 100): # if opt_path_len gets greater than 100 its means that the optimal path was not found. This is just a condition for not getting into an infinity loop here.
          val_h = Q_table[:,x_opt_path[0],x_opt_path[1]]
          opt_action = np.argmax(val_h)
          if opt_action == 0: # action: Up
               print("Up")
               delta_x = [-1,0]
            
          elif opt_action == 1: # action: Left
               print("Left")
               delta_x = [0,-1]
            
          elif opt_action == 2: # action: Right
               print("Right")
               delta_x = [0,1]
            
          else: # action: Down
               print("Down")
               delta_x = [1,0]
          
          x_opt_path = x_opt_path + delta_x
          print(x_opt_path)
          if (x_opt_path == x_goal).all():
             goal_reached = True
          
          opt_path_len += 1
    

    print("The length of the optimal path is:")
    print(opt_path_len)
    print("The total reward of the optimal path is:")
    print(goal_state_reward - (opt_path_len-1))
    # print("The final Q_table is:")
    # np.set_printoptions(formatter={'float': lambda Q_table: "{0:0.2f}".format(Q_table)})
    # print(Q_table)


    
    return [num_Iter, num_step, path_reward, cumulative_steps]











