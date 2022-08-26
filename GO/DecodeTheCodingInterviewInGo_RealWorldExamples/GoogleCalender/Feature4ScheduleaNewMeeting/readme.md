## Description

For this feature, we have a user who wants to add a new meeting to their tentative meeting schedule. First, we need to add the new meeting to the user’s schedule. Then, we want to make refinements in the schedule to merge some of the meetings. The user’s initial schedule will have no conflicts; however, the new meeting might overlap with one or more of the older ones. Therefore, we can save time by merging some of the meetings that can be held together in the same venue (this can be done for the tasks that can run simultaneously). The meetings can only be merged if the new meeting time overlaps or is adjacent to an existing meeting. We merge these meetings to eliminate conflict.

Suppose you are given a list of non-overlapping scheduled meetings, such as [[1, 3], [4, 6], [8, 10], [10, 12], [13, 15], [16, 18]]. The new meeting, which we need to fit into this already busy schedule, is also given; it is [9, 13]. In this case, the new meeting overlaps with two meetings: [8, 10] and [10, 12]. After merging, the meeting is adjacent to the [13, 15] meeting, so `[13, 15]` will also be merged. Hence, the final schedule for the day will be: `[[1, 3], [4, 6], [8, 15], [16, 18]]`.

## Solution

To implement this feature, we need to first sort the meetings based on startTime. Then, we will process the meetings that come before the new meeting, insert the new meeting, and merge the new meeting with the older ones if needed.

Here is how we will implement this feature:

* First, we need to sort the meetings according to the startTime.

* After the meetings are sorted, we will create a new list called output and add the meetings that start before the newMeeting to it.

* Then, we will add the newMeeting to the output and merge it with the previously added meeting (if the new meeting starts before the previously added meeting).

* Finally, we will add the remaining meetings to the output and merge it with the last added meeting (if the last added meeting starts before the previously added meeting).
