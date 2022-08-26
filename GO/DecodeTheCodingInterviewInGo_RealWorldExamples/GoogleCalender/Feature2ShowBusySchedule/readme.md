## Description

For the next feature, we want to find the times during which a user is busy. This feature is intended to show the busy hours of a user to other users without revealing the individual meeting slots. Therefore, if any meetings overlap or are back to back, then we want to merge their timings.

We will be provided a list of scheduled meetings, such as [[1, 4], [2, 5], [6, 8], [7, 9], [10, 13]]. In this schedule, [1, 4] and [2, 5], as well as [6, 8] and [7, 9], are overlapping. After merging these meetings, the schedule becomes [[1, 5], [6, 9], [10, 13]].

## Solution

To solve this problem, it is best to sort the meetings based on the startTime. Then, we can determine if two meetings should be merged or not by processing them simultaneously.

Here is how we’ll implement this feature:

* First, we will sort the meetings according to startTime.

* Considering two meetings at a time, we will then check if the startTime of the second meeting is less than the endTime of the first meeting.

* If the condition is true, merge the meetings into a new meeting and delete the existing ones.

* Repeat the above steps until all the meetings are processed.









