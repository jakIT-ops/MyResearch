## Description

A legacy ad service at the Amazon backend creates a list of ads that match a user’s profile and preferences. We have an ad-serving API, read4(), which a client can call to retrieve the next 4 ads in the list.

The legacy API was developed when users were still working on PCs with monitors that had relatively smaller screen sizes and lower resolutions. Showing any more or fewer than four ads wasn’t practical. However, now, many of our users are visiting websites through mobile devices with very small screens or PCs with much larger displays. As a result, sometimes, we also need to serve more than or fewer than four ads at a time.

The client determines the number of ads that can be displayed on a certain client’s screen. This may be more or less than four. Without modifying the backend, we want to implement a read(n) function that will return the next N ads (or fewer, if we reach the end of the ads list).


## Solution

Let’s look at the steps that we can follow to solve this problem:

* Create a struct to maintain the variable’s state in a closure. We will use struct to store:

	* buff, which will be passed to the read4 function and used to store 4 characters at a time.

	* ptr, which will be used to iterate through buff.

	* count, which will be used to keep track of what the read4 function returned—that is, how many characters the read4 function read.

* Start a loop to read a file.

	* If the buff iterator ptr is 0, we will read the File using the read4 function and save the returned value.

	* If the read4 function didn’t read any character and returns 0, we will break the loop.

	* Otherwise, we will fill the buffer array with the buff array, using the other counts’ variables.

	* At the end, we will return i, which will represent the number of characters that the buffer array contains.












