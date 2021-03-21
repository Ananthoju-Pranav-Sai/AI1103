import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import random

count=0
size=1000000            
for x in range(size) :
    d = np.random.randint(low=1,high=7,size=3)  #number of dots on the face showing up for the three dice
    if (d[0]==d[1]) and (d[1]==d[2]) :      
        count=count+1
sim_prob = count/size
theo_prob = 1/36
print("Theoretical probability : ",theo_prob)
print("simulated probability : ",sim_prob)
cases=['E']
x = np.arange(len(cases))
plt.bar(x + 0.00, theo_prob, color = 'red', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, sim_prob, color = 'blue', width = 0.25, label = 'Simulated')
plt.xlabel('Event E')
plt.ylabel('Probabilities')
plt.xticks(x  + 0.25/2,[''])
plt.legend()
plt.show()