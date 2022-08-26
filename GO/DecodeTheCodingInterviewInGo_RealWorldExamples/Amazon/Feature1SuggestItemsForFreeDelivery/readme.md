## Description

For the first feature, we want to suggest products customers can buy to make their orders eligible for free delivery. The minimum order amount to qualify for free shipping varies by customer location. When a customer views their cart and the current total does not qualify for free shipping, we want to show them a pair of products that can be bought together to make the total amount equal to the amount required to be eligible for free delivery. You can assume that it was a corporate decision to show a pair of products instead of a single product. Historical data collected by your team shows that customers are more willing to buy multiple products as it gives the illusion of a better deal. Also, the UX team says that only two items should be displayed given the screen space for this feature.

## Solution

This feature can be easily implemented using hashing, meaning maps in Go. For every item price, p_i
p 
i
​
 
, we will look for p_i - n
p 
i
​
 −n
 in the map. Then, we will check whether each product’s complement exists in the map or not. This will continue until a product’s complement is found, and the indices of these products will be returned.

The algorithm’s complete steps are given below:

* Create a map called buffDict, which will be used to store the products’ prices.

* Then, iterate over the itemPrices list and calculate the remaining amount for each product by subtracting its price from the given amount.

* Check if the remaining amount is present in the buffDict; if it’s not present, add this amount in the dictionary as a key and set the index i as the value.

* On the other hand, if the remaining amount is present in the buffDict, return a list containing the value (index) of the product from the dictionary with the key equal to the remaining amount and the index of the current product, i.

