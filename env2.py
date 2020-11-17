# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:06:46 2020

@author: mahsa
"""

def environment2():
    
    import numpy as np
    
    x_goal_env2 = np.array([17, 19])
    x_start_env2 = np.array([0,1])
    
    # Building the environment 2
    # Environment 1 is a 20 by 20 grid world
    # Each blocked cell has a value of 1 in the environment array 
    env2 = np.zeros((20,20), dtype = np.uint8)
    # first gruop of blocks
    env2[1,1] = 1
    env2[1,2] = 1
    env2[1,3] = 1
    env2[1,4] = 1
    # second group of blocks
    env2[4,2] = 1
    env2[4,3] = 1
    env2[4,4] = 1
    env2[5,3] = 1
    env2[6,3] = 1
    env2[7,3] = 1
    # third group of blocks
    env2[2,6] = 1
    env2[3,6] = 1
    env2[4,6] = 1
    env2[5,6] = 1
    env2[6,6] = 1
    env2[7,6] = 1
    env2[8,6] = 1
    env2[9,6] = 1
    env2[9,5] = 1
    env2[9,4] = 1
    env2[9,3] = 1
    env2[9,2] = 1
    env2[9,1] = 1
    env2[8,1] = 1
    env2[10,1] = 1
    env2[11,1] = 1
    env2[12,1] = 1
    env2[13,1] = 1
    env2[14,1] = 1
    env2[15,1] = 1
    env2[16,1] = 1
    env2[17,1] = 1
    env2[18,1] = 1
    # fourth group of blocks
    env2[12,3] = 1
    env2[12,4] = 1
    env2[12,5] = 1
    env2[12,6] = 1
    env2[12,7] = 1
    env2[13,3] = 1
    env2[14,3] = 1
    env2[15,3] = 1
    env2[16,3] = 1
    env2[17,3] = 1
    # 5th group of blocks
    env2[14,6] = 1
    env2[15,6] = 1
    env2[16,6] = 1
    env2[17,6] = 1
    env2[17,5] = 1
    env2[17,7] = 1
    env2[17,8] = 1
    env2[17,9] = 1
    env2[17,10] = 1
    env2[18,9] = 1
    env2[19,9] = 1
    # 6th group of blocks
    env2[5,9] = 1
    env2[6,9] = 1
    env2[7,9] = 1
    env2[8,9] = 1
    env2[9,9] = 1
    env2[10,9] = 1
    env2[11,9] = 1
    env2[12,9] = 1
    env2[13,9] = 1
    env2[14,9] = 1
    env2[15,9] = 1
    # 7th group of blocks
    env2[1,12] = 1
    env2[1,13] = 1
    env2[1,14] = 1
    env2[1,15] = 1
    env2[1,16] = 1
    # 8th group of blocks
    env2[3,10] = 1
    env2[3,11] = 1
    env2[3,12] = 1
    env2[3,13] = 1
    env2[3,14] = 1
    # 9th group of blocks
    env2[2,18] = 1
    env2[3,18] = 1
    env2[4,18] = 1
    env2[5,18] = 1
    env2[6,18] = 1
    env2[7,18] = 1
    env2[8,18] = 1
    env2[9,18] = 1
    env2[6,17] = 1
    env2[6,16] = 1
    env2[6,15] = 1
    env2[6,14] = 1
    env2[6,13] = 1
    # 10th group of blocks
    env2[9,16] = 1
    env2[9,15] = 1
    env2[9,14] = 1
    env2[9,13] = 1
    env2[9,12] = 1
    env2[10,12] = 1
    env2[11,12] = 1
    env2[12,12] = 1
    env2[13,12] = 1
    env2[14,12] = 1
    env2[15,12] = 1
    env2[16,12] = 1
    env2[16,13] = 1
    env2[16,14] = 1
    env2[16,15] = 1
    env2[16,16] = 1
    # 11th group of blocks
    env2[13,14] = 1
    env2[13,15] = 1
    env2[13,16] = 1
    env2[13,17] = 1
    env2[13,18] = 1
    env2[14,18] = 1
    env2[15,18] = 1
    env2[16,18] = 1
    env2[17,18] = 1
    
    # print("The environment is:")
    # print(env2)
    return [env2 , x_start_env2, x_goal_env2]
