## Description

To develop this project’s first feature, we are given a set of meeting times. Our job is to implement a solution that can identify the number of meeting rooms needed to schedule the required meetings. Each meeting time will contain a startTime and an endTime that are both positive integers.

Our list of meetings times looks like the following: [[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]]. If we schedule each meeting in a separate room, that would require six rooms. However, we want to use the minimum number of rooms possible. In the example, we can see that the first three meetings, [2, 8], [3, 4], and [3, 9], are overlapping. Therefore, each of them will require a separate meeting room.

## Solution

We can use a heap or priority queue to keep the meeting timings, where the key would be the endTime of each meeting. This way, we can check if any room is free or not by simply checking the heap’s topmost element. The room at the top of the heap would get free the earliest out of all the other rooms currently occupied.

If the room we obtain from the top of the heap isn’t free yet, then this means no other room is free either. So, we can allocate a new room in this condition.

Here is how the implementation will take place:

* Sort the given meetings by their `startTime`.

* Allocate the first meeting to a room and add an entry in the heap with the meeting’s endTime.

* Traverse over the remaining meetings, and keep checking if the meeting at the top of the heap has ended or not. This will tell us if a room is free yet.

* If the room is free, then we extract this element and add it again in the heap with the ending time of the current meeting we are processing.

* If not, then we allocate a new room and add it to the heap.

* After processing all the meetings, the heap’s size will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.





