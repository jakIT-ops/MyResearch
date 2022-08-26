import numpy as np

# 1
Z = np.arange(9).reshape(3,3).astype(np.int16)
print(Z)
print(Z.itemsize)# returns size of Z in bytes
print(Z.shape)# returns the x dimension and y dimension of Z
print(Z.ndim)# dimension in Z i.e (2 in this case) since the array is 2D
print()

# 2 
Z = np.arange(9).reshape(3,3).astype(np.int16)
stride = Z.shape[1]*Z.itemsize, Z.itemsize # store stride of Z
print("Stride(as np.int16):",stride)
print("Z.stride(np.16):",Z.strides)
Z = np.arange(9).reshape(3,3).astype(np.int32)
stride= Z.shape[1]*Z.itemsize, Z.itemsize  #stores stride of Z
print("Stride(as np.int32):",stride)
print("Z.stride(np.32):",Z.strides)
print()

# 3
Z = np.arange(9).reshape(3,3).astype(np.int16)
offset_start = 0
for i in range(Z.ndim):
  offset_start += Z.strides[i] * i #compute the start offset of Z
  offset_end = offset_start + Z.itemsize #compute the end offset of Z

print("Starting offset:", offset_start)
print("Ending offset:", offset_end)
print()

# 4
Z = np.arange(9).reshape(3, 3).astype(np.int16)
index = 1, 1
print(Z[index].tobytes())
   #b'\x04\x00'
offset_start = 0
for i in range(Z.ndim):
  offset_start += Z.strides[i] * index[i]
  offset_end = offset_start + Z.itemsize
  
print(Z.tobytes()[offset_start:offset_end])#b'\x04\x00'