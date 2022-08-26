## Description

The Facebook Status API queues requests using the requested Status ID and a timestamp. We want to implement a throttling mechanism on the requests that limits one request for a particular Status ID at a pre-configured time interval. Any additional requests for the same Status ID in this interval will be dropped. Multiple requests for different Status IDs can occur at the same time.

We’ll be provided with the name of the request and the time it arrived. Our system will have to decide whether to accept the request or reject it based on its arrival time. In this scenario, we’ll use a time limit of five days before a similar request can be sent from the same or different platform.

## Solution

The hashtable data structure will be used to implement this feature. This data structure can uniquely store all of the incoming requests while simultaneously taking care of the duplicate requests. The requests will be stored as keys and the request’s timestamp will be stored as corresponding values in the hashtable.

Here is how we will implement this feature:

1. Initialize the hashtable.

2. When a request arrives, check if it’s a new request or a repeated request that came after the assigned time limit.

3. If either of the above conditions is satisfied, accept the request and update the entry associated with that request in the hashtable.

4. If not, reject the request.
