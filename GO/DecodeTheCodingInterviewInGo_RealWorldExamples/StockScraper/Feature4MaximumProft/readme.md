## Description

We have now extracted the stock increase and decrease percentages over a number of consecutive days. This will be represented as a list of numbers, one for each consecutive day, holding the increase or decrease in stock price on the given day. We can use this data to find the maximum profit that could have been made for the given time period. Sometimes, the maximum profit might be negative, indicating a period of minimum loss. For simplicity and to avoid fractional values, we are rounding the increase and decrease percentages to their nearest value.

We’ll be provided with a list of positive and negative integers. The indexes will indicate the day number and the integer value will indicate the stock increase or decrease percentage on that day. We have to return the maximum value that can be obtained by adding the sublist elements.


## Solution

The basic idea is to scan the entire list and at each position find the maximum sum of the sublist ending there. This is achieved by keeping a currentMax for the current list index and a globalMax.

Let’s see how we might implement this functionality:

1. Initialize a currentMax and a globalMax and assign them the first value of the array.

2. Traverse the array starting with the second element.

3. For each element, check whether currentMax is less than zero:

	* If it is less than zero, assign it the current element as its value

	* Otherwise, add the current element in the currentMax

4. Similarly, for each element check if globalMax is less than currentMax then assign globalMax equal to the value of currentMax



