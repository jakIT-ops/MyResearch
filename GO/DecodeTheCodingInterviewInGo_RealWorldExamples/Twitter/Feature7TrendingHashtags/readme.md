## Description

We are given a list, tweetsInfo, which is a daily log of hashtags used by some people in their tweets. The log is structured as follows:

* the day on which the tweet was posted,

* all the people who posted on that day, and

* the hashtag they used in their tweet on that day.

Our task is to group and return all the people who used the same set of hashtags in one of their tweets, along with the day on which they tweeted with those hashtags. The output list will consist of day/person strings for all hashtags that have at least two mentions in the input. We can return the answer in any order.

A single day information string in the input list has the following format:

* "day_m p1(p1_hashtag) p2(p2_hashtag) ... pn(pn_hashtag)"

It means that on the day day_m, there are n people (p1,p2,...,pn) with hashtag they used in their tweet (p1_hashtag,p2_hashtag,...,pn_hashtag) respectively. Note that n >= 1 and m >= 0. If m = 0 it means the day is Monday, m = 1 it means the day is Tuesday and so on.

The output is a list of strings. Each string should be of the form day_1/p1 day_2/p2 if p1 and p2 tweeted with the same hashtag on day1 and day2, respectively. In the rest of the lesson, we’ll refer to the day, followed by a forward slash, followed by a person’s name, as the hashtag path, as shown below:

* day/person_name

## Solution

To get started with the solution, we first need to obtain the days, people names, and hashtags separately by appropriately splitting each string in the given tweetsInfo list. To find the people who used the same hashtag in their tweets, we will use a Hashmap called map. It will store the hashtag as the key and a list of hashtag paths as its value: (hashtag, list_of_hashtag_paths).

For every hashtag, we will check if it already exists in the map. If it does, we will add the current hashtag path to the list of hashtag paths corresponding to the current hashtag. Otherwise, we will create a new entry in the map, with the current hashtag as the key and the value being a list with only one entry, the current hashtag path.

Finally, we find out the hashtags corresponding to which at least two hashtag paths exist. We obtain the output list output, which is a list of lists containing these hashtag paths corresponding to the same hashtags.




