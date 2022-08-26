## Description

Suppose that the DNA of a virus from an alien species consists of 10 different nucleotides, which are represented by the numbers, 0 through 9. It mutates by transforming itself into a different permutation of the same nucleotides. A mutant with the next lexicographically greater permutation of nucleotides is most likely to survive. This is referred to as the most potent mutation of the virus. Once it has mutated to the lexicographically highest possible permutation, it rearranges its nucleotides to the lowest possible permutation.

In this problem, we are given a sequence of nucleotides. To get the next greater sequence of nucleotides, we have to rearrange the nucleotides into their next lexicographically high permutation. If such an arrangement is not possible, the nucleotides must be rearranged to the lowest possible permutation.


## Solution

Observe that no other higher permutation is possible if the sequence of nucleotides is in descending order. For example, no higher permutation is possible for the given sequence:

```
[3,2,1]
```

To find the solution, we traverse the sequence from the right to find the first pair of two consecutive numbers, num[i] and num[i-1], such that they satisfy the condition num[i] > num[i-1]. By this point, we know that the subsequence to the right of num[i-1] consists of numbers that are in descending order, so no rearrangement of these numbers can create a higher permutation. Therefore, we need to arrange the numbers to the right of num[i-1] including the number itself.

We know that our task is to find the permutation that is larger than the current permutation. Therefore, we replace num[i-1] with a number, say num[j], which is larger than itself and among the numbers that are in the subarray to the right of num[i-1]. This is demonstrated below.
