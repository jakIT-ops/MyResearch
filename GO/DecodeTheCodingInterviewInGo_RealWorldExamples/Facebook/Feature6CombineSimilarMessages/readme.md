## Description

Someone is posting messages on Facebook that are apparently gibberish. Research has indicated that the author picks every word and mutates it by adding a fixed offset value to each letter in the word. For example, they may mutate hy to iz by adding 1 to each letter of hy. Similarly, they may mutate hy to ja by adding 2 to each letter of hy, etc. We want to decode these messages. The first step is to group all the words that may be mutations of each order to make further analysis easier.


## Solution

From the above example, we can see that the difference between consecutive characters of each word is equal for each set. Consider the words lmn and mno from Set 1 of the example above. The difference between the ASCII values of each pair of consecutive characters of lmn is (1, 1), respectively, and the difference between each character of mno is also (1, 1). Words that are shifted versions of each other have identical character code differences. Using this, we can combine shifted words into separate sets. We can use a HashMap in which the keys can be represented by the differences between adjacent characters. The words that have these differences between their characters will be mapped as the values of these keys. For example, (1,1) will be a key with lmn and mno as its values. When all words are processed, the values of our HashMap will be the different groups.

In Set 2 of the above example, a wrap-around case occurs. In the string azb and bac, z(122) - a(97) gives us 25, but a(97) - b(98) gives us -1. If we don’t take care of this case, these two messages would end up being in two different sets. So, if any difference is less than zero, simply add 26 to it. For our case, -1 + 26 gives us 25, which is correct since, in reality, a is 25 steps away from b moving in a forward direction.

Here is how we will implement this feature:

1. Create a generateKey() function that takes a string and returns their character differences. This function will start traversing from the second character and will compute all the subsequent differences in a string.

2. Initialize a Map called messageGroup.

3. Traverse the list of strings, and for each string, compute the key value using the generateKey() function.

4. If a key is present in messageGroup, append the current string to it. Otherwise, add the key and then append the string to it.

5. Return messageGroup when the iteration ends.




