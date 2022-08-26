## Description

Every DNA strand contains multiple chromosomes of different types. The type of genes in these chromosomes varies in different DNA samples. We can mutate a single DNA sample of one species into another by replacing the genes in the chromosomes. However, we can only replace the genes from a list of available samples. For simplicity, let’s say that the genes in chromosomes are represented by lowercase English letters, a, b, c,..., etc. The available samples will be the twenty-six letter lexicon for alphabets. In a single replacement, we can replace all occurrences of the same type of genes with any other available sample from our list. Furthermore, gene replacement must be done one by one. For example, garlano could be converted to gorlono if a is replaced with o. Then, if o is replaced with t, it becomes gtrltnt.

We’ll be provided with two chromosome samples from different DNAs in the form of strings. The genes in these chromosome samples can be of the same or different types. Our task will be to determine whether one sample can be mutated to the other under the provided constraints.

## Solution

The above examples demonstrate that to convert one sample to another, both samples have to contain the same number of genes. Each character of string1 needs to be converted to a corresponding character in string2. We can map each element in string1 to what it needs to be in string2. We can model this as a graph problem by representing the mapping relationship as the edges of a graph. The graph for the above mutable example can be represented as follows:

The condition that all occurrences of the same gene need to be replaced in one iteration. This infers that a single gene in string1 can only be mapped to a single gene in string2. This means a single node of the graph can have only one outer edge. Otherwise, the mutation will not be possible. The graph for the above mutable example can be represented as follows:

For example, we have two strings: str1 = "abc" and str2 = "bcd". To transform str1 into str2, we get the following chain of conversions:

transform chain = a -> b -> c -> d

If we start our conversions from the beginning of the chain, we will get stuck on our second iteration because we would get two mappings of b. If we start from the end, following c -> d, b -> c, and finally a -> b, our transformation will be possible. There is also a possibility of cycles in our graph. For example, let’s say we have two strings str1 = "ac" and str2 = "ca". We get the following chain of conversions if we want to transform str1 into str2:

transform chain = a -> c -> a

We can see that in this cyclic graph, we’ll get two mappings of a in the second iteration, which is not acceptable. Here, we can break the cycle by introducing a substitute value. This substitute value will come from the list of the available samples, which in our case is the twenty-six letter English lexicon. So, instead of c -> a, we can do c -> y and y -> a to get the following:

transform chain = c -> y, a -> c, y -> a

We can tolerate cycles as long as there are characters available in our lexicon to use as substitutes. Therefore, a mutation is only possible if and only if:

* Each character edge forms a linear graph with every node having one out-degree

* There should be characters available in the sample(lexicon) to use as substitutes if a cycle occurs.



