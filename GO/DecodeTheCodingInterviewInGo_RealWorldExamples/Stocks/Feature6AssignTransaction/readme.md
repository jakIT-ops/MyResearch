## Description

Stock transaction requests arrive and are inserted at the head of a singly linked list. The transactions need to be carried out by K brokers, such that each transaction is independent of all others. K is a positive integer and is less than or equal to the length of the linked list. There are a total of N transaction requests in the linked list. The first \lfloor N/K \rfloor
⌊N/K⌋
 transactions need to be assigned to the first broker, the next \lfloor N/K \rfloor
⌊N/K⌋
 transactions to the second broker, and so on. In the end, some transactions (< N/K)
(<N/K)
 may still be left in the original linked list. A first-come-first-serve policy will not be guaranteed globally, but the subset of transactions assigned to a specific broker will need to be carried out in the same order in which they arrived.

We do not want to split the original linked list. We will just pass a pointer to the transaction at the beginning of each K-node, set to different brokers. However, since this is a singly linked list and the order of the transactions in the linked list is opposite to the order in which they need to be processed, we will require each set of \lfloor N/K \rfloor
⌊N/K⌋
 transactions in the linked list to be reversed. For this problem, we can assume that we are given a linked list of stock transaction requests, where an integer value represents each transaction request. We want to reverse the transactions in the list \lfloor N/K \rfloor
⌊N/K⌋
 at a time and return the modified list. We may not alter the values, and only the transaction, rather physically change the transactions in the linked list.

## Solution

To reverse \lfloor N/K \rfloor
⌊N/K⌋
 transactions in the linked list at a time is simply a linked list reversal algorithm. We will be using a linked list reversal function to solve this problem. First, let’s look at an algorithm to reverse a linked list:

* Suppose we have the starting node of the linked list, say head.

* Consider another pointer, revHead, which acts as the head of the reversed linked list.

* We will use a pointer, ptr, to traverse the original linked list.

* We will traverse the list and, for every element, we will insert the node at the beginning of the reverse list that has revHead as its head.

* We will keep moving the ptr pointer one step forward and inserting the nodes at the beginning of our reversed list. The linked list will be reversed once all the nodes have been inserted.



