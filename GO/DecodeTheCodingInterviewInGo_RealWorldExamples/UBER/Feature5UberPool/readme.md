## Description

Uber pool allows a passenger to share the car with other passengers on their journey. In return, each passenger pays less than what they would pay for their own car. However, passengers in a pooled ride are not predetermined. As a pool customer is taking a ride, more pool ride requests may arrive. The driver will have the option to pick up those new passengers to pool the ride. It is quite possible that a customer gets the entire ride to themselves because no one else along their ride’s route requested an Uber pool.

Let’s say a driver has picked up a pool customer and is at a checkpoint. There are multiple routes to the passenger’s destination, and the likelihood of finding another pool customer on each route may be different. Based on these likelihoods, we have assigned metrics to each route to the destination. We don’t want to always suggest the route with the highest probability because it might not necessarily be the best option. Instead, we want to suggest a route randomly picked from the available routes to the destination in proportion to the metric assigned to the route. That way, high probability routes are more likely to be selected, but other routes will also be selected.

We’ll be provided with a list where the index represents a route that the driver can take for finding another pool customer. The values in the list represent the likelihood metrics assigned to each route. We want the route with a higher likelihood to get higher weightage during selection.

## Solution

We can represent the probabilities using a line. The line length can correspond to the likelihood metric of each route. The metric values have been added for each point to represent all of the probabilities on the same line.

On a number line, make marks at arr[0], arr[0] + arr[1], arr[0] + arr[1] + arr[2], ...., arr[0] + arr[1] + … arr[n-1]. This results in n line segments each corresponding to one of the entries in the array. Let the last mark be at a value k. Now, if we draw a random value between 0 and k, it will lie on one of these line segments. If the random value lies on the ith line segment, we’ll say that the ith array value has been picked. The likelihood of a random value between 0 and k falling on a specific line segment depends on the length of the line segment, which equals the value of the corresponding array element. This means that we have picked an array element using probability determined by its value.










