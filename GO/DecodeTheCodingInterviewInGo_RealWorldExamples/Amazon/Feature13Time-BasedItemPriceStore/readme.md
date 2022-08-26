## Description

Thousands of items are sold on Amazon every minute. Some of the items don’t meet the buyer’s expectations and are returned. Item prices fluctuate over time. It’s possible for the price of a returned item to change since it was purchased. The customer should then be refunded the item price applicable at the time of purchase.

We want to store the prices of items using the timestamp in a data structure and update the price whenever needed, along with the current timestamp. When a customer wants to return an item, we’d like to query the item’s price at that time. An item’s price is unchanged until it is updated.

Our task is to design a time-based item price data structure that can store multiple prices for the same item at different time stamps and retrieve the item’s price at a certain timestamp.

## Solution

Let’s approach this problem in the following way:

* TimeMap struct declares a struct containing two hash maps, Prices and TimeStamp, where Items will be the keys, and Prices and Timestamp will be the values.

* Set(Item string, Price string, Timestamp int) stores the key Items with the value Price at the given time Timestamp.

	* Check if the key Item already exists in the hash map. If it does, then check if the given Price of Item does not already exist at the last Timestamp in the Prices[Item]. If it already exists, the item’s Price and Timestamp will be stored in the Prices[Item] and Timestamp[Item] maps, respectively.

	* Otherwise, we will save the Item with its Price and Timestamp into the Prices and TimeStamp hash maps.
