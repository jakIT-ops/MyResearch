## Description

The DNA for an alien species consists of a sequence of nucleotides. We can uniquely identify a species by finding the longest substring of nucleotides in the DNA, where no nucleotide appears twice. This substring of DNA is known as a species marker. Given an animal’s DNA, where each nucleotide is represented by a letter, we can find its species marker.

## Solution

The basic idea is to traverse the entire sequence of nucleotides and search for a substring in which no nucleotides appear twice. For each visited nucleotide, we can store its last occurrence in a hash map, with the key as the nucleotide and the value as its last position in the sequence.

Here’s how we implement this feature.

1. We initialize the following set of variables to 0 to keep track of the visited nucleotides:

	* stCurr: the starting index of the current substring.

	* longest: the length of the longest substring.

	* start: the starting index of the longest substring.

	* currLen: the length of the current substring.

2. For every nucleotide in the sequence, we check whether it is present in the hash map or not.

	* If it is not present, we store it in the hash map with the value as the current index.

	* If it is already present in the hash map, then this means that the nucleotide can repeat in the current substring. For this, we check if the previous occurrence of the nucleotide is before or after the starting index, stCurr, of the current substring.

	If it is before stCurr, then we update the value in the hash map. If it is after stCurr, we find the current substring’s length as currLen and compare it to that of the longest substring. If the longest is less than the currLen, we update the longest as currLen and start as stCurr. To prevent the repetition of the current nucleotide, the next substring will start from the last occurrence of the current nucleotide.

3. After traversing the entire sequence of nucleotides, we find that the species marker is from nucleotide[start] to nucleotide[start+longest].





