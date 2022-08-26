## Description

Amazon wants to upsell related products to the customer during checkout. Amazon wants to do this by recommending a single product picked randomly from a collection of several related products. You must implement three related features to recommend. First, you want to enable adding an item to the list of related products. Second, you want to enable removing an item from the list once it is deprecated. Lastly, you want to enable picking a random item from the list such that any item is equally likely to be picked. You must implement all of these features so that they run in O(1) time.

## Solution

This data structure’s most important feature is recommending products at random in O(1)
O(1)
 time. Let’s consider the data structures with constant time lookup, such as arrays and maps/dictionaries.

If we consider storing all the products in the array, given the index of the element, accessing that element will take O(1)
O(1)
 time. To implement the random functionality, we need to choose a random index first and then retrieve the array element. The problem with arrays is that deleting a value at an arbitrary index takes linear time.

Now, let’s consider maps/dictionaries. In maps, insertion and deletion occur in constant time. However, we can’t fetch a random product with the identifier because maps do not have identifiers. If we want to get a truly random product, we will have to first convert all the keys in the map into a list and then choose randomly. This will be a linear-time operation.

Both of these data structures have their own advantages. To benefit from both, we will create a hybrid data structure to store the products.

* Insertion: For the insertion in our data, we will store the product in a list. The index at which this product is stored will be inserted into the dictionary as a value, and the key will be the product. Both of these operations will take O(1)
O(1)
 time.

* Deletion: Using the dictionary, find the index at which the product exists. Swap the last product in the list, with the one to be removed. Then, change the key-value pair in the dictionary accordingly. Lastly, pop out the last element from the list.

* Get random: For this operation, we can choose a random index using the rand.Intn function in Go. The product at this index will be returned using the list.

