## Description

While searching on the web, we know that users make many spelling errors. One error is combining multiple words. To tackle this issue, your team has decided to create a module that adds white spaces in the query to see if valid words can be created by breaking the original query. This module will be triggered if the original query gives very few results or no results at all. You are not concerned with implementing the triggering function; you only have to implement the breakQuery functionality, which receives the current query and a list of all possible valid words.

Let’s consider a case where you are given the query "vegancookbook". This query didn’t get any web hits, so now it is sent to the breakQuery function to check if it’s possible to add white spaces to this query to create valid words. You are also given a dictionary containing all possible words. For this problem, we will assume that the only possible words are ["i", "cream", "cook", "scream", "ice", "cat", "book", "icecream", "vegan"]. Your function should use this list of strings to determine if the original query can be broken down into words provided in the dictionary. Then, the breakQuery function should return a Boolean value depending on whether it is possible to break down the query or not. In the example we just discussed, the function will return true because we can add spaces in the "vegancookbook" to produce "vegan cook book", which contains words from the dictionary.

## Solution

This problem can be solved using the dynamic programming technique. The idea behind this approach is that the given problem p
p
 can be divided into subproblems p1
p1
 and p2
p2
. If these subproblems satisfy the required conditions individually, the complete problem also satisfies the conditions. This means that the string "vegancookbook" can be split into the substrings: "vegan" and "cookbook". The substring "vegan" is a word found in the dictionary, meaning the condition is satisfied. Now, let’s consider the other substring, "cookbook", this can be divided further into "cook" and "book". These strings can also be found as words in the dictionary, meaning this part of the problem also satisfies the given condition. Hence, we can say that the input string "vegancookbook", as a whole, satisfies the condition.

The complete algorithm is given below:

* First, create a Boolean list called dp to track all the substrings in the query that satisfy the given condition.

* Use two nested loops with i and j as indices. The index i will refer to the length of the substring p'
p 
′
 
, and j will be the index that splits the current substring p'
p 
′
 
 into smaller substrings, p'(0, j)
p 
′
 (0,j)
 and p'(j+1, i)
p 
′
 (j+1,i)
.

* Initially, the first element of the dp array will be set to true because an empty string is always present in the dictionary, and the rest of the elements of the dp are set to false.

* In the nested loop, the substrings of all possible lengths are considered starting from the beginning by using the index i. Each substring is then split into p1
p1
 and p2
p2
 in every possible way using the index j.

* Next, the entry at dp[i] is checked to see if it contains True, which means that the substring p1'
p1 
′
 
 satisfies the given condition. If this condition is satisfied, we further check if p2'
p2 
′
 
 is also present in the dictionary.

* If both strings are present, we set dp[i + l] to True. Otherwise, it remains False. Here l represents the length of the substring, i.e., p2'
p2 
′
 
.
