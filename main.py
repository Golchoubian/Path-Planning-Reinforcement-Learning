# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:46:07 2020

@author: mahsa
"""

import env1
import env2
import env_ref
import Qlearning
import SARSA
import matplotlib.pyplot as plt
import time




# ****************************** Environment 1 ********************************* 
[env1 , x_start_env1, x_goal_env1] = env1.environment1()  
opt_path_reward_env1 = 10 - (16-1) # for environment 1


##**************** Q_learning vs. SARSA - Environment 1 ********************

gamma1000 = 0.5 # discount factor
alpha1000 = 0.1 # learning rate
epsilon1000 = 0.1
max_Iter1000 = 500
wall_penalty1000 = -2
goal_state_reward1000 = 10
max_step1000 = 2000 

t0 = time.time()
[num_Iter1001, num_step1001, path_reward1001, cumulative_steps1001] = Qlearning.Q_learning(env1 , x_start_env1, x_goal_env1, gamma1000, alpha1000, epsilon1000, max_Iter1000, max_step1000, wall_penalty1000, goal_state_reward1000)
t1 = time.time()

alpha1000 = 0.1 # learning rate for SARSA
[num_Iter1002, num_step1002, path_reward1002, cumulative_steps1002] = SARSA.SARSA_alg(env1 , x_start_env1, x_goal_env1, gamma1000, alpha1000, epsilon1000, max_Iter1000, max_step1000, wall_penalty1000, goal_state_reward1000)
t2 = time.time()

fig1001 = plt.figure()
ax = plt.subplot(111)
ax.plot(num_Iter1001, num_step1001, '-b', label='Q_learning')
ax.plot(num_Iter1002, num_step1002, ':k', label='SARSA')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("number of steps")
plt.show()
fig1001.savefig('number-of-steps-1000.png')
fig1001.savefig('number-of-steps-1000.pdf')

fig1002 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter1001, path_reward1001, '-b', label='Q_learning')
ax.plot(num_Iter1002, path_reward1002, ':k', label='SARSA')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("sum of rewards")
plt.show()
fig1002.savefig('sum-of-rewards-1000.png')
fig1002.savefig('sum-of-rewards-1000.pdf')

fig1003 = plt.figure()
ax = plt.subplot()
ax.plot(cumulative_steps1001, num_Iter1001,'-b', label='Q_learning')
ax.plot(cumulative_steps1002, num_Iter1002,':k', label='SARSA')
ax.legend()
plt.xlabel("cumulative steps")
plt.ylabel("Iteration")
plt.show()
fig1003.savefig('Iteration-steps-1000.png')
fig1003.savefig('Iteration-steps-1000.pdf')


Loss1001 =  path_reward1001
Loss1001[:] = [abs(number-opt_path_reward_env1)/max_Iter1000 for number in Loss1001]
Loss1002 =  path_reward1002
Loss1002[:] = [abs(number-opt_path_reward_env1)/max_Iter1000 for number in Loss1002]

fig1004 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter1001, Loss1001, '-b', label='Q_learning')
ax.plot(num_Iter1002, Loss1002, ':k', label='SARSA')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("Loss")
plt.show()
fig1004.savefig('Loss-1000.png')
fig1004.savefig('Loss-1000.pdf')  


print("Time elapsed for Q_learning (env1): ", t1-t0)     
print("Time elapsed for SARSA (env2): ", t2-t1) 


# *************** Q_learning - Environment 1 - Comparing parameter values ********************* 


#        # ---------- different Learning rates -------------

gamma2000 = 0.5 # discount factor
epsilon2000 = 0.1
max_Iter2000 = 500
wall_penalty2000 = -2
goal_state_reward2000 = 10
max_step2000 = 2000 
 
alpha2001 = 0.5 # learning rate     
[num_Iter2001, num_step2001, path_reward2001, cumulative_steps2001] = Qlearning.Q_learning(env1 , x_start_env1, x_goal_env1, gamma2000, alpha2001, epsilon2000, max_Iter2000, max_step2000, wall_penalty2000, goal_state_reward2000)
alpha2002 = 0.2
[num_Iter2002, num_step2002, path_reward2002, cumulative_steps2002] = Qlearning.Q_learning(env1 , x_start_env1, x_goal_env1, gamma2000, alpha2002, epsilon2000, max_Iter2000, max_step2000, wall_penalty2000, goal_state_reward2000)
alpha2003 = 0.1
[num_Iter2003, num_step2003, path_reward2003, cumulative_steps2003] = Qlearning.Q_learning(env1 , x_start_env1, x_goal_env1, gamma2000, alpha2003, epsilon2000, max_Iter2000, max_step2000, wall_penalty2000, goal_state_reward2000)


fig2001 = plt.figure()
ax = plt.subplot(111)
ax.plot(num_Iter2001, num_step2001, '-b', label='learning rate = 0.5')
ax.plot(num_Iter2002, num_step2002, '--r', label='learning rate = 0.2')
ax.plot(num_Iter2003, num_step2003, ':k', label='learning rate = 0.1')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("number of steps")
plt.show()
fig2001.savefig('number-of-steps-2000.png')
fig2001.savefig('number-of-steps2000.pdf')

fig2002 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter2001, path_reward2001, '-b', label='learning rate = 0.5')
ax.plot(num_Iter2002, path_reward2002, '--r', label='learning rate = 0.2')
ax.plot(num_Iter2003, path_reward2003, ':k', label='learning rate = 0.1')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("sum of rewards")
plt.show()
fig2002.savefig('sum-of-rewards-2000.png')
fig2002.savefig('sum-of-rewards-2000.pdf')


Loss2001 =  path_reward2001
Loss2001[:] = [abs(number-opt_path_reward_env1)/max_Iter2000 for number in Loss2001]
Loss2002 =  path_reward2002
Loss2002[:] = [abs(number-opt_path_reward_env1)/max_Iter2000 for number in Loss2002]
Loss2003 =  path_reward2003
Loss2003[:] = [abs(number-opt_path_reward_env1)/max_Iter2000 for number in Loss2003]

fig2003 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter2001, Loss2001, '-b', label='learning rate = 0.5')
ax.plot(num_Iter2002, Loss2002, '--r', label='learning rate = 0.2')
ax.plot(num_Iter2003, Loss2003, ':k', label='learning rate = 0.1')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("Loss")
plt.show()
fig2003.savefig('Loss-2000.png')
fig2003.savefig('Loss-2000.pdf')  




        ##---------- different discount factor -------------

alpha3000 = 0.2 # learning rate   
epsilon3000 = 0.1
max_Iter3000 = 500
wall_penalty3000 = -2
goal_state_reward3000 = 10
max_step3000 = 2000 

gamma3001 = 0.1 # discount factor
[num_Iter3001, num_step3001, path_reward3001, cumulative_steps3001] = Qlearning.Q_learning(env1 , x_start_env1, x_goal_env1, gamma3001, alpha3000, epsilon3000, max_Iter3000, max_step3000, wall_penalty3000, goal_state_reward3000)
gamma3002 = 0.3
[num_Iter3002, num_step3002, path_reward3002, cumulative_steps3002] = Qlearning.Q_learning(env1 , x_start_env1, x_goal_env1, gamma3002, alpha3000, epsilon3000, max_Iter3000, max_step3000, wall_penalty3000, goal_state_reward3000)
gamma3003 = 0.5
[num_Iter3003, num_step3003, path_reward3003, cumulative_steps3003] = Qlearning.Q_learning(env1 , x_start_env1, x_goal_env1, gamma3003, alpha3000, epsilon3000, max_Iter3000, max_step3000, wall_penalty3000, goal_state_reward3000)



fig3001 = plt.figure()
ax = plt.subplot(111)
ax.plot(num_Iter3001, num_step3001, '-b', label='discount factor = 0.1')
ax.plot(num_Iter3002, num_step3002, '--r', label='discount factor = 0.3')
ax.plot(num_Iter3003, num_step3003, ':k', label='discount factor = 0.5')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("number of steps")
plt.show()
fig3001.savefig('number-of-steps-3000.png')
fig3001.savefig('number-of-steps-3000.pdf')

fig3002 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter3001, path_reward3001, '-b', label='discount factor = 0.1')
ax.plot(num_Iter3002, path_reward3002, '--r', label='discount factor = 0.3')
ax.plot(num_Iter3003, path_reward3003, ':k', label='discount factor = 0.5')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("sum of rewards")
plt.show()
fig3002.savefig('sum-of-rewards-3000.png')
fig3002.savefig('sum-of-rewards-3000.pdf')


Loss3001 =  path_reward3001
Loss3001[:] = [abs(number-opt_path_reward_env1)/max_Iter3000 for number in Loss3001]
Loss3002 =  path_reward3002
Loss3002[:] = [abs(number-opt_path_reward_env1)/max_Iter3000 for number in Loss3002]
Loss3003 =  path_reward3003
Loss3003[:] = [abs(number-opt_path_reward_env1)/max_Iter3000 for number in Loss3003]

fig3003 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter3001, Loss3001, '-b', label='discount factor = 0.1')
ax.plot(num_Iter3002, Loss3002, '--r', label='discount factor = 0.3')
ax.plot(num_Iter3003, Loss3003, ':k', label='discount factor = 0.5')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("Loss")
plt.show()
fig3003.savefig('Loss-3000.png')
fig3003.savefig('Loss-3000.pdf')  




# # _____________________________________________________________________________

##******************** Environment 2 *********************
[env2 , x_start_env2, x_goal_env2] = env2.environment2()
opt_path_reward_env2 = 10 - (35-1)  # 100 - (35-1) # for environment 1



##******************** Q_learning vs SARSA - Environment 2 *********************

gamma4000 = 0.5 # discount factor
epsilon4000 = 0.1
max_Iter4000 = 3500 
alpha4000 = 0.1 # learning rate for Q_learning
wall_penalty4000 = -2 #
goal_state_reward4000 = 10 
max_step4000 = 4000 

t3 = time.time()
[num_Iter4001, num_step4001, path_reward4001, cumulative_steps4001] = Qlearning.Q_learning(env2 , x_start_env2, x_goal_env2, gamma4000, alpha4000, epsilon4000, max_Iter4000, max_step4000, wall_penalty4000, goal_state_reward4000)
t4 = time.time()

alpha4000 = 0.1 # learning rate for SARSA
[num_Iter4002, num_step4002, path_reward4002, cumulative_steps4002] = SARSA.SARSA_alg(env2 , x_start_env2, x_goal_env2, gamma4000, alpha4000, epsilon4000, max_Iter4000, max_step4000, wall_penalty4000, goal_state_reward4000)
t5 = time.time()

fig4001 = plt.figure()
ax = plt.subplot(111)
ax.plot(num_Iter4001, num_step4001, '-b', label='Q_learning')
ax.plot(num_Iter4002, num_step4002, ':k', label='SARSA')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("number of steps")
plt.show()
fig4001.savefig('number-of-steps-4000.png')
fig4001.savefig('number-of-steps-4000.pdf')


fig4002 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter4001, path_reward4001, '-b', label='Q_learning')
ax.plot(num_Iter4002, path_reward4002, ':k', label='SARSA')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("sum of rewards")
plt.show()
fig4002.savefig('sum-of-rewards-4000.png')
fig4002.savefig('sum-of-rewards-4000.pdf')


fig4003 = plt.figure()
ax = plt.subplot()
ax.plot(cumulative_steps4001, num_Iter4001,'-b', label='Q_learning')
ax.plot(cumulative_steps4002, num_Iter4002,':k', label='SARSA')
ax.legend()
plt.xlabel("cumulative steps")
plt.ylabel("Iteration")
plt.show()
fig4003.savefig('Iteration-steps-4000.png')
fig4003.savefig('Iteration-steps-4000.pdf')


Loss4001 =  path_reward4001
Loss4001[:] = [abs(number-opt_path_reward_env2)/max_Iter4000 for number in Loss4001]
Loss4002 =  path_reward4002
Loss4002[:] = [abs(number-opt_path_reward_env2)/max_Iter4000 for number in Loss4002]

fig4004 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter4001, Loss4001, '-b', label='Q_learning')
ax.plot(num_Iter4002, Loss4002, ':k', label='SARSA')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("Loss")
plt.show()
fig4004.savefig('Loss-env2-4000.png')
fig4004.savefig('Loss-env2-4000.pdf')  

print("Time elapsed for Q_earning (env2): ", t4-t3)
print("Time elapsed for SARSA (env2): ", t5-t4)



# # # # ---------- different Learning rates - Q_learning -  Environment 2  -------------

gamma5000 = 0.5 #discount factor
epsilon5000 = 0.1
max_Iter5000 = 3000 
wall_penalty5000 = -2
goal_state_reward5000 = 10
max_step5000 = 2000

alpha5001 = 0.5 # learning rate
[num_Iter5001, num_step5001, path_reward5001, cumulative_steps5001] = Qlearning.Q_learning(env2 , x_start_env2, x_goal_env2, gamma5000, alpha5001, epsilon5000, max_Iter5000, max_step5000, wall_penalty5000, goal_state_reward5000)
alpha5002 = 0.2
[num_Iter5002, num_step5002, path_reward5002, cumulative_steps5002] = Qlearning.Q_learning(env2 , x_start_env2, x_goal_env2, gamma5000, alpha5002, epsilon5000, max_Iter5000, max_step5000, wall_penalty5000, goal_state_reward5000)
alpha5003 = 0.1
[num_Iter5003, num_step5003, path_reward5003, cumulative_steps5003] = Qlearning.Q_learning(env2 , x_start_env2, x_goal_env2, gamma5000, alpha5003, epsilon5000, max_Iter5000, max_step5000, wall_penalty5000, goal_state_reward5000)


fig5001 = plt.figure()
ax = plt.subplot(111)
ax.plot(num_Iter5001, num_step5001, '-b', label='learning rate = 0.5')
ax.plot(num_Iter5002, num_step5002, '--r', label='learning rate = 0.2')
ax.plot(num_Iter5003, num_step5003, ':k', label='learning rate = 0.1')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("number of steps")
plt.show()
fig5001.savefig('number-of-steps_5000.png')
fig5001.savefig('number-of-steps_5000.pdf')

fig5002 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter5001, path_reward5001, '-b', label='learning rate = 0.5')
ax.plot(num_Iter5002, path_reward5002, '--r', label='learning rate = 0.2')
ax.plot(num_Iter5003, path_reward5003, ':k', label='learning rate = 0.1')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("sum of rewards")
plt.show()
fig5002.savefig('sum-of-rewards_5000.png')
fig5002.savefig('sum-of-rewards_5000.pdf')


Loss5001 =  path_reward5001
Loss5001[:] = [abs(number-opt_path_reward_env2)/max_Iter5000 for number in Loss5001]
Loss5002 =  path_reward5002
Loss5002[:] = [abs(number-opt_path_reward_env2)/max_Iter5000 for number in Loss5002]
Loss5003 =  path_reward5003
Loss5003[:] = [abs(number-opt_path_reward_env2)/max_Iter5000 for number in Loss5003]

fig5003 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter5001, Loss5001, '-b', label='learning rate = 0.5')
ax.plot(num_Iter5002, Loss5002, '--r', label='learning rate = 0.2')
ax.plot(num_Iter5003, Loss5003, ':k', label='learning rate = 0.1')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("Loss")
plt.show()
fig5003.savefig('Loss_5000.png')
fig5003.savefig('Loss_5000.pdf')  



# # # ---------- different Discount factor - Q_learning -  Environment 2  -------------

alpha6000 = 0.2 # learning rate
epsilon6000 = 0.1
max_Iter6000 = 3000
wall_penalty6000 = -2
goal_state_reward6000 = 10
max_step6000 = 2000 

gamma6001 = 0.5 # discount factor
[num_Iter6001, num_step6001, path_reward6001, cumulative_steps6001] = Qlearning.Q_learning(env2 , x_start_env2, x_goal_env2, gamma6001, alpha6000, epsilon6000, max_Iter6000, max_step6000, wall_penalty6000, goal_state_reward6000)
gamma6002 = 0.45 # discount factor
[num_Iter6002, num_step6002, path_reward6002, cumulative_steps6002] = Qlearning.Q_learning(env2 , x_start_env2, x_goal_env2, gamma6002, alpha6000, epsilon6000, max_Iter6000, max_step6000, wall_penalty6000, goal_state_reward6000)
gamma6003 = 0.35 # discount factor
[num_Iter6003, num_step6003, path_reward6003, cumulative_steps6003] = Qlearning.Q_learning(env2 , x_start_env2, x_goal_env2, gamma6003, alpha6000, epsilon6000, max_Iter6000, max_step6000, wall_penalty6000, goal_state_reward6000)


fig6001 = plt.figure()
ax = plt.subplot(111)
ax.plot(num_Iter6001, num_step6001, '-b', label='discount factor = 0.5')
ax.plot(num_Iter6002, num_step6002, '--r', label='discount factor = 0.45')
ax.plot(num_Iter6003, num_step6003, ':k', label='discount factor = 0.35')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("number of steps")
plt.show()
fig6001.savefig('number-of-steps_6000.png')
fig6001.savefig('number-of-steps_6000.pdf')

fig6002 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter6001, path_reward6001, '-b', label='discount factor = 0.5')
ax.plot(num_Iter6002, path_reward6002, '--r', label='discount factor = 0.45')
ax.plot(num_Iter6003, path_reward6003, ':k', label='discount factor = 0.35')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("sum of rewards")
plt.show()
fig6002.savefig('sum-of-rewards_6000.png')
fig6002.savefig('sum-of-rewards_6000.pdf')



Loss6001 =  path_reward6001
Loss6001[:] = [abs(number-opt_path_reward_env2)/max_Iter6000 for number in Loss6001]
Loss6002 =  path_reward6002
Loss6002[:] = [abs(number-opt_path_reward_env2)/max_Iter6000 for number in Loss6002]
Loss6003 =  path_reward6003
Loss6003[:] = [abs(number-opt_path_reward_env2)/max_Iter6000 for number in Loss6003]

fig6003 = plt.figure()
ax = plt.subplot()
ax.plot(num_Iter6001, Loss6001, '-b', label='discount factor = 0.5')
ax.plot(num_Iter6002, Loss6002, '--r', label='discount factor = 0.45')
ax.plot(num_Iter6003, Loss6003, ':k', label='discount factor = 0.35')
ax.legend()
plt.xlabel("number of iteration")
plt.ylabel("Loss")
plt.show()
fig6003.savefig('Loss_6000.png')
fig6003.savefig('Loss_6000.pdf')  


