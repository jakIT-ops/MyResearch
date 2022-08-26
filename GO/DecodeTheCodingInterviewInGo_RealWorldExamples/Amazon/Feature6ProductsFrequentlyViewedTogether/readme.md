## Description

We want to improve the recommendation system of products at Amazon. For this purpose, the management has decided that if a group of products is searched or viewed back to back by users, these products are similar or related. So, if another user is browsing one of these products, we can recommend the other ones to them. To determine these similar products, we will look at the previous activities of all users and check if particular products are viewed back to back.

Your task is to create a module that is given a dataset of product IDs in the order they were viewed by the user. You will also be given a list of products that are likely similar. Your job is to find how many times these products occur together in the dataset. The order of their occurrence does not matter unless they are back to back without any other products in between.

For example, let’s say the dataset of product IDs you are given is:[3, 2, 1, 5, 2, 1, 2, 1, 3, 4]. The candidates for similar products are [1, 2, 3]. We can see that these products occur together twice in the dataset, first at indices 0 to 2 and then at 6 to 8. The function’s output should be the list of the occurrences’ starting indices, which in this example is [0, 6].

## Solution

The basic idea behind this solution is to use a sliding window on the products dataset and keep a hashtable referring to the occurrences of the products in the sliding window. Another map will be kept for the candidates. At each step, the maps will be compared to check if a permutation of candidate products exists.

1. We will first create a map from the candidates list, called the candCount. This map will have product IDs as keys and their frequency of occurrence as values.

2. Then, we will use a sliding window with the capacity of candidates's size.

3. We will also create a map reference called prodCount for the products inside the sliding window.

4. As the sliding window moves, we will recompute prodCount in constant time by adding one product to the right and removing one product from the left.

5. While moving the sliding window, we will compare the maps. If they are equal at any point, this means that the window is a permutation of the candidates list. So, we will update the result.

6. The result will be returned at the end when the products list is completely traversed.





