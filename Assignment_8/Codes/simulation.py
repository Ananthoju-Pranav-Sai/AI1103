import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad
def integrand(x):
    return np.exp(-x*x/2) /math.sqrt(2*math.pi)
mean, cov, n_samples = np.array([0.,0.]), np.array([[2.0,-1.0],[-1.0,2.0]]), 1000000
data=np.random.multivariate_normal(mean,cov,size=n_samples)
X1=data.T[0]
X2=data.T[1]
count=0
for i in range(1000000):
    if(X1[i]-X2[i]>6):
        count+=1
p=count/n_samples
I = quad(integrand, -np.inf, -math.sqrt(6))
print("Theoretically calculated pr(X1-X2>6) = Phi(-sqrt{6}) = ",I[0])
print("Simulated pr(X1-X2>6) = ",p)