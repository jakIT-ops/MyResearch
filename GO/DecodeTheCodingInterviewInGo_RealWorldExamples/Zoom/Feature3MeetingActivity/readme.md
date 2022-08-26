## Description

A large number of employees across the globe had to switch to working from home during the pandemic as their companies shut offices down. In this situation, Zoom is a popular collaboration tool, and the number of people using Zoom to work from home is increasing daily. Working from home has caused a lot of stress for employees and has made team building challenging for the employer. Employers have introduced several remote activities that help people relax and get to know each other. Zoom wants to play its part in this by providing fun team activities for online meetings. Zoom has decided to introduce mini games that can be played during meetings. One game they are making is a guessing game that is played on a timer. In this game, the user will be shown an image of stairs with n steps numbered from 0 to n - 1. Each step on the stair also has a number written on it. The player’s answer will be the minimum number of steps that a sprite at the bottom of the stairs needs to take to get to the top.

Your task is to implement a function that can find the correct answer given an array, k, containing the values written on the steps of the stairs. The rules of the game are the following:

* The sprite can jump from step i to step i + 1, where i + 1 < n.

* The sprite can jump from step i to step i - 1, where i - 1 >= 0.

* The sprite can jump from step i to step j, where k[i] == k[j] and i != j.

## Solution

This problem can be mapped as a graph problem in which we need to find the shortest path between two vertices. So, to solve this problem, we will use a breadth-first search.

* First, we will build a graph. This will be an unweighted, undirected graph, and the indices of k will represent nodes.

* There will be an edge between the nodes corresponding to the surrounding indices and also to the other indices that have the same value. We will store nodes with the same value together in a graph map.

* Now, we will do a breadth-first search and find all paths from the first index to the last.

* However, if we already checked one index, we do not need to check it again. We can mark the index as visited by storing it in a visited map.

* While searching, we do not need to iterate the whole list to find the nodes with the same value as the next steps, we need to consult the precomputed graph map. However, to prevent retracing our own steps, we need to clear the corresponding hash table entry once we reach a specific node.





