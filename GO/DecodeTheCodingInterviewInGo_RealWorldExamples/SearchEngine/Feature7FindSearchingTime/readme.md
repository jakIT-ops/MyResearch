## Description

A typical search engine consists of many services, such as crawling, indexing, word stemming, synonym fetching, etc. When a user’s search query arrives at a web front end, it is dispatched to the above-mentioned search-related services. A single search query turns into a large number of calls to these services. Some of these calls are recursive, too. For instance, the stemming service may stem one or more words from the search query before invoking itself recursively on the rest of the search string.

Optimization is an ongoing effort and search engines keep trying to reduce the time it takes for the search results to be displayed on the user’s screen. To better guide this optimization activity, we instrumented code to achieve some statistics. Using these statistics, we want to figure out the time spent in each of the search-related services over a specific time window.

To find the time spent by each service, we will use log messages. Each service is identified in the logs by a serviceId, and the logs contain the start and end timestamps of each invocation of the service. The logs will be stored in a list of strings, where each string will have the following format: "{serviceId}:{"start" | "end"}:{timestamp}".

## Solution

Once we encounter a particular function’s start message, we will calculate the time spent in all the subsequent nested calls until we encounter the end message for the first function. This can be done using the stack data structure. We can also subtract the difference of the end time and the nested function execution time from the start time to determine the running time of the first function.

Here is how the implementation will take place:

0. Initialize the servTimes list with 0’s.

1. Start traversing over the list of strings. Retrieve the ID of the first service, push it on the stack, and store its time in the time variable.

2. If the next service in line has a start state, add its time to servTimes[i] and subtract the time variable.

3. If the service next in line has an end state, add its time to servTimes[i], subtract the time variable, and add 1 because the service will run until the end of its specified time.

4. Repeat steps 2 and 3 until all the services in the list have been executed.

5. Return the sum of the servTimes list.









