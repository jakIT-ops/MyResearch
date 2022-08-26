## Description

In this feature, the user will be able to randomly browse through movie titles and read their summaries and reviews. We want to enable a Back button so the user can return to the previous title in the viewing history. We also want the user to immediately get the title with the highest viewer rating from their viewing history. We want to implement both of these operations in constant time to provide a good user experience.

## Solution

To enable a Back button, we need to store the user’s viewing history in some data structure. Pressing the Back button fetches the last viewed item. This indicates a last in first out (LIFO) structure, which is characteristic of a stack. In a stack, push and pop operations can be easily implemented in O(1)
O(1)
. However, the stack doesn’t allow random access to its elements, let alone access to the element with the maximum rating. We will need to create a stack-like data structure that offers a getMax operation, in addition to push and pop, that all run in O(1)
O(1)
.

The implementation of such a data structure can be realized with the help of two stacks: maxStack and mainStack. The mainStack holds the actual stack with all the elements, and maxStack is a stack whose top always contains the current maximum value in the stack.

How does it do this? The answer is in the implementation of the push function. Whenever push is called, mainStack simply inserts it at the top. However, maxStack checks the value being pushed. If maxStack is empty, this value is pushed into it and becomes the current maximum. If maxStack already has elements in it, the value is compared with the top element in this stack. The element is pushed into maxStack if it is greater than the top element else, the top element is pushed again.

The pop() function simply pops off the top element from mainStack and maxStack.

Due to all these safeguards, the maxRating function only needs to return the value at the top of maxStack.



