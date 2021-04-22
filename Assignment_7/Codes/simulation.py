import numpy as np
import matplotlib.pyplot as plt
import math
size=100000
count1=0
count2=0
count3=0
count4=0
for j in range(size):
  n=10
  X=[]
  for i in range(n):
    a=np.random.normal(0,1)
    X.append(a)

  if(X[0]>X[1]+X[2]+X[3]+X[4]+X[5]+X[6]+X[7]+X[8]+X[9]):
    count1=count1+1
  if(X[0]>X[1]*X[2]*X[3]*X[4]*X[5]*X[6]*X[7]*X[8]*X[9]):
    count2=count2+1
  if(math.sin(X[0])>math.sin(X[1])+math.sin(X[2])+math.sin(X[3])+math.sin(X[4])+math.sin(X[5])+math.sin(X[6])+math.sin(X[7])+math.sin(X[8])+math.sin(X[9])):
    count3=count3+1
  if(math.sin(X[0])>math.sin(X[1])*math.sin(X[2])*math.sin(X[3])*math.sin(X[4])*math.sin(X[5])*math.sin(X[6])*math.sin(X[7])*math.sin(X[8])*math.sin(X[9])):
    count4=count4+1
print("Pr(X_1>X_2+X_3+...+X_10) = ",count1/size)
print("Pr(X_1>X_2X_3X_4....X_10) = ",count2/size)
print("Pr(sin(X_1)>sin(X_2)+sin(X_3)+...+sin(X_10)) = ",count3/size)
print("Pr(sin(X_1)>sin(X_2)sin(X_3)...sin(X_10)) = ",count4/size)