import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Doing the experiment 1e7 times
simlen=int(1e6)

sample_size = 40                #As there are 40 students in the class
n_girl = 25                     #As there are 25 girls in the class
n_boy = sample_size-n_girl      #As remaining students are boys

#calculating the theoretical probabilities
prob_girl = n_girl/sample_size  
prob_boy = n_boy/sample_size    

#Simulation using bernoulli r.v
data_bern_girl = bernoulli.rvs(size = simlen, p = prob_girl)

#Number of Favourable outcomes
err_ind_girl = np.nonzero(data_bern_girl == 1)
err_ind_boy = np.nonzero(data_bern_girl == 0)  #As if its not girl it will be boy

#Calculating the simulated probabilities
exp_prob_girl = np.size(err_ind_girl)/simlen
exp_prob_boy = np.size(err_ind_boy)/simlen
#Printing theoretical and simulated probability
print("Theoretical Probability of picking a card with girl's name = ", prob_girl)
print("Simulated Probability of picking a card with girl's name = ", exp_prob_girl)

print("Theoretical Probabilty of picking a card with boy's name = ", prob_boy)
print("Simulated Probability of picking a card with boy's name = ", exp_prob_boy)

cases=['girl','boy']
probab_theo=[prob_girl,prob_boy]
probab_sim=[exp_prob_girl,exp_prob_boy]

# plot
x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'red', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, probab_sim, color = 'yellow', width = 0.25, label = 'Simulated')
plt.xlabel('Cases')
plt.ylabel('Probabilities')
plt.xticks(x  + 0.25/2,['Girl', 'Boy'])
plt.legend()
plt.show()