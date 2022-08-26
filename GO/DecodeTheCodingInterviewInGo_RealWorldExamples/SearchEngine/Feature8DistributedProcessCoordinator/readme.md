## Description

For this search engine feature, we will implement a distributed process coordinator. In distributed computing, a coordinator is the organizer of a task that is distributed among nodes. Our distributed process coordinator is responsible for breaking a task into multiple subtasks, assigning tasks among different worker nodes, and monitoring their progress. We want to implement fault tolerance, so that if one or more worker node(s) fail, our search engine can continue working without interruption. To implement fault tolerance, we will implement a snapshot functionality to save the current progress of worker nodes.

We have n worker nodes. Each node will have a state, which will be the number of subtasks that the node has successfully executed. In the beginning, the state of each node should be 0. We can change the progress state for each node by using the SetState(idx, state) function. This function will take two parameters. idx is the index of the node whose progress we are setting, whereas state is the new state of that node. We should also be able to take a snapshot of the nodes at any time. This means that we should be able to save the current state of the nodes at any given time. To implement this, we need to create a Snap() function. This function will not take any parameters and will return the snapshotId. The snapshotId counts the number of times that the snaps were taken.

## Solution

To solve this problem, we will start by creating a dictionary named nodeState. The nodeState will hold all the states, along with the nodes, at different times in further sub-dictionaries. The keys to the nodeState dictionary are the snapshot IDs. For a given key, the values are also dictionaries. These inner dictionaries have node IDs as keys, and the node’s state as values.

As an optimization, we will not initialize all the nodes. Instead, we will initialize a node when we set its value for the first time. We will use the SetState(idx, state) function to set the current progress of the specified node to state. After taking a snapshot, we will increment the snapshotId. Then, we will copy the recent progress of the nodes, and create a new dictionary, which will be used to store the latest progress of the nodes. We will, then, return the id of this Snapshot. To access the state of a particular node at the specified time, we will search for the snapshotId in the nodeState. If the snapshotId is less than the number of snapshots taken so far, we will check the state of the node. If the state of the said node has been set, we will return it. Otherwise, we will return 0. If the snapshotId is greater than the number of snapshots taken, we will return None.













