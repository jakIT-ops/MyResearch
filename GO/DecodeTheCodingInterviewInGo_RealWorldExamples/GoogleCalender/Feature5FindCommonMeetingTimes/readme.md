## Description

Now, we want to implement a feature that lets us see when two users are busy at the same time. We will be given the meeting schedule of two users, and we have to find all the overlapping meetings to determine when both of them are unavailable.

> We will also assume that each user’s schedule is free of conflicting meetings, meaning their schedules are non-overlapping. Moreover, the meetings have been already sorted based on their starting time.

Let’s say that we are given the following pairs of meeting schedules: [[1, 3], [5, 6], [7, 9]] and [[2, 3], [5, 7]]. In this example, we can see that both of the users will be busy at the following times: [[2, 3], [5, 6]].

## Solution

Here is how we will implement this feature:

* We will use two indices, i and j, to traverse both of the meeting schedules, meetingsA and meetingsB, respectively.

* The indices i and j will both be zero at the beginning.

* Next, we will check if meetingsA[i] and meetingsB[j] overlap by comparing the start and end times.

* If the times overlap, the overlapping time interval will be added to the resultant list.

* Otherwise, we will keep incrementing the indices depending upon the end time of the next meeting. This means that if the next meeting in meetingsA ends before the next meeting in meetingsB we will only increment i. This is because the current meeting in meetingsB has the possibility to overlap with the next meeting. Similarly, vice versa is also true in case of incrementation in j.




