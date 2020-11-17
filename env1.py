# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:45:07 2020

@author: mahsa
"""
def environment1():

    import numpy as np
    
    x_start_env1 = np.array([0,0])
    x_goal_env1 = np.array([6, 6])
    
    # Building the environment 1 
    # Environment 1 is a 9 by 9 grid world
    # Each blocked cell has a value of 1 in the environment array 
    env1 = np.zeros((9,9), dtype = np.uint8)
    # first gruop of blocks
    env1[1,2] = 1
    env1[2,1] = 1
    env1[2,2] = 1
    env1[3,1] = 1
    # second group of blocks
    env1[0,5] = 1
    env1[1,5] = 1
    env1[2,5] = 1
    # third group of blocks
    env1[5,0] = 1
    env1[5,1] = 1
    env1[5,2] = 1
    env1[5,3] = 1
    env1[6,2] = 1
    # fourth group of blocks
    env1[4,5] = 1
    env1[5,5] = 1
    env1[6,5] = 1
    env1[7,5] = 1
    env1[4,6] = 1
    env1[4,7] = 1
    env1[7,6] = 1
    
    
    # print("The environment is:")
    # print(env1)

    return [env1 , x_start_env1, x_goal_env1]