import torch

#*****************************************************************
x1 = torch.empty(3,3) #Creation of a matrix size 3x3 

x2 = torch.zeros(2,2) #Creation of a matrix size 2x2 and it contains only 0
x3 = torch.ones(2,2) #Creation of a matrix size 2x2 and it contains only 1

x4 = torch.empty(3,3,dtype=torch.float16) #Change the type of the matrix unity.

x5 = torch.tensor([2.5,0.1]) #Utilisation of transor


print(x4) #Output of the matrix and the values inside
print(x4.size()) #Output of the size [x,y] of the matrix
#*****************************************************************



#*****************************************************************
#This make an addition of two matrixs
a1 = torch.rand(2,2)
a2 = torch.rand(2,2)
a = a1 + a2
#Possibility to do : a = torch.add(a1,a2) or a1.add_(a2)
print(a1)
print(a2)
print(a)

#This make a substraction :
a = a1 - a2
a = torch.sub(a1,a2) #Equal to the precedent operation
print(a)

#This make a multiplication :
a = a1 * a2
a = torch.mul(a1,a2) #Equal to the precedent operation
a.mul_(a2)
print(a)

#This make division :
a = a1 / a2
a = torch.div(a1,a2) #Equal to the precedent operation
print(a)
#*****************************************************************


#*****************************************************************
#To obtains just a column or a line
x = torch.rand(5,3)
print(x)
print(x[:,0]) #This show all the elements of the first column ( 0 is the first index )
print(x[1,:]) #This show all the elements of the seconde line
print(x[1,1]) #This show the element on the second line and on the second column ( 1 element )
print(x[1,1].item()) #This show precisly the value of this element. item() can be use on just one element
#*****************************************************************

 
#*****************************************************************
x = torch.rand(4,4)
print(x)

y = x.view(16) #This transfer all the elements in one vector. 16 = 4*4 
print(y)

z = x.view(-1,8) #-1 is the value to automaticly transform the matrix on a dimension (a,8), a is an int
print(z)
print(z.size) #This confirm the new dimension of the matrix z (2,8), a = 2
