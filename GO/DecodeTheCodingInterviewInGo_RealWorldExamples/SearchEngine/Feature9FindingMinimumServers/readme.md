## Description

For this search engine feature, we want to find the optimal server configuration to handle a given workload demand. Workload demand represents the user query traffic coming into our search engine. Greater incoming traffic requires a greater number of servers. We have defined a way to measure workload (user traffic). Our server deployment consists of n different types of servers. Each type of server is capable of handling a different amount of workload with workload handling capacities [c0…cn-1]. We want to determine the optimal set of servers to handle a specific workload. This set of servers must have a capacity at least equal to the workload. We would incur a fixed one-time cost of commissioning a server. We have such a large deployment of servers that you may assume an unlimited supply of all types of servers.

Deploying each of the server incurs a fixed one time cost. As the numbers of servers increase, the total cost of deployment does too. We want to find an optimal way to meet the total workload demand by deploying the minimum amount of these servers.










