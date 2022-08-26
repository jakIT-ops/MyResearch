Genetic algorithms are a powerful and often overlooked tool for solving difficult problems. Some of the most beautiful solutions to practical problems are inspired by or modeled after solutions found in nature. Genetic algorithms are no exception. Inspired by the original optimization algorithm, evolution, genetic algorithms can be used to solve a variety of problems in various fields. As you’ll see in this course, genetic algorithms have applications in finance, logistics, artificial intelligence, and more.


Unfortunately, despite being one of the first “artificial intelligence” algorithms, there’s a surprising lack of resources

## Why Elixir?

Elixir is certainly not a popular choice for genetic algorithm design; however, that does not mean it is not a good choice. Let’s take a look at the advantages that it brings.

### Advantages of Elixir

Firstly, as you will see in the upcoming chapters, parallelism in Elixir is a straightforward task. The BEAM is specially optimized for running numerous processes at once, so writing and running parallel code is easy. Genetic algorithms are, by nature, very parallel. A portion of [research](http://personal.denison.edu/~lalla/MCURCSM2011/6.pdf) into genetic algorithms takes advantage of the parallelism offered by Erlang to experiment with parallel genetic algorithms.

In addition, Elixir’s syntax and design patterns lend themselves nicely to writing idiomatic genetic algorithms. As you will see throughout this course, Elixir offers a number of useful features for creating a general framework for genetic algorithm design. This is not only excellent for learning, but also for rapid prototyping of new ideas.
