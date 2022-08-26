## Description

For this search engine feature, we are given all the search results to display on one page. Each page shows a maximum of twenty-five search results at a time. Multiple pages in the search results can belong to the same domain. However, the team has decided that we do not want adjacent results to be from the same domain because they are likely to be similar and might favor only one site. To give our users a wide range of results, we want to rearrange the results such that two results from the same domain are not consecutive.

Suppose, we denote each domain with a character. There can only be twenty-five results on a page, so the maximum number of simultaneous domains in the search results will also be 25. Thus, denoting them with a character will be simple. Now, you are given a string that represents the initial order of the search results. Your job is to reorganize this string so adjacent characters are not identical. For example, if the input string is bbnnc, then the output should be bnbnc or any other reordering of characters such that it fulfills the conditions. If this is not possible, we will just show the original order of results.


## Solution

The optimal way to solve this question to use the greedy technique using the heap data structure. If we build the resultant order from the most common letter followed by the second most common letter and keep following this trend, we are likely to get the needed result. If this fails, it means that it was not possible to rearrange the string. The condition for failing occurs when the frequency of a character exceeds (n+1) / 2.

The complete algorithm is given below:

* First, we will find the frequency of the most frequent character in the input string.

* If the most frequent character in the string has the frequency maxFreq, for a valid rearrangement of the string, the remaining characters should be at least maxFreq - 1. We will verify this case. We can use the Map in Go. We will simply return the initial string if this test fails.

* We will be using a max heap to store the frequencies of the characters. We can use the MaxHeap data structure in Go to simulate a max heap. We will add (char, freq) tuples to a heap.

* Next, we will remove the most frequent element. If that element is not the last element in the result, we add it to the result.

* If it is the last element of the result, we pick the second most frequent element and add that to the result. We also add the most frequent element back to the heap.

* When we pop from the heap and append it to the result, we need to add it back to the heap if the frequency is not 0.

* In the end, we will return the result.





