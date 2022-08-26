## Description

We are given the price predictions, prices, of a stock over a future time window. We are interested in making a profit by selling the stock at a higher price.

There are n intervals in the time window, where each i^{th}
i 
th
 
 interval represents a stock’s predicted price for that interval. Our goal is to return an array, intervals, such that intervals[i] is the minimum number of intervals after the ith interval when the price will increase. If there is no time interval for which this is possible, we will keep intervals[i] == 0 instead.


## Solution

We are given an array that represents the time series of the predicted stock prices over n future intervals, all of equal duration. The i^{th}
i 
th
 
 element of this array represents the predicted stock price in the i^{th}
i 
th
 
 interval. Our task is to create another array that will represent the minimum number of time intervals that will pass before there is an increase in price after the i^{th}
i 
th
 
 interval.

We can solve this problem using a monotonic stack. We will use a monotonic decreasing stack, where the stack will be sorted in descending order to hold the indices of the prices. We have to find the minimum number of intervals. Therefore, we will store the indices of the prices, rather than the prices themselves.

For any given time interval, we will have two choices. If the current interval’s price is not greater than the price on the top of the stack, we will push the current interval’s index to the top of the stack. Since the price is not greater in this case, the stack will remain in a sorted order.

If the current interval’s price is higher than the price at the top of the stack, then the current interval is the first interval with a price that is higher than the interval with the price at the top of the stack. Once we find a higher price, the minimum number of intervals will be the difference between the current index and the index located at the top of the stack. We can declare an intervals array, before iterating through the predicted prices, and populate it as we go along.


