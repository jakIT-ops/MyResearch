## Description 

Thousands of clients are expected to be associated with a Netflix server at any given time. User session statistics such as packet drops and buffering events in the last one-minute interval are relayed back to the Netflix servers to monitor the session quality and adjust the streaming rate. Due to a large number of users, this amounts to an immense volume of data. Limited memory per user session is available due to the problem scale.

At any time, we may store the last k values for a particular measure (such as the number of buffering events) of a specific user session. As the next value arrives, the oldest value is removed from the memory. In other words, all the values for a session are not available but are accessible in a sliding window fashion.

We want to maintain some statistics of the user session. The nature of the network is such that there may be short-lived extreme cases where there are lots of buffering events. Therefore, the average value of the number of buffering events is of limited use. The median number of buffering events, on the other hand, is significant.

Given that the data values are revealed in a sliding window fashion, calculate the median number of buffering events in a one-minute interval.


## Solution

To solve this problem, we will use the same idea as used in Find Median Age. The only additional requirement is removing the outgoing elements from the window.

Assume that we are using two heaps as mentioned in the Find Median Age problem, but only the tops of heaps are accessible. Deleting elements that are not on the top of the heap is an O(\log n)
O(logn)
 operation. We need to find an efficient way to remove elements that are moving out of the window.

If the two heaps are balanced, only the top is needed to find the medians. Keeping the heaps balanced will allow us to keep invalidated elements in the heap without interfering with the results.

To do this, we can use the lazy removal technique, i.e., utilizing a hash-map to keep track of invalidated elements, and once they reach heap tops, remove them from the heaps.

The most challenging part here is to keep the heap balanced while keeping the invalidated elements. We can move the invalidated elements from one heap to the heap that contains invalidated elements.



