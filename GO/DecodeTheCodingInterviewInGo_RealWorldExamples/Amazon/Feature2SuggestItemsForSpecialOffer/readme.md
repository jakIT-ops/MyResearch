## Description

In this scenario, Amazon held a lucky draw contest and the customers who won, have been given a $200 shopping credit. The restriction placed by Amazon is that the customers can only buy up to three products. Now, we want to help the customer by suggesting a list of triplets that contain products worth $200. In other words, a triplet will be a package deal containing three products that sum up to $200, and we want to suggest as many triplets as possible. To implement this feature, you will have access to a list of products that the customer is likely to buy. These products will include products from the person’s wishlist and other products based on previous purchases.

## Solution

This feature can also be implemented by using a dictionary. For every item with price, p_i
p 
i
​
 
, we need to find a pair of elements at list indices i + 1 to n that add up to 200 - p_i
200−p 
i
​
 
. To find the pair, we use the hashing technique mentioned in the previous lesson.

The following steps show the complete algorithm:

* First, we sort the list, then iterate the list and check if the price of the item at the current index is greater than 200. If so, the item can’t be part of a triplet in the result. Therefore, we will break from the loop.

* Next, check if the current value and previous value are the same. If this is true, then we will skip the current element.

* Now, call the twoProducts helper function with the itemPrices list and the current element’s index, i.

* In the twoProducts helper function, start iterating the list using the index j that starts from i + 1.

* Then, compute the complement by subtracting the prices of items at i and j from 200.

* For each complement, check if it already exists in the set called seen (you can also use a dictionary here). If it does not, store the current complement in the set.

* If the complement already exists in the set, this means that we have found the triplet. We will add the list of these three elements to the output list.

* Also, add itemPrices[j] into the seen set.


