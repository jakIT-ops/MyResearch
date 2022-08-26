## Description

This feature will allow us to watch or re-watch stories on Instagram that are uploaded through Facebook. Every story uploaded by a user on Facebook gets assigned a unique incrementing id. On Instagram, a user can only watch one story at a time. These stories will be accessed from Facebook in ascending id order. When a story is watched, the story array rotates to accommodate unwatched stories at the start and watched stories at the end. Since stories are fetched from Facebook, so whenever a user wants to rewatch a story on Instagram, our system has to search for its id in the Facebook story list.

## Solution

The solution is essentially a binary search with some modifications. If we look at the array in the example closely, we notice that at least one half of the array is always sorted. We can use this property to our advantage. If the number n lies within the sorted half of the array, our problem is a basic binary search. Otherwise, we’ll discard the sorted half and keep examining the unsorted half.




