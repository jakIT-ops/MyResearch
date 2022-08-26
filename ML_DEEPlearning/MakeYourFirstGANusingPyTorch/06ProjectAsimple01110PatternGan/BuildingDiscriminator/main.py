import torch
import torch.nn as nn
import pandas
import random
from Discriminator import Discriminator

def generate_real():
    real_data = torch.FloatTensor(
        [random.uniform(0.0, 0.2),
         random.uniform(0.8, 1.0),
         random.uniform(0.8, 1.0),
         random.uniform(0.8, 1.0),
         random.uniform(0.0, 0.2)])
    return real_data

def generate_random(size):
    random_data = torch.rand(size)
    return random_data

# create Discriminator
D = Discriminator()
print("Training the discriminator")
for i in range(10000):
    # real data
    D.train(generate_real(), torch.FloatTensor([1.0]))
    # fake data
    D.train(generate_random(5), torch.FloatTensor([0.0]))
    pass

print( "Real data:", D.forward( generate_real() ).item() )
print( "Random noise:", D.forward( generate_random(5) ).item() )
