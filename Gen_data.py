import numpy as np
import random as rd

def f(x):
  m_1 = .1
  m_2 = 3
  c = 17
  return(m_1*x + m_2*(x**2) + c)

#Intialize arrays
samplesize = 100
arr_x = np.linspace(0,1,num=samplesize)
arr_y = [0] * samplesize

for i in range(0,samplesize):
  arr_y[i] = f(arr_x[i])

np.savetxt('data.txt', np.vstack((arr_x,arr_y)).T, delimiter=',')