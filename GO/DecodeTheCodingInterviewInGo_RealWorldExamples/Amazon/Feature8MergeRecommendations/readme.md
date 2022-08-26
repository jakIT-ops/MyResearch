## Description

Amazon has acquired a new company that already has a database of user-profiles and their corresponding product recommendation data. Now, Amazon wants to check if any of their current users have an account on the acquired website, so they can use the recommendation data. To accomplish this, Amazon has decided to merge the users’ accounts. We will be using the name of the user and the emails associated with their account to determine if multiple accounts belong to the same person. A person may have provided primary, secondary, tertiary emails, etc when setting up an account on either of the websites

You will be given a 2D array of accounts. Each element, accounts[i], is an array of strings, such that accounts[i][0] is a name while the remaining elements are emails associated with that account. You have to determine if two accounts belong to the same person by checking if both accounts have at least one email in common. Remember that if two accounts have the same name, they might belong to different people, as people can have the same name. However, all accounts that belong to one person will have the same name. Moreover, there can be more than two accounts made by one person.

## Solution

This feature can be mapped to a graph problem. We draw an edge between two emails, in case they occur in the same account. From here, the problem comes down to finding the connected components of this graph.

The complete algorithm is as follows:

* First, we will build an undirected graph by creating an edge from the first email to all the other emails in the same account. Each email is treated as a node and an adjacency graph will be made.

* Additionally, we’ll remember a map from emails to names on the side.

* Now, we will use a depth-first search starting with the first email.

* We will find all the nodes/emails that can be reached from the current email and denote it as a connected component. Then, we will add the respective name and this component, in sorted order, to the final answer.

* We will keep track of the visited nodes. If a visited node is found, this means that it was already a part of a previous component, so we can skip it.


