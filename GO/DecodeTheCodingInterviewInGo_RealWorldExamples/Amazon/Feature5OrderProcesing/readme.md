## Description

Let’s assume the Amazon team wants to collect stats of the number of orders processed. These stats will be presented in a quarterly report using a histogram. To collect data for this presentation, the devs have stored the number of orders for each day rounded down to the nearest significant milestone. For example, when we meet or exceed one million orders, we display “1M+ orders processed.” We continue to display the same message until another milestone is reached. For instance, when nine million orders or more are processed, we display “9M+ orders processed.” Every day, the rounded cumulative number of orders processed is appended to an array.


## Solution

To implement this feature, we can use a modified binary search approach. Let’s take a look at the step by step algorithm:

* First, we will implement a search() function that returns the first index at which we can insert a number, n, into milestones to keep it sorted.

* In the search() function, we will use two pointers, first and last, that point to either side of the array. Then, we calculate the mid of the array.

* If the milestone at mid is equal to or greater than target, the first day of the milestone will be in the left half (including the middle) of the list, and the right half of the list can be ignored. Otherwise, the left half of the list can be ignored, and we will focus on the right half.

* Now that we have the search(), we will use it to find the first occurrence of the target milestone. However, target might not be present in the milestone. This could happen if we jump two or more milestones in a day. Therefore, we will first check if the target is present in milestones. If it isn’t present, we will return [-1, -1].

* When the target is in the array, we need to find the last day of the milestone. To do this, we can search for target+1 in the milestones array using the search() function. After finding the first occurrence of target+1, we can subtract 1 to find the last day of the milestone.









