### Description

Netflix has received a user complaint about the Back button we implemented in the previous feature misbehaving. The complaint was that the viewing history was not shown in the sequence it was accessed. Being the lead developer of this functionality, you went through the logs and retrieved the sequence of push operations and the sequence of pop operations in separate lists. Each new entry that the user clicked went to the push operations list. Each time the user clicked the back button, the removed entry went to the pop operations list.

The user also had a session where they browsed for some titles or pressed the Back button several times. The user did not browse the same title more than once. At the end of the session, the Back button was disabled. Unfortunately, these logs are separate and there are no timestamps. We want to know if the stack handled the user session correctly or if there may be a bug in the stack implementation.

We’ll receive two lists of push and pop operations. These lists will contain the ID’s of the pages that were browsed. We want to verify whether our implementation of the max stack is behaving correctly or not. To do this, we can check if the sequence of push operations and the sequence of pop operations have been interleaved and performed on a valid stack that was initially empty.

### Solution

From the above list, we get these push and pop lists:

`push = [1, 2, 3, 4, 5]`

`pop = [4, 5, 3, 2, 1]`

We only have the push and pop operations and not the timestamps for when they were performed. Since the user did not browse any title more than once and the Back button is disabled at the end. This means that every ID that was pushed to the stack must have been popped once.

After every push operation, we immediately try to pop. If the session is fine, all pushed elements will get popped at one point.

Here is how the implementation will take place:

1. Declare an empty stack.

2. Remove the element from the front of the pushed list and push it onto the stack.

3. If the element at the top of the stack is the same as the item at the front of the popped list, pop the element from the stack and remove it from the popped list.

4. If the stack is empty by the end, return true.

5. Otherwise, return false.






