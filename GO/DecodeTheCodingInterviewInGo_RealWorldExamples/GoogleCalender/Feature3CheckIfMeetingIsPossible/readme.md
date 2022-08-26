## Description

For this feature, we want to program a function that will let User A know if it is possible to schedule a meeting with User B or not. This decision will be made based on User B’s meeting schedule. If the new meeting’s time overlaps with an existing meeting in User B’s schedule, then the new meeting can not be scheduled.

You will be given a list of start and end times of User B’s scheduled meetings, which are non-overlapping. Additionally, you will be given the start and end times for the proposed meeting, which we need to verify is schedulable.

Suppose that the list of timings is [[1, 3], [4, 6], [8, 10], [10, 12], [13, 15]], and the new meeting is [7, 8]. In this example, you can see that the new meeting does not overlap with any existing meetings. Therefore, it can be scheduled, and the output will be true. Now, consider if the new meeting had been [9, 11]. It would have overlapped with [8, 10] and [10, 12]. Therefore, the output would have been false.

## Solution

This feature can be implemented by brute force traversal. However, we can make it more efficient using a Binary Search Tree (BST). The main advantage is that we can insert all the meetings in a BST first, and then check if the new meeting can also be inserted without any clash. Placing the meetings in a BST in sorted order lets us verify whether the new meeting can be added in O(log(n))
O(log(n))
 time.

Here is how we will implement this feature:

* `BST` structure: First, we will implement a simple BST data structure with an Insert function, and an AddNode function.

	* Insert() function: This function takes in the start and end timing of meetings and creates a new node. If the root is nil, then the new node will become the root. Otherwise, the recursive helper function AddNode will be called. The return type of this function is Boolean, as we will use it to determine if the node was added successfully.

	* `AddNode()` function: This recursive helper function has two inputs: currentNode, which is initially the root node, and the newNode to be added. We will check if the newNode starts before the currentNode ends; this shows that there is no conflict up to this point. This means we will have to call the recursive function again to check for a conflict in the right child of the currentNode. If the previous check does not pass, we will check if the newNode starts after the currentNode and similarly call the recursive function for the left subtree if the check passes. If both of these conditions fail, this means that the new meeting overlaps with an existing meeting. Therefore, we will return false.

* `checkMeeting()` function: We initialize the BST with the user’s scheduled meetings in this function. Then, we will add the new meeting and return the result.



