import numpy as np

Z = np.zeros((5,5))
print("Z:\n",Z)
print("Z.ravel().base:\n",Z.ravel().base)
print("Z.ravel().base is Z:",Z.ravel().base is Z) #returns true if memory of Z.ravel() is shared with Z

print("\nZ[::2,::2].ravel():\n",Z[::2,::2].ravel())
print("\nZ[::2,::2].ravel().base is Z:",Z[::2,::2].ravel().base is Z)#returns true if memory of Z[::2,::2].ravel() is shared with Z

print("\nZ.flatten()\n:",Z.flatten())
print("Z.flatten.base is Z:",Z.flatten().base is Z)#returns true if memory of Z.flatten() is shared with Z