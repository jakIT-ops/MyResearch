import torch
# set up simple graph relating x, y and z
a = torch.tensor(3.0, requires_grad=True)
b = torch.tensor(2.0, requires_grad=True)

x = 3*a + 3*b
y = 6*a*a + 5*b*b*b
z = 3*x + 3*y

print("a:", a)
print("b:", b)

print("x:", x)
print("y:", y)
print("z:", z)

'''
a: tensor(3., requires_grad=True)
b: tensor(2., requires_grad=True)
x: tensor(15., grad_fn=<AddBackward0>)
y: tensor(94., grad_fn=<AddBackward0>)
z: tensor(327., grad_fn=<AddBackward0>)
'''
