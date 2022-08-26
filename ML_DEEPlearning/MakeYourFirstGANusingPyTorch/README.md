## Rise of ML and AI

Machine learning (ML) and artificial intelligence (AI) has exploded in the last few years with amazing achievements being reported in the news every few months.

Not only does your smartphone understand you when you talk to it, but it is also pretty good at translating between many human languages. Self-driving cars are now able to drive as safely as humans, and machines can now diagnose some diseases more accurately and sooner than experienced doctors.

### GANs are new

Compared to the decades of research and refinement behind traditional neural networks, GANs only came to prominence in 2014 with Ian Goodfellow’s now seminal paper [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661).

This means GANs are very new, and the creative possibilities are only starting to be explored.

It also means we don’t yet fully understand how to train them as effectively as we can with traditional networks. When they work, they work spectacularly well, but too often they fail. Research into how GANs work, and why they can fail, is currently very active.

# PyTorch Basics

Building larger networks could be a laborious task. One of the most laborious parts is doing calculus to work out the relationship between the back-propagated error and weights in our network. If we decide to change our network we would potentially have to do all this work again.

Here we’ll be using PyTorch because it takes away a lot of that leg work, and lets us focus on thinking about the design of our networks.

One of the most powerful and convenient features of PyTorch is that it does all the calculus for us, whatever the shape or size of the network we dream up. If we change our minds about the design of the network, PyTorch automatically works out the new calculus without us having to pull out a pencil and paper to work out the gradients again.

* PyTorch is a leading machine learning framework for Python. Similar to NumPy, it allows us to work with arrays of numbers. It also provides a rich library of convenient tools and functions to make machine learning easier.

* In PyTorch, the basic unit of data is called a tensor. These can be multi-dimensional arrays, simple 2-dimensional grids, 1-dimensional lists, or even a single value.

* The key feature of PyTorch is the ability to automatically work out gradients for functions we’ve defined. Calculating gradients is essential for training neural networks. To do this, PyTorch builds a computation graph of tensors and how they’re related to other tensors. It does this transparently when we define how one tensor is calculated from another in our code.
