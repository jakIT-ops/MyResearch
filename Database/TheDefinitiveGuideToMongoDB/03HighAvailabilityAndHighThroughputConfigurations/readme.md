# 1. Replica Sets

### Introduction to Replica Sets

What is replication?

One of the reasons NoSQL databases evolved in the first place was the need for a different way of storing data in distributed systems-- one server was not good enough anymore.

Now, we have multiple servers with multiple NoSQL databases running on them. This process of synchronizing data across multiple servers in the whole system is called replication.

### Why Use Replication

The goal of replication is for all of the servers to have the same data so that the users who access different servers have the same information. This process ensures data durability and makes sure that no data is lost if one server fails, or if the network experiences problems for a certain amount of time.

### Replication in MongoDB

In MongoDB, replication is implemented using replica sets. Replica sets are instances of MongoDB processes (mongod) that host the same data set. Each of these processes is considered as one node and that node can be a data-bearing node or an arbiter node.

Data bearing nodes, as the name implies, are nodes that host data. So a replica set is basically created from two or more of those nodes. Based on operations that are done on them, nodes can be either primary or secondary.

An arbiter node, on the other hand, does not maintain a data set nor can it be a primary node. The main purpose of an arbiter node is to add an odd number of votes in elections held to choose a primary node, and to respond to heartbeat requests by other members.

<br>
<div align="center">
	<img src="../img/Screenshot from 2022-07-25 14-16-29.png">
</div>
<br>

### Primary Node

There can only be one primary node in a replica set, and that is the node on which all write operations are done. When a write operation is done on the primary, it records information about this operation in the operation log (oplog).

### Secondary Nodes

Write operations never go to secondary nodes. Instead, they replicate the primary’s oplog and then apply the recorded operations to their data set. This way, the secondary data set mirrors the primary one.

MongoDB client can be configured in a way that reads data from the secondary nodes.

### Detecting a Failing Node

In general, these nodes maintain the heartbeat between them, as a mechanism for detecting a failing node. This way, when one of the nodes fails; other nodes are aware of that.

# 2. Implementing Replica Sets

### Connecting Nodes

The next thing we want to do is put all these nodes together in one replica set.

In order to do this, we need to attach to one of the running `mongod` processes using the MongoDB shell client.

So, I called `mongo` to connect to the `mongod` process that is running on port `27017`.

```nodejs
mongo
```

### Using `rs.initiate()`

```nodejs
rs.initiate()
```

```
rs.initiate({_id : "rs0",members: [{_id : 0, host : "localhost:27017"}]})
```

As you can see, I used this JSON document for configuration:

```nodejs
{
  _id : "rs0",
  members: [
    {_id : 0, host : "localhost:27017"}
  ]
}
```

In members, I just added just the node that is running on port 27017. To add other nodes, you can simply extend this JSON to look like this:

```nodejs
{
    _id : "rs0",
    members: [
        { _id : 0, host : "localhost:27017" },
        { _id : 1, host : "localhost:27018" },
        { _id : 2, host : "localhost:27019" }
    ]
}
```

### Using `rs.add()`


The other way this can be achieved is by calling the

```nodejs
rs.add()
```

method, like so:

```nodejs
rs.add("localhost:27018")
rs.add("localhost:27019")
```

### Using `db.isMaster()`

Another useful function is:

```nodejs
db.isMaster()
```

```nodejs
db.isMaster()
```

# 3. Sharding

## Limitations of Replica Sets

We learned that replica sets gave us the ability to hold data in multiple databases and thus, give us a certain level of fault tolerance and data duration.

However, this approach has certain limitations. As previously mentioned, all write operations go to the primary node, which makes it the bottleneck of the system. This means that if the system grows, the primary node will be overused and, eventually, it will be limited with hardware limitations like RAM, the number of CPUs, and disk space.















































