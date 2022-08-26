## Description

An enterprise partner has asked us to create a feature for them. They want us to find two sets of consecutive days to schedule board meetings. They are selecting members for two teams from a candidate pool. Selecting each team takes k hours. We want to schedule two sets of meetings, one for each team, of duration k hours each. To ensure fairness, we want the selection committee meetings for a specific team to be done on consecutive days. This means that, once the interviews for a specific team start, there should be meetings every day until the interviews are over. The interviews for the second team cannot start on the last day of selections for the first team; they do not necessarily need to start the very next day, either. To best utilize everyone’s time, we want to fully utilize the mutually free hours on each day meetings are scheduled. We have already found the number of mutually free hours over a set of consecutive days for the members of the selection committee. Furthermore, we want each selection meeting to last as few days as possible. Your task is to find two sets of consecutive days for these selection board meetings that fulfill the above criteria and return the total number of days needed for the meetings.

For example, consider that the number of mutually free hours over a set of consecutive days are [1, 2, 2, 3, 2, 6, 7, 2, 1, 4, 8], and k is 5. In this case, the possible set of days with k free hours are [1, 2, 2], [3, 2], and [1, 4]. The requirements said that we want to select the sets that span the fewest days, so those are: [3, 2] and [1, 4]. Your function should return the total days that will be needed for both sets of meetings. Therefore, the output will be 4 for this example.

## Solution

To implement this solution, we can calculate the prefix sum for each index in the input array and use a hash table to store it. Then, we traverse the array and use the hash table to find the shortest subarrays with a sum equal to k.

The complete algorithm is given below:

* First, we will traverse through the input array once and store the key-value pairs in a hash table such that, for every ith index, the key is the sum of a[0] to a[i] and the value is i.

* We will also add (0, -1) to the hash table as the default.

* Now, we will traverse through the array again, and for every i, we will find the minimum value of the length of the subarray on the left or starting with i, whose value is equal to k.

* Then, we will find another subarray starting with i + 1, whose sum is k.

* We will update the result with the minimum value of the sum of both the subarrays. This is possible because all the values are positive, and the value of the sum is strictly increasing.
