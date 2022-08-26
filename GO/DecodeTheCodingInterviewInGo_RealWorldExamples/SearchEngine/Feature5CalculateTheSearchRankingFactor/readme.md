## Description

Consider that your company has decided to experiment with a different search ranking algorithm. This algorithm favors search results that reference each other and create a closed graph. All the web pages in the search result have already been assigned scores based on their content quality and relevance. Now, we want to determine the ranking factor of each page, which will be used in tandem with other criteria to determine the final page rank. To find this ranking factor, the team has decided to take the product of the scores of all pages that are referenced by the current page. This means that in the set of web pages where each one references the other, the ranking factor of each page will be determined by multiplying the scores of all the other pages in the set except itself.

To implement this feature, you will be provided with an array containing the page scores of web pages that reference each other. A page’s rank is calculated as the product of the scores of all the pages that link to it. For example, you are given the following scores of five web pages that link to each other: [1, 4, 6, 9]. The ranking factor found by the algorithm mentioned above will be: [216, 54, 36, 24].

## Solution

The optimal approach for solving this problem is that for every index, i, we will evaluate the product of all the numbers to the left and all the numbers to the right of i. Then, we will multiply those two individual products. This will give us the product of all the numbers except the one at the index, i.

The complete algorithm is given below:

* First, let’s start by calculating the product of all the elements to the left for each index.

* We will use a ranking array and start populating it with the product of the elements to the left. The product of the elements to the left for index 0 will be 1 because there are no elements to the left.

* Then, we will traverse the page scores from index 1. For each ranking[i], we will find the product of elements to the left by multiplying pageScore[i - 1] and ranking[i - 1].

* We have the product of elements to the left for each index stored in ranking. Now, we need to do the same for the right side and multiply both. We can use another array to do this. However, we will prioritize saving space and use a constant variable, right, to store the product.

* Initialize this variable with 1, and start traversing the list from the end.

* We will multiply right with ranking[i] to find the final ranking for the page at i. The right variable will also get updated at each iteration by multiplying it with pageScore[i].

* Finally, we can find the required page ranking factors in the resultant ranking list.



