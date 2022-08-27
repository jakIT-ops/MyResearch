# Components of a HPC cluster

A cluster is two or more (often many more) computers working as a single logical system to provide services. Though from the outside the cluster may look like a single system, the internal workings to make this happen can be quite complex.

The figure above presents the logical functions that a physical node in a cluster can provide. Remember, these are logical functions; in some cases, multiple logical functions may reside on the same physical node, and in other cases, a logical function may be spread across multiple physical nodes.

Aside from the cluster nodes (management node, compute nodes, and storage nodes) that make up a cluster, there are several other key components that must also be considered. The following sub-sections discuss some of these components.

* Ethernet switches Ethernet switches are included to provide the necessary node-to-node (1/10 GB) communication.

```py
+ Infiniband switch: For faster networks (56/100 GB), mainly used by MPI enabled software.
```

# Login node(s)

Individual nodes of a cluster are often on a private network that cannot be accessed directly from the outside or corporate network. Even if they are accessible, most cluster nodes would not necessarily be configured to provide an optimal user interface. The Login node is the one type of node that is configured to provide that interface for users (possibly on outside networks) who may gain access to the cluster to request that a job be run, or to access the results of a previously run job.

# Compute node(s)

A compute node is where the real computing is performed. The majority of the nodes in a cluster are typically compute nodes. In order to provide an overall solution, a compute node can execute one or more tasks, based on the scheduling system.

# Master node(s)

Clusters are complex environments, and the management of the individual components is very important. The management node (generally named as the: `master` or `head` node) provides many important capabilities, including:

* Monitoring the status of individual nodes (typically compute nodes).

* Issuing management commands to individual nodes to correct problems or to provide commands to perform management functions, such as power on/off.

* In most clusters, the compute nodes (and other nodes) may need to be reconfigured and/or reinstalled (provisioned) with a new OS image relatively often. The master node provides the images and the mechanism for easily and quickly installing or reinstalling software on the cluster nodes.

* The master node can also provide networking services that help the other nodes in the cluster work together to obtain the desired result. Control nodes can provide two sets of functions: Dynamic Host Configuration Protocol (DHCP), Domain Name System (DNS), and other similar functions for the cluster. These functions enable the nodes to easily be added to the cluster and to ensure they can communicate with the other nodes.

* Scheduling tasks (to be discussed in detail soon!) can be another important role for a master node. For instance, if a compute node finishes one task and is available to do additional work, the control node may assign that node the next task requiring work. However, sysadmins may decide to allocate a separate node (Scheduler node) for this purpse to reduce loads on the master node.

To create high availability (HA) , the master node can have a backup master node. Also, in some systems, master node’s tasks may be distributed over various nodes such as Job-scheduler node, log-server nodes, monitoring node, etc.

# Storage node(s)

Compute nodes must have fast, reliable, and simultaneous access to the storage system. This can be accomplished in a variety of ways depending on the specific requirements of the application. Storage devices may be directly attached to the nodes or connected only to a centralized node (storage node) that is responsible for hosting the storage requests through Networked file system (NFS) mounts.

The use of a clustered file system is essential in modern computer clusters.Examples include the IBM’s General Parallel File System (GPFS), Microsoft’s Cluster Shared Volumes or the Oracle Cluster File System. The storage node in turn can be connnected to tape libararies for further backups.
