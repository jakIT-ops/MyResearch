## Description

The first functionality we’ll be building is to locate the nearest available drivers within the vicinity of a user. There are numerous Uber drivers roaming around in a city. For simplicity, we’ll consider the city as a Cartesian plane and assign the coordinates (0, 0) to the user’s location. When a user wants to book a ride, we’ll simply find k drivers with the shortest distance on the Cartesian plane. Here, k is the minimum threshold for choosing the closest drivers.

We’ll be provided a list containing a set of points on the Cartesian plane and a number k. Each set of points will represent the location of a driver. We need to find the k closest drivers from the user’s location.

## Solution

The Euclidean distance between a point P(x,y) and the origin can be calculated using the following formula: 

​​Now that you can calculate the distance between a user and all nearby drivers, how will you find the K nearest drivers? The best data structure that comes to mind to track the nearest K drivers is Heap.

We iterate through the array and calculate the distance between each driver’s current location and the user. We’ll insert the distances of the first K drivers into the Heap. Each time we find a distance smaller than the maximum distance in the Heap, we do two things:

* Remove the maximum distance from the Heap

* Insert the smaller distance into the Heap

This will ensure that we always have K minimum distances in the Heap. The most efficient way to repeatedly find the maximum number among a set of numbers is to use a max-Heap.

Below is an illustration of this process. We have mapped the city of Seattle onto the cartesian plane to get simpler latitude and longitude values for the driver’s location.




