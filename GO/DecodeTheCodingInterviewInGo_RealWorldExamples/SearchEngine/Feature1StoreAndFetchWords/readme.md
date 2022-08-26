## Description

For the first feature, your company wants you to design a module for the search engine that can be used to store and fetch words efficiently. This module will act as a dictionary with insert and search functionalities. Moreover, this dictionary should also have a feature for searching whether a given prefix exists in the dictionary or not. This feature can be represented by the startsWith function because a prefix comes at the beginning of the word.

Let’s say we insert the following words in the dictionary: the, a, there, answer, any, by, bye, their, and abc by calling the InsertWord() function. Then, by calling the SearchWord() function with input, there should return true. Similarly, calling the StartsWith() function with the prefix by should also return true.

## Solution

To implement this dictionary with efficient lookup times, we will use a trie data structure. Maybe you had already come to this conclusion, or maybe you were considering using a hash table instead. However, we will not use a hash table for this particular scenario is because it would be very inefficient for the prefix searching. Additionally, scaling hashtables for large datasets also increases collisions and space complexity. On the contrary, a trie is efficient in both time and space.


To implement the WordDictionary class, we will do the following:

* `Constructor`: We will initialize the root node of the tree in the constructor. This node will be of type Node. The Node class contains a dictionary of nodes and the Boolean isWord, which determines if the character is at the end of a word or not.

* `InsertWord() function:` In this function, we will take in a word as input. Starting from the root node, we will add the word’s characters to the children dictionary of each character as nested dictionaries. We will check if the child node with the character is present or not at each step. If it’s not present, a new node is initialized. For the last character of the word, we also set the isWord to True for the corresponding node.

* `SearchWord() function:` In this function, we begin checking from the root node to see if the first character exists in children. If it exists, we move on to that node and check its children for the next character. If at any point the node corresponding to a character is not found, we return false. If the whole word is found but isWord is not set to true for the last node, we return false as well. true is only returned if all the characters match and the word also ends at that point.

* `StartsWith() function:` This function is mostly the same as the searchWord function. The only exception is that we do not check if isWord is also set to true in the last-found node because we are not looking for a complete word, a prefix is enough. In the above trie, for instance, startsWith("th") should return true.








