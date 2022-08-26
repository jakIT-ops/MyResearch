# 1. Looking Deeper into Genetic Algorithms

## The genetic algorithm structure

Based on what we’ve learned so far, we can understand that every genetic algorithm follows the same basic steps. While algorithms for different problems may use different techniques, probabilities, or strategies, they all share the same structure. As programmers, we want to take advantage of this.

One of the golden rules of programming is “Don’t Repeat Yourself (DRY),” which essentially boils down to not rewriting unnecessary code. We can exploit the shared structure of genetic algorithms to avoid rewriting code that remains the same from algorithm to algorithm. Unfortunately, we have to start from scratch.

So how do we go about designing a versatile framework from the ground up? Start with the basics. All genetic algorithms follow the same structure. They all use chromosomes and populations, and they all require similar inputs. We can use this to our advantage and begin designing from the ground up.

### Chromosomes and populations

Chromosomes represent solutions to problems. In the One-Max problem, our solutions consisted of a series of ones and zeroes. However, that won’t be the case for every problem. Some problems are encoded using real values, some as permutations, and some using characters. Also, some problems require us to use a data structure other than a list to encode solutions.

All of this means that specific encoding schemes are unique and vary from problem to problem. We can use the Enumerable protocol to ensure the framework is as general as possible and works for all of the encoding schemes.

In Elixir, protocols allow us to implement polymorphism within our libraries. Data structures that implement the Enumerable protocol can be passed into any function within the Enum library. That means we can encode our chromosomes using any data structure that implements Enumerable — even ones that are self-built.

### Initializing the population

The first step in every genetic algorithm is initializing a population. Typically, the first population is random — it’s like a splattering onto the search space. The idea is to start out examining many different solutions and slowly work toward the best ones.

We’ve already determined that a population is a list, which means the function we implement for this step must return a list of chromosomes. But we need to ensure that our function can apply to all types of problems and doesn’t include specifics about how chromosomes are encoded. To do this, we can take a function that generates chromosomes as input.

Elixir allows us to pass functions as arguments to other functions. We can ensure one of the parameters is a function that produces a chromosome. We don’t care about the specifics of how this function is implemented; we only care that this function returns a chromosome.

With this step, we have two main goals:

* The initialization step must produce an initial population, meaning a list of possible solutions.

* The function which initializes the population should be agnostic to how the chromosome is encoded. To do this, we can accept a function that returns a chromosome.

### Evaluating the population

The evaluation step is responsible for evaluating each chromosome based on some fitness function and sorting the population based on this fitness. This makes it easy to extract the best chromosome from the population. It also makes it easier to work with the population in the selection step.

Just like encoding schemes vary from problem to problem, so does fitness. Different problems require different measures of how good a solution is. If we were trying to find the shortest path between two points, we’d evaluate your solutions based on the distance of the path they produce. If we were trying to optimize a portfolio full of stocks, we’d evaluate the portfolio based on a potential return. Essentially, we don’t care how the fitness function is implemented or even what it returns — we just need a measure that allows us to compare the fitness of each chromosome against the rest of the chromosomes in the population.

This leaves us with the following goals or requirements of the evaluation step:

* The evaluation step must take a population as input.

* The evaluation step must produce a population sorted by fitness.

* The function which evaluates the population should take a parameter that is a function that returns the fitness of each chromosome.

* The fitness function can return anything, as long as the fitness can be sorted.
