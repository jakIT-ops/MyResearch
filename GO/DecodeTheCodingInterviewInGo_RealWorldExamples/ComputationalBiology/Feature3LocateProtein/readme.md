## Description

Experiments have shown that a certain protein provides immunity against a specific virus. Unfortunately, the presence of the protein can’t be determined based on an exact match. Instead, we only know that like any other protein, this one has really long palindromic strings of nucleotides. To detect this protein, we need to first find the longest palindromic portion in an unknown sample.

We’ll be provided with a DNA generated protein sequence in the form of a string. Our task will be to locate and isolate the portion that has the nucleotides lined up as the longest palindrome to identify the correct protein.

## Solution

A palindrome is a string that reads the same backwards as forwards. For example, str = abba is a palindrome, but str' = abcd is not. Although there can be multiple palindromes in the input string, we have to find the longest one. There are two ways we can check if a string is a palindrome:

* Start two pointers from each end of the string. Move towards the center while checking that the element at each pointer is the same.

* Start two pointers from the center of the string. One pointer will move left and the other will move right while checking that the element at each pointer is the same.

We will use the second approach to solve our problem. We can traverse over the string, considering each position the center of a palindromic string. This way, we’ll find each palindrome within our string and return the longest one. This center position can either be a specific character in the string (if the string size is odd) or between two characters (if the string size is even). For example, if the string length is odd, say, abcba, the center exists in the middle. If the string length is even, say, abba, the center exists in between the two bb elements.

The longest palindromic substring may be odd in length. In this case, its central element would be a character in the original string. All n characters in the string must, therefore, be tried as a possible center of the longest palindromic substring. On the other hand, a palindrome could be even in length. In this case, its central element would be straddling between two characters in the original string. This means that n-1 positions must be tested for potential centers of a palindromic substring of even length. So, in total, there are 2n - 1 candidates for the center position of the longest palindromic substring in a string of size n.

Let’s see how we might implement this functionality:

1. Return an empty string if the input is null or of length 0.

2. Initialize the two start and end pointers. Assign them 0 at the start.

3. Write a function, returnPalindromeLength(s, left, right), to return the length of the palindromic string centered at that position specified as the left and right arguments. Since the center position for an even-sized substring is not an integer, instead of specifying the center index, we will pass the indices of the elements to the left and right of the center position. We will have a loop that runs n times.

4. In each iteration, we will call the returnPalindromeLength(s, left, right) function twice. In one call, we will pass the loop variable i as both the left and right indices - indicating a substring of odd length. In the other call, we will pass i for the left index and i + 1 for the right index.

5. The max of the two lengths calculated by the returnPalindromeLength(s, left, right) function would be the resultant length of the palindrome starting from the current index as its center.

6. The start and end pointers can then be updated using the index and resultant length value.

7. Return the substring from start to end+1.




