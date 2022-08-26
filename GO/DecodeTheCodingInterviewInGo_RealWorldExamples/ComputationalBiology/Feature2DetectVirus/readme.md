## Description

While studying different DNA samples, we observed that a certain virus consists of really long sequences of k distinct nucleotides. The virus infects a species by embedding itself into the species’s DNA. We are working on devising a test to detect the virus. The idea is to analyze the longest string that consists of, at most, k nucleotides from a species’s DNA.

We’ll be provided with a string representing a chromosome from the infected DNA and a k value supplied from a hidden function. Our task will include calculating the longest subsequence from the chromosome string that has k unique nucleotides.

## Solution

Since we want to return a substring from a specific window over the original string, we can use a sliding window approach to accomplish this efficiently. We’ll use two pointers, left and right, to denote the boundaries of our sliding window.

Initially, both our pointers will be at the beginning of the string at position 0. We’ll keep moving the right pointer to the right as long as there are k distinct characters in our window. If we get k + 1 distinct characters at any point, the left pointer will be moved to the right to prevent keeping more than k distinct characters in our window.

We can use a map to control the movement of the left pointer so that we always have only k distinct characters in our window. The characters will be stored as keys in the HashMap, and those characters’ rightmost positions will be their corresponding values. Remember that the HashMap can only entertain k + 1 entries. When we get k + 1 entries, we need to move the left pointer to ensure our window contains only k distinct characters. We’ll also remove the character with the lowest position number from the HashMap.

We will maintain two dummy variables: start and end. After each iteration, we’ll update their values with the left and right pointers if the (end - start) difference is less than the (right - left) difference. In the end, the start and end pointers will contain the virus’s location.

Let’s see how we might implement this functionality:

1. Return 0 if the string is empty or if k is equal to zero.

2. Initialize the left and right pointers. Assign them the value 0. Initialize the two other start and end variables with the value 0 as well.

3. Traverse the string with the right pointer and keep adding the current value to the HashMap.

4. If the HashMap contains k + 1 distinct characters, remove the leftmost character from the HashMap and move the left pointer so that the sliding window contains only k distinct characters.

5. At the end of each iteration, assign the left value to start and the right value to end if the (end - start) difference is less than the (right - left) difference.



