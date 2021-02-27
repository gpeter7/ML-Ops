# import required packages
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pickle

my_file = open("/home/ubuntu/project/data.txt", "r")
arr_y = np.array([])
arr_x = np.array([])

for line in my_file:
    fields = line.split(",")
    x = float(fields[0])
    y = float(fields[1])
    arr_y = np.append(arr_y, y)
    arr_x = np.append(arr_x, x)
    
#print(arr_x)
#print(arr_y)

# initializing for backprop and gradiant descent using MSE Error model for loss
# 1. calculate loss
def calculateLoss(pred, actual):
  #return an error if the arrays differ in size
  if(len(pred) != len(actual)): 
    return "error"
  #MSE Calc = mean of the sqared differences betwen each element 
  mse_calculated = np.mean( np.square( np.subtract( pred,actual ) ) )  
  return(mse_calculated)  

# 2. calcualte gradiant of m1
def calculateGradm1(pred, actual, xVal):
  #return an error if the arrays differ in size
  if(len(pred) != len(actual)): 
    return "error"
  arr_diff = np.subtract(pred,actual)
  grad_m_1 = (2/len(pred)) * np.sum(np.dot(arr_diff, xVal))
  return(grad_m_1)

# 3. calcualte gradiant of m2
def calculateGradm2(pred, actual, xVal):
  #return an error if the arrays differ in size
  if(len(pred) != len(actual)): 
    return "error"
  arr_diff = np.subtract(pred,actual)
  grad_m_2 = (2/len(pred)) * np.sum( np.dot( arr_diff, np.square(xVal) ) )
  return(grad_m_2)

# 4. calculate gradiant of bias
def calculateGradBias(pred, actual, xVal):
  #return an error if the arrays differ in size
  if(len(pred) != len(actual)): 
    return "error"
  arr_diff = np.subtract(pred,actual)
  grad_bias = (2/len(pred)) * np.sum(arr_diff)
  return(grad_bias)

#initialize variable
m_1 = 0.1
m_2 = 0.1
bias = 0.1
lr_rate = 0.09
desc_iter = 7000
arr_loss_1 = [0] * desc_iter
arr_loss_2 = [0] * desc_iter

for i in range(desc_iter):
  predicted_y = m_1 * arr_x + m_2 * np.square(arr_x) + bias
  #loss calculate - calculateLoss(pred, actual)
  arr_loss_1[i] = calculateLoss(predicted_y, arr_y)
  #if i % 10 == 0:
    #print("iteration: "+str(i) +" loss: "+str(arr_loss_1[i]))
  #gradiant for m1 - calculateGradm1(pred, actual, xVal)
  grd_m_1 = calculateGradm1(predicted_y, arr_y, arr_x)
  #gradiant for m2 - calculateGradm2(pred, actual, xVal)
  grd_m_2 = calculateGradm2(predicted_y, arr_y, arr_x)
  #gradiant for bias - calculateGradBias(pred, actual, xVal)
  grad_bias = calculateGradBias(predicted_y, arr_y, arr_x)
  #now descent in the direction of gradient 
  m_1 = m_1 - lr_rate * grd_m_1
  m_2 = m_2 - lr_rate * grd_m_2
  bias = bias - lr_rate * grad_bias

write_to_file = [("m_1", m_1), ("m_2", m_2), ("c", bias)]
with open('/home/ubuntu/project/model.pkl', 'wb') as handle:
    pickle.dump(dict(write_to_file), handle, protocol=pickle.HIGHEST_PROTOCOL)

#printing results
print("Predicted M1 = " + str(m_1))
print("Predicted M2 = " + str(m_2))
print("Bias = " + str(bias))
