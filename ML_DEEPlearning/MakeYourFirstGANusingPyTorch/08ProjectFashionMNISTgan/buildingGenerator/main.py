import torch
import matplotlib.pyplot as plt
from Dataset import FMnistDataset
from Discriminator import Discriminator
from Generator import Generator

# load data
fmnist_dataset = FMnistDataset('fashion-mnist_train.csv')

# functions to generate random data
def generate_random_image(size):
    random_data = torch.rand(size)
    return random_data


def generate_random_seed(size):
    random_data = torch.randn(size)
    return random_data

# test discriminator can separate real data from random noise
D = Discriminator()

G = Generator()
print("Generator:\n", G)

# check the generator output is of the right type and shape

G = Generator()

output = G.forward(generate_random_seed(100))

img = output.detach().numpy().reshape(28,28)

plt.imshow(img, interpolation='none', cmap='Blues')
plt.savefig('output/legend.png')
