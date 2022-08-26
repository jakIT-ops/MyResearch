## Description

Twitter wants to adjust the number of servers deployed in a cluster, according to the user traffic, in 15-minute intervals. A metering service collects user traffic statistics over five-minute intervals. These user statistics are stored in a list, for example, [5,7,15,8,10]. We subscribe to the stream from this service. However, the five-minute interval is too short a time window to help the server deployment adapt. We want to aggregate this data to determine the average moving traffic in the last 15-minute interval.

The first two data points are an exception. When the first data point is received, it is used as the average itself. When the second data point is received, the average of the first two data points is used.

## Solution

To solve this problem, we can start by initializing an empty deque (double-ended queue) to keep track of the incoming values. For simplicity, we will call this a queue. The size of the queue will be the size of the sliding window. We will calculate the average of the items present in the queue every time we append a new count of the tweets. This queue will only keep the count of the required tweets. Once our queue is full, we will pop the first item from the left of the queue and append the new value at the end of this queue. We will use the windowSum variable to store the sum of the integers in that window. When our queue is full and a value is popped, we will subtract that value from the sum and calculate the sum using the new value.



