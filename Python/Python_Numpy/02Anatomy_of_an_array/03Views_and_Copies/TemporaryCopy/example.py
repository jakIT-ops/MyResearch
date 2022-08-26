import numpy as np

X = np.ones(10, dtype=np.int)#create an array X of size 10 containing ones
Y = np.ones(10, dtype=np.int)#create an array Y of size 10 containing ones
A = 2*X + 2*Y #store 2*X + 2*Y in A
print("X:",X)
print("Y:",Y)
print("A=2*X + 2*Y :\nA:",A)

'''
output:
X: [1 1 1 1 1 1 1 1 1 1]
Y: [1 1 1 1 1 1 1 1 1 1]
A=2*X + 2*Y :
A: [4 4 4 4 4 4 4 4 4 4]
'''

X = np.ones(10, dtype=np.int) #create an array X of size 10 containing ones
Y = np.ones(10, dtype=np.int) #create an array Y of size 10 containing ones
print("X:",X,"Y:",Y,"\n np.multiply(X, 2, out=X)")
np.multiply(X, 2, out=X) # multiply X with 2 and store the result in X
print("X:",X,"Y:",Y,"\n np.multiply(Y, 2, out=Y)")
np.multiply(Y, 2, out=Y)# multiply Y with 2 and store the result in Y
print("X:",X,"Y:",Y,"\n np.add(X, Y, out=X)")
np.add(X, Y, out=X)# add X and Y and store the result in X
print("X:",X,"Y:",Y)

'''
X: [1 1 1 1 1 1 1 1 1 1] Y: [1 1 1 1 1 1 1 1 1 1] 
 np.multiply(X, 2, out=X)
X: [2 2 2 2 2 2 2 2 2 2] Y: [1 1 1 1 1 1 1 1 1 1] 
 np.multiply(Y, 2, out=Y)
X: [2 2 2 2 2 2 2 2 2 2] Y: [2 2 2 2 2 2 2 2 2 2] 
 np.add(X, Y, out=X)
X: [4 4 4 4 4 4 4 4 4 4] Y: [2 2 2 2 2 2 2 2 2 2]
'''