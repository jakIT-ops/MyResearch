## Description

Amazon has acquired a grocery shopping website and is now integrating grocery shopping into their own website. In order to bootstrap their own site’s grocery section, they want to derive item relationships from the sales data of the company they acquired. The items in the affiliate’s store are stored as a linked list. For each product, we also have a pointer to the item that is most frequently bought with it. For example, the item most frequently bought with bread is eggs. In this example, the node for bread has a pointer to the node for eggs, in addition to whatever element is next in the list.

Now, you have been assigned the task of taking this linked list and making a deep copy of it for the new online store. The list’s Node will contain the following attributes:

* `prod`: The ID of the product

* `next:` Points to the next product in the list.

* `related:` Points to the product most frequently bought with the current product; this could also be empty if enough sales data about the product is not available.

## Solution

To make a deep copy of the list, we will iterate over the original list and create new nodes via the related pointer or the next pointer. We can also use a map/dictionary to track whether the copy of a particular node is already present or not.

The complete algorithm is as follows:

* We will traverse the linked list starting at the head.

* We will use a dictionary/map to keep track of visited nodes.

* We will make a copy of the current node and store the old node as the key and the new node as the value in visited.

* If the related pointer of the current node, i
i
, points to the node j
j
 and a clone of j
j
 already exists in visited, we will use the cloned node as a reference.

* Otherwise, if the related pointer of the current node, i
i
, points to the node j
j
, which has not been created yet, we will create a new node that corresponds to j
j
 and add it to visited.

* If the next pointer of the current node, i
i
, points to the node j
j
 and a clone of j
j
 already exists in visited, we will use the cloned node as a reference.

* Else, if the next pointer of the current node, i
i
, points to the node j
j
, which has not been created yet, we will create a new node corresponding to j
j
 and add it to the visited dictionary.

