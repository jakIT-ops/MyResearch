import torch
import torch.nn as nn
import pandas
import random
from Discriminator import Discriminator
from Generator import Generator

# create Generator
G = Generator()

# model summary
print(G)

# check the generator output is of the right type and shape
print("The untrained generator output:", G.forward(torch.FloatTensor([0.5])))
