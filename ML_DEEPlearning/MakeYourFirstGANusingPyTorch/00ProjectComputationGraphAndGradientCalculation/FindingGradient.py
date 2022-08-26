import torch
# set up simple graph relating x, y and z
a = torch.tensor(3.0, requires_grad=True)
b = torch.tensor(2.0, requires_grad=True)

x = 3*a + 3*b
y = 6*a*a + 5*b*b*b
z = 3*x + 3*y

# work out gradients
z.backward()

# what is gradient at a = 3.0
print(a.grad)

# what is gradient at b = 2.0
print(b.grad)

'''
tensor(117.)
tensor(189.)
'''
