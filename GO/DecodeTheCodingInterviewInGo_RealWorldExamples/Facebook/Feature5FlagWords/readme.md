## Description

Facebook recently conducted a survey on the techniques people use to hide offensive or profane words. The goal was to flag such words in the posts and messages of users. The most observable pattern was that the characters of a word were repeated multiple times to avoid detection. A single character in a word was observed to be repeated at least 3 times. This means that characters repeated less than 3 times will be ignored in the detection process

## Solution

Since we have to observe letters of two strings at a time, we can follow a two-pointer approach to solve this problem.

Here is how we will implement this feature:

1. Initialize two pointers, i and j, to start traversing from S and W, respectively.

2. Check if letters currently pointed to by i and j of both words are equal. Otherwise, return false.

3. For each equal letter found:

	* Get the length of the repeating sequences of the equal letter found in both words.

	* The length of the repeating sequence of W letters should be less than or equal to the length of the repeating sequence of S letters.

	* The length of the repeating sequence of S letters should be greater than or equal to 3.

4. If any of the conditions mentioned in step 3 fails, return false.

5. If the ends of both strings are reached, return true.


