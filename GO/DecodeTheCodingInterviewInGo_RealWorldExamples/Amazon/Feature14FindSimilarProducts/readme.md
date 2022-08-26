## Description

We want to create a product recommendation system. Product recommendations are an important business function. It’s important and beneficial for a business to recommend the right products to groups of users with similar tastes and interests. To recommend the right products, first, we must find people with similar tastes.

We are given the products that were purchased recently by two users. We want to find how similar their purchases were by finding the products that they both purchased.

Suppose we have 1000 products in total and each user can buy a maximum of 1000 products at a time. Given two lists that represent the products recently bought by the two users, our task is to find all the items that both of them purchased.

## Solution

To solve this problem, a beginner’s approach will be to iterate along the first array, ProductsIds1, and check if each product is present in the ProductsIds2 array or not. If each of the products is present in the ProductsIds2 array, we’ll add the product ID to the output. This approach will give us \mathcal{O}(n \times m)
O(n×m)
 time complexity, where n
n
 and m
m
 will represent the lengths of the arrays.

The number of products that a user can buy is fixed at 1000. We can exploit this property and create an array to determine if both the users purchased a particular product or not. For each product in the ProductsIds1 array, we will set the count in the respective element of this array to 1. Then, we will iterate in the ProductsIds2 array. If the count is 1 for any product of the ProductsIds2 array, we will set the respective element in the array to 2, which will denote that the product exists in both the ProductsIds1 and the ProductsIds2 arrays.

Let’s look at the flow that we can follow to solve this problem:

* We will use a variable named counter of size 1001, because the maximum number of products that a user can buy is 1000. Then, we will initialize this counter to 0 and use it to keep track of the count of each product present in ProductsIds1 array.

* First, we will set the counter to 1 for each ID present in the ProductsIds1 array.

* Then, for each ID in ProductsIds2, we will check if the counter is 1. If that is true, then we will set the counter to 2.

* At last, we will check for each id in the counter. If the counter is greater than 1, then we will add that product ID to the SimilarPurchases array.

* Finally, we will return the SimilarPurchases array.


