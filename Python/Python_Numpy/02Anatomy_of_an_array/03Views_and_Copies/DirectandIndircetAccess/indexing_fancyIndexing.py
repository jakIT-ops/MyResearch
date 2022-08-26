import numpy as np

# 1
Z = np.zeros(9)
Z_view = Z[:3] 
Z_view[...] = 1 #Z_view modifies the base array 'Z'
print(Z) # [1. 1. 1. 0. 0. 0. 0. 0. 0.]

# 2
Z = np.zeros(9)
Z_copy = Z[[0,1,2]]
Z_copy[...] = 1 #Z_copy does not modify the base array 'Z'
print(Z) # [0. 0. 0. 0. 0. 0. 0. 0. 0.]

# 3
Z = np.zeros(9) 
index = [0,1,2]
Z[index] = 1 # store 1 at index 0,1,2
print(Z) # [1. 1. 1. 0. 0. 0. 0. 0. 0.]

# 4
Z = np.random.uniform(0,1,(5,5)) #draws sample from a uniform distribution
Z1 = Z[:3,:]
#print("Z1",Z1)
Z2 = Z[[0,1,2], :]
#print("Z2",Z2)
print(np.allclose(Z1,Z2)) #returns True if two arrays are element-wise equal within a tolerance.
print(Z1.base is Z)#return true if memory of Z1 is shared with Z and false otherwise
print(Z2.base is Z)#return true if memory of Z2 is shared with Z and false otherwise
print(Z2.base is None) #return true if meory of Z2 is not shared