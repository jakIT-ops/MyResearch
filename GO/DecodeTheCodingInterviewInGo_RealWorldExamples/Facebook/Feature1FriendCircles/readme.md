## Description

First, we need to find all the people that are in each user’s friends circle on Facebook. Your individual friend circle is defined as a group of users who are directly or indirectly friends with you. Assume there are a total of n users on Facebook. Some of them are your friends and others are not. The friendship/connection is transitive in nature. For example, if Shaw is a direct friend of Andy, and Andy is a direct friend of Noah, then Shaw is an indirect friend of Noah. Getting the total number of friend circles that exist on Facebook helps us suggest connections on Instagram for every user.

## Solution

We can think of the symmetric input matrix as an undirected graph. All the friends (both direct and indirect) who should be in one friend circle are also in one connected component​ in the graph. So, the number of connected components in the graph will give us the number of friend circles. We can treat our input matrix as an adjacency matrix; our task is to find the number of connected components.

Here is how we will implement this feature.

1. Initialize a list/array, called visited, to keep track of the visited vertices of size n with 0 as the initial value at each index.

2. For every vertex v, traverse the graph using DFS if visited[v] is 0. Otherwise, move to the next v.

3. Set visited[v] to 1 for every v that the DFS traversal encounters.

4. When the DFS traversal terminates, increment the friend circles counter by 1. This means that​ one whole connected component has been traversed.
