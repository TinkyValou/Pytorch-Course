import torch
import numpy as np

a  = torch.ones(5)
print(a) #[1,1,1,1,1]
b = a.numpy() #Or b = torch.from_numpy(a)
print(b) #[1,1,1,1,1] = a
print(type(b)) #class 'numpy.ndarray'

a.add_(1) # a +=1
print(a) #[2,2,2,2,2]
print(b) #[2,2,2,2,2] (it's the same memory to a and b)

