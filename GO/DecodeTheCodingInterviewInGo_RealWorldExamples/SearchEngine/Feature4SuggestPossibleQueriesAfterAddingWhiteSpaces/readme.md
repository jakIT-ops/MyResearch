## Description

This feature is an extension of the one we programmed in the previous lesson. Like the last feature, we are given a user query that doesn’t provide a significant number of web hits. Therefore, we have decided to break down the query by adding white spaces to see if valid words can be created by breaking the original query. However, this time the difference is that you are tasked with finding a list of all the possible valid queries created by adding white spaces in the original query.

Let’s suppose the user searches "vegancookbook". This query didn’t get any web hits, so it is sent to the breakQuery function to check if it’s possible to add white spaces to create valid words. You are also given a dictionary containing all the possible words. In this problem, we will assume that the only possible words are ["an", "book", "car", "cat", "cook", "cookbook", "crash", "cream", "high", "highway", "i", "ice", "icecream", "low", "scream", "veg", "vegan", "way"]. Your function should use this list of strings to determine if the original query can be broken down into words provided in the dictionary. Then, the breakQuery function should return a list of strings that can be created by breaking down the query into the words present in the dictionary. In the example we just discussed, the function will return ['vegan cook book', 'vegan cookbook', 'veg an cook book', 'veg an cookbook']. Similarly, for the query string "highwaycarcrash" and the same word dictionary, the function should return ["high way car crash", "highway car crash"]


## Solution

This problem can also be solved using a dynamic programming (DP) technique. We will be using top-down dynamic programming, which is more efficient, even though other variations of DP can also be used. Let’s take a look at the intuition behind this solution.

Consider the query string, denoted by q
q
, "vegancookbook". We will define the result breaking this query into valid words as F(q)
F(q)
. Now, if a word, denoted by w
w
, is present in the list of words dict and matches the prefix of the query, we can divide the query string into two parts: the word and the remaining postfix of the query.

Here is the complete algorithm for the implementation:

* The breakQuery() function takes in the query string and the list of words called dict. This function then calls a recursive helper function.

* The recursive function takes in the query string. The dict is converted into a set before sending to the function (lookup in sets is linear), and an empty python dictionary (not to be confused by dict) is also sent. Later, we will use this dictionary to store results for each substring.

* The helper function’s base case is when the query is empty; this returns an empty list. Note that it is actually an empty list of lists because that is the return type of this function.

* In the recursive function, we run an iteration over all the prefixes of the query. If the corresponding prefix happens to match a word in the set, we recursively invoke the function on the postfix.

* At the end of the iteration, we store the results in the dictionary called result with each valid postfix string as the key and the list of words that compose the prefix as the value. For instance, for the postfix cookbook, the corresponding dictionary entry would be [“cook”, “book”].

* At last, we return the value from result that corresponds to the query string as the key.


