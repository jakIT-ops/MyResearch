## Description

For this next Twitter feature, the company has decided to create an API that can be used by business accounts on Twitter. This API will identify three disjoint time intervals in which the most users followed or interacted with the businesses’ Tweets. You will be given the historical data of user interaction per hour for a particular business’ Twitter account. The API will have another parameter for hours. Your goal is to find three continuous intervals of a size equal to hours such that the sum of all the entries is the greatest. These time intervals should not overlap with each other.

Consider a Twitter profile with the following history of user interactions: [0, 2, 1, 3, 1, 7, 11, 5, 5] and hours = 2. The interaction array represents that this particular business’ account received no interactions during the first hour, 2 in the second hour, and so on. In this case, we want three intervals of size 2 with the maximum sum. These intervals will be [1, 3], [7, 11], and [5, 5]. Your function should return the indices of the first elements in the intervals. Therefore, the output will be: [2, 5, 7].

## Solution

To solve this problem, we can start by calculating the sum of n intervals for each index, where n = hours. We can store these sums in an array called sums. Then, all that’s left will be to find the lexicographically smallest tuple of indices [a, b, c] that maximizes sums[a] + sums[b] + sums[c].

Let’s take a look at the algorithm to find the solution:

* First, we need to calculate the sums at each index and store them in the array called sums. We can calculate sums using a sliding window.

* When the sums are calculated, we need to find the [a, b, c] indices. We know that we can assume some constraints for the lexicographically smallest trio of indices.

* If we consider b to be fixed, a should be in between 0 and b - n. Similarly, c should be between b + n and len(sums)-1. We can deduce these constraints considering we want non-overlapping intervals. We can now find these indices using dynamic programming.

* We will create two arrays, left and right. These arrays will store the maximum starting index from the left and right, respectively. The left[i] will contain the first occurrence of the largest value of W[a] on the interval a \in [0, i]
a∈[0,i]
. Similarly, the right[i] will be the same but on the interval a \in [i, \text{len}(sums) - 1]
a∈[i,len(sums)−1]
.

* Finally, for each value of b, we will check whether the corresponding left and right values are in the above-mentioned constraints or not. Out of all the trios that fulfill the constraints, we will choose the one that produces the maximum sums[a] + sums[b] + sums[c].










