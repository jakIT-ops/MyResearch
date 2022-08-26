## Description

The settling period is the time that must elapse before money changes hands after a stock trade is completed. We don’t want to allow another trade in the same stock before the expiry of the settling period. So, a person can’t trade more than one stock of the same company at once, and the user must wait for the settling period before another stock of the same company can be traded.

We are given a list of letters, where each letter represents the stock of a company for which a stock trade must be made. The stocks will be mapped to letters to form this input array. Letters can repeat to represent that multiple trades need to be made for the same company’s stocks. We want to make all the given trades as quickly as possible. The constraint is that two trades of the same company must be separated by at least k intervening periods; these could be trades of other companies or idle periods. The parameter k defines the settling period. We need to calculate the minimum amount of time required to trade all the stocks.

For example, if a user wants to trade four stocks of APPLE, two stocks of TESLA and one stock of MICROSOFT in the same transaction, an input array like ['A', 'A', 'A', 'T', 'T', 'M', 'A'] would be given.

## Solution

First, calculate and store the number of trades needed for each stock in a list named frequencies.

We will store the count of stocks of the company that will be traded the most in the transaction as fMax; after that, the fMax trades of the most traded company need to be separated by (fMax - 1) intervals equal to the settling period. If you have n items, there are n-1 intervals between them.

Initially, (fMax - 1) is multiplied by settling time, this gives the number of idle periods between the fMax trades of the most frequently traded item, and we assign this value to idleIntervals. Then, we keep updating the idleIntervals variable. We pick the next most frequently traded stock. If it is less frequent than the most frequently traded stock, it can be traded in the intervening periods between the trades of the latter. Otherwise, it will have to be traded one interval after the most traded stock. In the end, we need len(stocks) intervals for the actual trades and idleIntervals for the idle intervals

1. Calculate and store the frequencies of the trades for each company in an array called frequencies. Sort this array in descending order.

2. Then find the maximum value in frequencies. Store this max value as fMax to get the count of stock of the company traded the most.

3. Next, calculate the idle intervals between consecutive trades of the most frequent stock; to get that this value, we multiply settling time with fMax - 1.

4. Iterate over frequencies, and if the value at each index is less than (fMax - 1), subtract the value from idleIntervals. If the value is greater than (fMax - 1), we subtract (fMax - 1) from idleIntervals instead.

5. If idleIntervals is negative, we return len(stocks). Otherwise, we return idleIntervals + len (stocks).


