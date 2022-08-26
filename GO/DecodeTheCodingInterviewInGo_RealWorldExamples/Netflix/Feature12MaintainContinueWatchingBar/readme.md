## Desciption

We are working on a new algorithm to suggest programs to watch first on a “Continue Watching” bar. When the user navigates to the browse page, we want to suggest programs on a “Continue Watching” bar based on the past viewing history. Each time the user navigates, we want to show newer seasons or episodes of shows that have been most-watched by the user.

The user can either clean up their watch history or binge-watch the shows. In this case, the algorithm should suggest the next most frequent show watched or does not suggest any show.

Your task is to design an algorithm that will keep track of the most-watched show. Each time the user navigates to the browse page, the algorithm will suggest the most frequently watched show and in case of a tie among two or more shows, we want to suggest the show watched most recently.

The algorithm will save the show’s name each time the user watches the show’s episode. The names that are saved the most, i.e., the most-watched show’s names, will be shown to the “Continue Watching” bar first.

Suppose, User watched multiple episodes of the following shows:
```
["Queen's Gambit", "Teen Wolf", "Bridgerton"]
```

## Solution

As we care about the frequency of the show, let’s save the number of occurrences for each show in a map named Frequency.

To pop the element with the maximum frequency we must keep track of the current maximum frequency element in the stack. We can use a variable named MaxFrequency to perform this task.

Let’s save the elements for each frequency in a map named Group, in which we can save multiple elements for each frequency. The map, for each frequency, will store an array that will work as a stack to push or pop an element.

In the case, where multiple elements have the same frequencies, we can use Group to pop the most recent element — the top of the stack.

