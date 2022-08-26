## Description

A planet has n genes, numbered 1 to n. Every species on the planet has a subset of these genes in its DNA sequence. For a given species’ DNA, A, we want to find the k^{th}
k 
th
 
 missing gene in a sorted order. The given DNA sequence will be sorted in strictly increasing order.

### Constraints

* 1 <= A[i] <= 1000

* 1<= k <= 1000

* A[i] <= A[j] for 1 <= i < j <= A.length

## Solution

Our input is sorted in an ascending order. We can use this fact and try to solve this problem using binary search. However, we need to find the number of missing genes that come before a given gene in the DNA A in order to use the binary search algorithm. To find the number of missing genes, we will compare our input array, A, with an array that has no missing genes.

Suppose that the input array, A, is [2, 3, 4, 7, 11]. We will compare it to an array with no missing genes, that is, [1,2,3,4,5]. The number of missing genes is the difference between the corresponding elements of the two arrays.

The number of missing genes before the gene, A[i], is equal to A[i] - i - 1. The following illustration shows how we can use this formula to get the number of missing genes before A[i].


