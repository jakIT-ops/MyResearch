## Description

Alice and Bob have created some posts on their walls. Each of the posts contain one or more “topics.” We want to mine their sequence of posts to find any overlap in the topics. Specifically, we want to find the shortest sequence of posts by Alice that have mentioned all the topics that Bob has also posted about.

In this problem, we have two lists. List A contains all of the topics that Alice posted about, namely: `["corona", "petrol", "climate", "cricket", "climate", "corona", "soccer", "music", "submarine", "elections"]. List B contains all of the topics that Bob posted about, namely: ["corona","climate"]`. Now, we want to take a snapshot of the smallest contiguous portion of Alice’s wall in which she has mentioned all the topics that Bob talked about in his posts. To solve this problem, we need to find the smallest sequence of topics mentioned by User Y (including duplicates), which overlaps with the topics mentioned by User X. In our case, the smallest sequence is `["climate","corona"]`.

## Solution

We need to return the smallest sequence in List A that contains all of the topics from List B. A desirable sequence is a sequence of elements from List A in which both the first and the last elements are also members of List B, and all of the elements of List B are present in the desirable sequence. This feature requires finding the smallest desirable sequence from A. We’ll solve this problem using the sliding window approach.

We use two pointers, say left and right, in the sliding window approach. We use both of these pointers to expand and contract the window, respectively. We only move one pointer at a time, and we keep the other pointer fixed.

We first filter our List A. Then, we create a new list, say sifted list. This list will contain all the elements along with their indices of List A that are also present in List B. For example:
```
A = ["soccer", "climate", "corona","petrol", "cricket", "elections","china", "forest","soccer","corona","forest","Isreal" ]
B =["soccer","forest"]
sifted_list = [(0, 'soccer'), (7, 'forest'), (8, 'soccer'), (10, 'forest')]
```

We then iterate through the sifted list, and we keep expanding and contracting (if possible) our desirable window, until it contains all of the required topics. We save the window, which contains the smallest sequence. In the end, we will then have our smallest sequence, which will hold all the topics.

Let’s try to understand this using an example:

```
A = ["corona","petrol","corona","corona","climate","petrol","petrol","corona"]
B = ["corona","petrol","climate"]
```

smallest sequence = ["corona","climate","petrol"]
We first filter out our List A such that our new list, that is, the sifted list, only holds the topics (along with their indices) that are also present in List B. We then start with the pointers left and right, pointing to the same first index of the sifted list. Once we have a desirable window, we increment the left pointer one by one and check if the window is still desirable. If it is, then we keep moving the left pointer forward. If the window is not desirable, then we expand the window using the right pointer and repeat the process until we have our smallest sequence.



