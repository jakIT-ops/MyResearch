## Description

We want to offer marathons for our viewers. Each marathon will have a fixed set of movies catering to a specific taste. For a given marathon, different viewing orders of the movies will yield different user satisfaction results. We want to experiment (A/B testing) with different viewing orders of the same marathon.

## Solution

Solution#
To solve this problem, we will use the backtracking approach.

We will assume a Backtrack function that takes the index of the first movie to consider as an argument Backtrack(first).

* If the first movie to consider has index n, then that means that the current permutation is done.

* We will iterate over the marathon from index First to index n - 1.

* We will place the ith movie first in the permutation, that is, Movies[First], Movies[i] = Movies[i], Movies[First].

* We will proceed to create all the permutations that start from the ith movie: Backtrack(First + 1).

* Now we will backtrack, that is, Movies[First], Movies[i] = Movies[i], Movies[First] back.





