## Description

A person has divided their workday into 15-minute time slots numbered as 1, 2, 3, ... n. People who want to schedule a meeting with this person choose any available time slot that suits them. Assume that this person’s calendar is now filled with jumbled up numbers that represent the time slots reserved for meetings. Your task is to find out what the longest consecutive time period in which this person will be busy is.

## Solution

The longest busy period can start from any of the array’s indexes, so we have to search the entire array. Additionally, for each slot, we need to look up the entire array for the next consecutive slot. We can use the set data structure and convert a linear time lookup to constant time to find the longest sequence of consecutive numbers.

Here is how the implementation will take place:

1. Initialize a set data structure and store the busy schedule in it.

2. Traverse the input array, and for each time slot, check if the next consecutive slot is in the array or not.

3. If the above condition is true, keep incrementing the slot number until we get a slot that is not in the set.

4. We will keep the count of consecutive slots in a variable. If the current longest slot count is greater than the previously calculated one, we will replace it with the current one.

5. Return the largest slot count at the end.




