## Description

Several users made a number of Facebook posts every day last month. We have stored the number of daily posts in a list. We want to mine these posts for information. We have k worker nodes to process the data. For optimally exploiting the temporal relationship between the posts, each worker node must process posts from one or more consecutive days. There will be a master node among our k worker nodes. This node will be in charge of distributing posts to other nodes, as well as mining the posts itself. Given an allocation of tasks to workers and the master node, the master node should get the smallest task. To efficiently utilize our resources, we want an allocation of tasks that maximizes the task allocation to the master node, so we have optimal utilization of worker nodes processing power. There can be a lot of posts a day, so input posts for each day would be in thousands.


## Solution

We have to search for the maximum number of posts that can be assigned from a list of integers. We can use the binary search with some modifications to compute this value. In a typical binary search, we compute the middle value in the list. If our target value is greater than this middle value, we move to the right portion of the list. Otherwise, we move to the left portion. We have found the element at which our target becomes equal to the middle value.

For this problem, our target is to optimally divide the number of posts into k nodes. This is a two-step process:

First, use binary search to maximize the minimum sum of subarrays in a split.
Then, figure out if such a split is possible.
What’s the maximum possible sum that any split could have? One extreme is everything gets assigned to one node, sum(posts). No one gets anything to do. However, we know that this isn’t a valid split because it isn’t a split at all. Can we do better than this? Sure. How about the average, sum(posts)/k? That’s a good starting point. The minimum subarray sum will definitely be smaller than or equal to the mean. We can assign the lower bound to 1 since, at minimum, the master node will be assigned a single post to process.

So, start with low = 1 and high = sum(posts)/k. Then, binary search for the maximum sum of the smallest subarray sum over all the splits. We first check if it is possible to get a k-way split such that the smallest subarray has a sum less than or equal to mid = (high + low) / 2. If possible, we check if we can find a split with an even higher minimum subarray sum by setting low = mid. If not, we check if a smaller minimum subarray sum is possible by setting high = mid - 1.

How do we check if a split is possible for a given target minimum subarray sum? We just iterate over the array’s elements and keep accumulating elements into a single subarray as long as the sum doesn’t exceed mid. As soon as that happens, we declare the current subarray “closed” and “open” the next sub-array. We are splitting the array into subarrays such that their sum doesn’t exceed mid. If the number of such subarrays is less than k, we were aiming too high. Otherwise, we were aiming too low. We’ll keep doing this until our search condition low < high returns false as at that stage the mid value will have converged to the optimal one.

Here is how we will implement this feature:

1. Initialize low and high, as described above. Also, initializing the variables target and division to zero as target would denote the posts we currently have because we traverse over the list and division will tell us how many days we would get after dividing the list in mid amount of posts.

2. As long as low < high, compute the middle value as (low + high + 1) / 2. Here, +1 includes the mid in our range. If we don’t include +1, we’ll be stuck in an infinite loop because we’ll always pick the same mid, which will be low.

3. Traverse the list and keep adding the posts until the target becomes greater than or equal to our mid, and do the following:

	* Increment divisions by 1.

	* Assign target to 0.

4. At the end of traversal, assign low = mid if the divisions are greater than or equal to the number of nodes. Otherwise, assign high to mid - 1.

5. When low < high returns false, return either low or high as they would have converged to the optimal value.












