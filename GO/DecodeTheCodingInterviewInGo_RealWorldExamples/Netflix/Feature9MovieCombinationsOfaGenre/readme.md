### Description

Suppose we have `n` different movie genres like Action, Comedy, Family, Horror, and so on. In each genre, we have `0` to `k` movies. We need to screen several movies of different genres in a specific sequence. For example, in the morning, may want to feature a Family program, followed by a Comedy. Late at night, we may want to show Horror movies followed by Action movies. At prime time, we may want to use some other sequence. Our task is to implement an algorithm that creates a combination of movies, chosen from the given set of genres in a specific sequence.

### Solution

To solve this problem, we can use a backtracking algorithm template to generate all of the possible combinations correctly.

Let’s break down this problem into four parts.

* If the input has only one genre, return all the movies in that genre—for example, ["Action"]. This example is trivial where all of the corresponding movies will be returned, for example, `["Iron Man", "Wonder Woman", "Avengers"].`

* We already know how to solve the one-genre problem. To solve the two-genre problem, such as ["Action, Family"], we can pick the one-genre solutions for the Action genre and then append the solutions for the one-genre problem of the Family genre. For example, start with "Iron Man" and then append all the solutions for the one-genre problem of the Family genre, resulting in [[Iron Man, Frozen],[Iron Man, Kung Fu Panda],[Iron Man, Ice Age]]. Then, we can switch to the other solutions for the one-genre problem of the Action genre and repeat.

Here, we can see that solving the one-genre case is trivial, and solving the two-genre case is just solving the one-genre case twice. In the same way, we can solve the problem for n
n genres.

* To solve the three-genre problem, solve the two-genre problem to generate all combinations of the movies from the first two genres, and then solve the one-genre problem for the final genre of movies.

* To solve the four-genre problem, solve the three-genre problem for all combinations of the movies from the first three genres and then solve the two-genre and one-genre problems for the final genres of movies.


















