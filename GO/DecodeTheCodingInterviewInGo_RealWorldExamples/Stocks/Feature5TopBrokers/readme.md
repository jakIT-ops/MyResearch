## Description

The company is doing performance evaluations. Each broker’s increments will be decided based on their level of activity throughout the last quarter. Each broker is assigned a unique ID that can be used to track their progress. Currently, this information is managed using a list. Every time a broker completes a trade, their ID is inserted into this list. Now, the company wants to promote its top k brokers. We have to implement a functionality that will automatically output the top k performers at the end of a quarte


## Solution

We need to find the top k IDs based on each number’s frequency count. In this problem, we first need to know the frequency of each number; we can do this using a, HashMap. Once we have the frequency map, the best data structure to keep track of the top k frequencies is heap. We’ll iterate through the frequency map and insert each element into our heap. If for an element, i, the size of our heap is k + 1, we do two things:

1. Take out the lowest frequency element from the heap.

2. Insert the element, i, into the heap.

This will ensure that we always have k maximum frequencies in the heap. The most efficient way to repeatedly find the smallest number among a set of numbers is using a min-heap.


