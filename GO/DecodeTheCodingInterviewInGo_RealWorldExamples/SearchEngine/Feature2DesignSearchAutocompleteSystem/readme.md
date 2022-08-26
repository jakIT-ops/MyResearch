## Description

The second feature we want to implement is the auto-complete query. This is the feature that prompts the search engine to give you some suggestions to complete your query when you start typing something in the search bar. These suggestions are given based on common queries that users have searched already that match the prefix you have typed. Moreover, these suggestions are ranked based on how popular each query is.

Assume the search engine has the following history of queries: ["beautiful", "best quotes", "best friend", "best birthday wishes", "instagram", "internet"]. Additionally, you have access to the number of times each query was searched. The following list shows the number each query string occurred, respectively: [30, 14, 21, 10, 10, 15]. Given these parameters, we want to implement an AutoComplete() function that takes in an incomplete query a user is typing and recommends the top three queries that match the prefix and are most popular.

## Solution

To design this system, we will again use the trie data structure. Instead of simply storing the words in the prefix tree, as we did in the WordDictionary, we will now store the query strings. The AutocompleteSystem type will act as a trie that keeps a record of the previous queries and assigns them a rank based on their number of occurrences.

We will implement the AutocompleteSystem type as follows:

* `new`: In the new function, we will feed the historical data into the system and create a trie out of it. We will initialize the root node of trie and call the AddRecord() function to add all the records.

* `AddRecord() function:` This function inserts records in the trie by creating new nodes. Its functionality is similar to the InsertWord() function that we discussed in Feature #1: Store and Fetch Words. Each node of the trie will have:

	* A children map

	* A Boolean called isEnd to set the end of the query sentence

	* A new variable called data that is optional, but we can use it to store the whole query sentence in the last character of the sentence. This will increase space complexity but can make computation easier.

	* A rank variable to store the number of occurrences

In the code below, you will notice that we are storing the rank as a negative value. There is a valid reason for doing this unintuitive step. Later, you will see that we will obtain the top three results, and this negative rank will play a significant role. This will be explained in more detail in the explanation for the AutoComplete() function.

* `AutoComplete()` function: This function checks if the input string is not the end of string delimiter "#". If it is not the end of the input string, we append the value to the keyword member variable. On the other hand, if the input string is the end of the input, we add the value present in keyword to the trie by calling AddRecord(). Next, the value of the keyword variable is reset to an empty string. Before returning, you can see that we do some computation on the result list. We will fetch the first three elements of the sorted list. From this list of three tuples, we will create a list containing only the second element of each tuple, meaning only the sentences. Finally, we return it. If we had used the actual positive value for rank, we would have needed to sort ascending for sentence and descending for rank.






