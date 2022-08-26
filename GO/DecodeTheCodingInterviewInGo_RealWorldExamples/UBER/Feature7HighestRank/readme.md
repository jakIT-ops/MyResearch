## Description

At Uber, each driver is assigned a rank based on the reviews they receive from their passengers. Currently, the system prioritizes drivers with the highest rank and assigns them instant rides. We want to change this driver selection criterion such that drivers with lower ranks don’t get starved while the drivers with high ranks keep getting rides. The drivers’ ranks are maintained in an unsorted list. We’ll call a hidden API that will provide us with a number k. The value of this k can range from 1 to the size of our rank list. Once we have a value k, we need to find the kth highest driver rank.

We’ll be provided with an unsorted list of integers representing the divers’ ranks. The drivers are represented by the index of this list. The value of k will be made available from the hidden API. Our task will be to determine the kth highest rank, so the driver associated with that rank can be selected.

## Solution

Just like in Feature #1, we can use a heap to obtain the kth highest rank from our unsorted list. We now have to select the largest number, so we’ll use a min-heap. We’ll insert ranks of the first k drivers into the min-heap.

As we know, the root is the smallest element in a min-heap. So, since we want to keep track of the kth highest element, we can compare every number with the root while iterating through all the numbers in the list. If any number is greater than the root element, we’ll take the root out and insert the greater number. This will ensure that we always have the k highest ranks in the Heap. In the end, we can simply return the root element as the kth highest rank.

