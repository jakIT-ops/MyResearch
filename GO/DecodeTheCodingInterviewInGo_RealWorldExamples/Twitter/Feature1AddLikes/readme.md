## Description

For the first feature of the Twitter application, we are creating an API that calculates the total number of likes on a person’s Tweets. For this purpose, your team member has already extracted the data and stored it in a simple text file for you. You have to create a module that takes two numbers at a time and returns the sum of the numbers. The inputs were extracted from a text file, so they are in the form of strings. The limitation of the API is that we want all of the values to remain strings. We cannot even convert the string to numbers temporarily.

For example, let’s say you are given the strings "1545" and "67" as input. Your module should not convert these into integers while computing the sum and return "1612".

## Solution

To solve this problem, we will do digit-by-digit addition because we cannot convert the strings to integers. The algorithm for decimal addition is given below:

* First, we will initialize an empty res variable.

* Then, we will initialize the carry as 0.

* Next, we will set two pointers, p1 and p2, that point to the end of like1 and like2, respectively.

* We will traverse the strings from the end using p1 and p2 and stop when both strings are done.

* We will set x1 equal to a digit from string like1 at index p1. If p1 has reached the beginning of like1, we will set x1 to 0.

* We will do the same for x2, setting x2 equal to the digit from string like2 at index p2. If p2 has reached the beginning of like2, we will set x2 to 0.

* Now, we will compute the current value using value = (x1 + x2 + carry) % 10. Then, we will update the carry, like so: carry = (x1 + x2 + carry) / 10.

* We will append the current value to the result.

* If both of the strings are traversed but the carry is still non-zero, we will append the carry to res as well.

* At last, we will reverse the result, convert it to a string, and return that string.
