## Description

Zoom is the leader in enabling smart enterprise video conferences. The offer of support it presents for a wide range of devices and operating systems is one of the main reasons for its popularity. Many users join meetings using mobile handheld devices, which can be rotated. We want to implement a rotate functionality on the profile pictures shown against each user in a meeting. We will start with the functionality to rotate 90 degrees clockwise. We will rotate the coordinates of the profile pictures. This feature will show us how to rotate the profile pictures in a meeting.

## Solution

We have to rotate the pixels of the profile pictures when the user switches the mobile screen from landscape mode to portrait mode or vice versa.

Let’s see the following implementation of the feature:

1. We will start with the values comprising the two outermost rows and the two outermost columns of the n x n matrix.

2. We will rotate the values clockwise, in the cells mentioned above, and iterate over the next cells of each rotated cell and rotate them.

3. We will repeat the step given above on the inner (n-1) x (n-1) matrix, using the same procedure.


