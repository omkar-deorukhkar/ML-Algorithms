import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd


def summation(x):
    sumx = 0
    for i in x:
        sumx += i
    return sumx
x =[]
y =[]
        
for i in range(0,100):
    x.append(i)
    y.append(i+random.randint(0,50))
x = np.array(x)
y = np.array(y)

b = np.array([0.2,0.3])
alpha = 0.0001


for i in range(0,10000):
    pred = b[0]*x + b[1]
    rmse = np.sqrt(summation((y-pred)*(y-pred))*1/100)

    delta_b0 = (-2/100)*summation(x * (y - pred))
    delta_b1 = (-2/100)*summation((y - pred))

    b[0] -= alpha*delta_b0
    b[1] -= alpha*delta_b1

pred = b[0]*x + b[1]


plt.plot(x,pred,color='blue',label='Regression Line')
plt.scatter(x,y,color='red',label='Scatter Plot')
plt.xlabel('x')
plt.ylabel('y_pred')
plt.show()

print(b[0],b[1])



