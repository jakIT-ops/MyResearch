## Description

In addition to other important tasks, Amazon’s logistic division is responsible for delivering packages. They have partnered with many delivery services so that the orders can reach customers quickly. One of the carrier companies has pricing criteria; we want to use that criteria to our advantage so that we can deliver maximum packages at minimum cost. This carrier is willing to send one or more trucks for deliveries as needed, but they charge in increments of k
k
 lbs. The vendor has different size truck (in increments of k
k
 lbs) available. Anything below k
k
 lbs costs $10. Whereas, anything between k
k
 and 2k
2k
 lbs costs $20 and so on. If we ship anything less than n∗k
n∗k
 lbs, where n
n
 is a natural number, we are not fully utilizing the money we’re spending. So, we want to fully utilize the cost.

Your task is to write a program that looks at the current lineup of the packages and determines if we can fully utilize the cost by delivering n number of packages from the lineup; n is greater than or equal to 2. One thing to note is that the packages are arranged so that adjacent packages are to be delivered to near locations. So, we always want adjacent packages to be delivered together. Therefore, the chosen n packages should appear back to back in the lineup.

Consider an example where the weights of the packages are given to you in the form of an array, [11, 42, 54, 44, 49, 26], and the value of k is 10. Now, we need to check if we can efficiently load and utilize the delivery contractor given the packages in the delivery dock. The example should return true because the mentioned condition is satisfied.

## Solution

To solve this problem, we will calculate the cumulative sum of the products in the array and use the remainder theorem to determine if n products containing the sum of weights equal to n * k exist or not. Let’s take a look at the complete algorithm.

* First, we will find the cumulative sums up to the i^{th}
i 
th
 
 index and find the remainder after the division of the sum by k.

* Then, these remainders will be stored in a hash table structure, and the cumulative sum will be equal to the remainder. However, before storing the reminder in the hash table, we will check if the value of remainder already exists for any other index, j
j
. If the value does not exist, we will add another entry in the hash table.

* If the remainder already exists, this is the case we are looking for. To understand this, let’s take a look at the remainder theorem:

(a+(n * k))\%k = (a\%k)
(a+(n∗k))%k=(a%k)

* In case of the [11, 42, 54, 44, 49, 26] array and k = 10, the running sums are [11, 43, 57, 51, 50, 26] and the remainders are [1, 3, 7, 1, 0, 6]. We have remainder 1 at index 0 and at index 3. This means that in between these two indexes, including the right bound, we must have added a number that is a multiple of k. If indexes i and j give the same remainder, the values at i + 1 to j will satisfy the condition. So, for this example, [42, 54, 44] sum up to a multiple of k.

* If the same remainder value is encountered again during the traversal, we return true directly.
