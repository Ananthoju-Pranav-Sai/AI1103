import numpy as np
from scipy.stats import bernoulli
import random

sample_size=100000

#choosing some random values for probability of A and probability of B
prob_A=random.random()
prob_B=random.random()

#Simulations using Bernoulli r.v.
while(1):
    sample_A= bernoulli.rvs(size= sample_size, p = prob_A)
    sample_B= bernoulli.rvs(size= sample_size, p = prob_B)


    #calculating P(AB):
    count=0
    for i in range(sample_size):
        if sample_A[i] == 1 and sample_B[i] == 1:
            count +=1
        
    #finding probability of A intersection B
    prob_AB= count/sample_size
    #finding probability of A/B  
    prob_A_B=prob_AB/prob_B  

    #considering the case  when P(A/B)>P(A)
    if prob_A_B > prob_A:
        break
print("If P(A/B) > P(A) then")
#Calculating P(B/A)
prob_B_A=prob_AB/prob_A
if prob_AB > prob_A*prob_B:
    print("P(AB) > P(A)P(B)")
else:
    print("P(AB) < P(A)P(B)")
if prob_B_A > prob_B:
    print("P(B/A) > P(B)")
else:
    print("P(B/A) < P(B)")