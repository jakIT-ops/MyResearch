## Description

Zoom is an application that helps to connect many people all over the world. It uses a binary search tree (BST) to maintain the participants’ data on the server and client-sides. The participants’ data is sent from the server to the client in the serialized form and then deserialized into a BST on the client-side. Let’s assume that when a new client joins a meeting, it downloads the participant list for the meeting. The list is serialized into a BST and sent over the network from the server to the client. Once the list is received from the client, we will verify that it was received correctly and that no errors occurred during the transmission. This feature will show us how to validate the BST containing the client-side participants’ data.

## Solution

We assume that the server sends the sorted string array in the in-order form to the client. The strings in the array are either in increasing or decreasing order. In our case, we will consider a given sorted string array in alphabetically increasing in-order format.

Here is how the implementation will take place:

1. First, we check if the given array has one element or no element. Then, we return true.

2. Now, if the given array has more than one value, we alphabetically compare adjacent string values from one index with those of the next index.

3. If the next index value is greater than the previous index value, the loop executes for the next pair until it reaches the end of the given array.

4. During the loop execution, if the next index value is not greater than the previous index value, the loop terminates and returns false.

This way, we validate the given sorted strings, regardless of whether it is a valid binary search tree or not.



