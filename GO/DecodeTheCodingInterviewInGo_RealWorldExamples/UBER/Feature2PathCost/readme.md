## Description

Now that some drivers have been selected, we need to calculate the cost required to travel between different checkpoints. The cost depends on the amount of water accumulated in different parts of the road. We know that water collects on roads that are either broken or uneven. We will use an API to access the data regarding water on the road, it will transform the 3D layout of the road into a nice 2D layout of water trapped between different parts of the road.

We’ll be given a list whose length is equal to the length of the road between two checkpoints. Each integer value on the list will represent the combined elevation(in cm) of the road at the points where it is broken. We need to find how much total water(in cm) will be accumulated in the spaces left between different elevations of the broken road.

## Solution

We need to calculate the amount of water that has accumulated above each road elevation and sum it up. At a single index/elevation (X), the amount of water depends on the heights of the highest bars to it left and right, regardless of how far apart they are. Upon further exploration, we also observe that the elevation (X) + the height of the water above this elevation, is equivalent to the minimum height of the highest bars around it. Therefore, the accumulation of the water, above a certain point (X), can be calculated using the formula:











