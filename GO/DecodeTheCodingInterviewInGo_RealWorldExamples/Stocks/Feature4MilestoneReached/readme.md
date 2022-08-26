## Description

Our company wants to display high achieving brokers in a hall of fame. They want to find out if a broker reached a milestone of making k trades and, if so, they want to know when they reached that milestone. Stockbrokers have been making trades and recording their tally of completed trades since the start of their career at the company. The data is being recorded into separate log files, each of which can be viewed as a matrix with 5 columns, one for each day of the week. There are r rows, representing the last r weeks of the year. We want to find out when a given broker reached the milestone of k trades in their career.

We’ll be provided with an m x 5 matrix and a target milestone value. Our task is to determine the day and week a stockbroker fulfilled their milestone.

## Solution

Each day stores the cumulative sum of all the trades, so we’ll have a matrix with an increasing number of values along each day. We can observed that the 2D matrix, with its unique properties, can be visualized as a sorted 1D array of size m x n. Since the array is sorted, we can simply apply the binary search algorithm on it to get the required value.

At each step of the binary search, convert the 1D index into row and column indices to look up the element in the 2D array.

Let’s see how we might implement this functionality:

* Initialize two pointers left and right at each end of the array as left = 0 and right = m x n - 1.

* Traverse the array until the value of the right pointer is greater than the value of the left pointer.

* Select the index of the middle element of the array as middleInd = (left + right) / 2.

* This selected index will give us the (row, col) pair (as explained above) to find the middle element of the matrix.

* If our milestone value is less than the middle element, skip the entire array right of the middle element as right = middleInd - 1.

* If our milestone value is greater than the middle element, skip the entire array left of the middle element as left = middleInd + 1.

* If at any point the middle element becomes equal to milestone, return the index positions. Otherwise, return -1, -1.

