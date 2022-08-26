## Description

Like in the previous feature, the participant data of a Zoom session is maintained using a binary search tree. This is beneficial because the sorted order of names on the display does not change even when participants join or leave the meeting. We’ll assume that this binary search tree is maintained on both the server and client sides. However, while transmitting this information back and forth, we also want to serialize the data, send it from the server to the client, and then deserialize the data received by the client into a BST. Therefore, we need to create two modules: a serializer that deserializes the data before sending it through the network and a deserializer that translates the serialized data into its original form.

## Solution

We can perform a tree traversal to efficiently serialize a BST into a string. We will be using pre-order to implement the tree traversal because it will be slightly easier and more efficient to deserialize it later. However, any other traversal can be used. Let’s take a look at the algorithm in detail:

### serialize:

* The serialize() function takes the root of the BST as input.

* An inner function called preOrder() is called on the root, which populates a list by first appending the root value. Then, it recursively calls preOrder() on the left subtree. After that, we will make a recursive call to preOrder() on the right subtree.

* A comma is appended to the list entry as a delimiter; this will be helpful later for deserializing.

* The resultant list is converted into a string using join(), and the string is returned.

### deserialize:

* The deserialize() function takes the data string as input, which represents the serialized BST.

* Using the Split() function with , as the delimiter, the string is converted into a list.

* Then, we will traverse this list and create a BST by inserting data in the root node.

* Finally, the root node is returned when the traversal ends.


