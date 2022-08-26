## Description

For the next feature, you have to implement a module that adds a user’s Tweets into an already populated Twitter feed in chronological order. Let’s assume that userA just started following userB. At this point, we want userB's Tweets to show up in userA's Twitter feed. We already have a chronologically sorted list of Tweets that will appear on userA's feed. Your job is to merge it with the list of userB's Tweets, which are also chronologically sorted.

As input, you will be given two sorted integer arrays, feed and tweets. The integers represent the posting time of the Tweets. You are also given the number of elements initialized in both of the arrays, which are m and n, respectively.

## Solution

We can solve this problem by comparing both arrays from the end and populating the result in the feed array. Take a look at the complete algorithm below:

* First, we will initialize two pointers, p1 and p2, that point to the last element of each array. (The last element of feed, or the element at the m-1 index, is the last initialized element.)

* Next, we will initialize another pointer called p, which will point to the m + n - 1 index of the feed. We will use this pointer to populate the result.

* Now, we will use the pointer p to traverse the feed array from the end.

* If the value at p1 is less than the value at p2, the result at p will be equal to the value at p1. Otherwise, the result at p will be set equal to the value at p2. We will decrement the pointer for the list that the entry was copied from.

* The traversal will continue until tweet is merged.











