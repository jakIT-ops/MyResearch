## Description

Our stock trading company is hiring interns. Different interns start on different days. Each intern is given a target to close at least three trades on any given day and log these trades using automatically incrementing sequence numbers. Each intern will close trades numbered 1, 2, 3, .... Since different interns have spent a different number of days on the job at any given time, one may be closing trade number 2 while another is closing trade number 23.

Before you arrived, a developer wrote a logging application for the interns. The application accepts trades sequence numbers from the interns and stores them in a centralized log. The logs keep separate records for each day. Unfortunately, the developer didn’t include the intern IDs in the log records. To complicate matters further, the developer sorted the list of trade numbers before storing it in the log. For example, consider a day on which three interns were working. They logged the following trades: [1, 2, 3, 4], [4, 5, 6] and [10, 11, 12]. The log for this day would say [1, 2, 3, 4, 4, 5, 6, 10, 11, 12].

Given a day’s record log, we want you to figure out if every intern working on a given day submitted at least three deals for the day or not as accurately as possible. Note that if the log said [1, 2, 3, 4, 5, 6, 10, 11, 12], we can’t be certain if there were three interns working or two. However, all we are interested in is a true/false answer, which would be true in the above case. If on a given day, there is no way that any number of interns could have reported at least three deals, return false.

We’ll be provided with a list of sorted numbers representing trades. This list actually contains the different sets of trades made by interns organized in a sorted manner. Our task is to determine if subsequences/sets with at least three consecutive elements exist in them or not.

## Solution

We need to determine if valid subsequences can be made under the above-mentioned constraints. Each number can either be part of an existing subsequence, or it will make a new subsequence starting from itself. We’ll need two maps to store the count of our numbers. The first map, frequencyMap, will store the frequency with which a number occurs in our trades list. The second map, imaginedMap, will help us determine if a new number should be part of an existing subsequence or not.

When making a new sequence with a number n, we need to ensure there are at least two consecutive numbers in the list that follows n. We can use our frequencyMap to verify this. When a subsequence with at least 3 consecutive integers is found, we’ll add that sequence’s next number to our imaginedMap with its respective count. Initially, this count value is 1 because we are assuming the number for the first time. If we have to assume this number again, we’ll increment its count value. Currently, we are assuming that this number will only be part of our initial subsequence.

When we move to the next number in our list, we can check our imaginedMap to verify if this new number needs to join an existing subsequence or not.

Here is how we will implement this feature:

1. Initialize the two maps frequencyMap and imaginedMap.

2. Let frequencyMap[n] be the frequency of n and imaginedMap[n] be the next number of an existing sequence.

3. Traverse the trades list. If new subsequences are found, we will decrement their count and add the next assumed number in imaginedMap.

4. For every n, check if it exists in the imaginedMap. If it exists, we will decrement its count in both maps.

5. Otherwise, create a new sequence and repeat from step 3.





