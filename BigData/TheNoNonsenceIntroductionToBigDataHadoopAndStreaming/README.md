# What is Big Data, And Why is it Popular?

### Overview

Big data refers to data that typically cannot be handled and analyzed using traditional techniques. If you need to make a quick decision based on a big data dataset, the computation time of days might be a business killer.

As the name implies, big data is a large dataset that cannot be effectively processed by traditional processing techniques. One such traditional technique is to perform SQL queries on our relational database that contains this dataset.

Although the idea of big data has existed for a long time, technological advancements now make it possible to deal with it effectively in terms of storing, processing, and speed.

### How big is “big data?"

Most people associate big data with a certain threshold of terabytes, petabytes, or exabytes. While this might make sense, there is no official definition of big data in terms of size.

As a simple rule though, big data refers to datasets that are not manageable in a traditional way, with single computing and storage. You can think of big data as any quantity of data greater than 5TB.

Again, this is very simplistic but will act as our working definition for this course.

### Measuring with V-indices

Big data can be divided into four dimensions: volume, variety, velocity, and veracity.

* Volume: The main characteristic that defines big data is its sheer volume. Many people question how many terabytes, exabytes, or petabytes of data we need before it is considered big data. However, it does not make sense to focus on minimum storage units, as the total amount of available data grows exponentially every year.

* Velocity: How fast is the data generated? Is the dataset stale like “all the geographical points on earth that received heavy snowfall since last week”, or updated multiple times every second like “what people are currently watching on Netflix, Youtube, and Amazon Prime?”

* Variety: How different is the dataset? Do we keep just text logs, just images, or just sound files? Or does the set include a combination of multiple types of data?

* Veracity: What is the quality of the data? Does it have noise and inconsistency? For example, do we describe the location of a user in a standard format? Or do some users describe it with string, whereas others with latitude/longitude coordinates? How many users have left the date of birth empty?

### The big data trend

The term big data has gained popularity in the past few years, mainly for the following reasons:

* Ubiquitous computing: Even a smart refrigerator can give information about someone, such as our habits or health issues. For instance, if 98% of foods in your refrigerator have a low glycemic index, the refrigerator might estimate that you have some diabetic disease.

* Smartphones: Did you know that your smartphone contains quite a few sensors that are utilized by the underlying operating system? Every time your smartphone moves around (for instance, when we commute, talk or walk), the operating system records these movements, which can be analyzed later.

If we apply this to the various applications that track our usage, multiplied by a few billion smartphones globally, we’ll see that we can generate data about ourselves through our devices multiple times per second.

* Free services: Companies that offer high-quality products free of charge usually want to utilize our data and make money from it, typically through targeted advertising.
In this way, Facebook and Google make a lot of their money acting as advertising companies.

Similarly, Amazon uses our activity trail to offer us relevant products and increase the possibility of us buying the recommended product.

Don’t take this the wrong way; we’re not saying this is a good or bad thing. It is up to the user to decide what they are comfortable with sharing this data.

Looking at how Facebook, Google, and Amazon use big data can help us understand why the amount and value of data have become bigger and bigger in the past few years. You can think of value as another V-index.

### The Growth of big data

The data size is increasing exponentially once every 2-3 years. At the time of writing this, roughly 90% of the world’s data was produced in the [past few years](https://techjury.net/blog/big-data-statistics/).

Due to faster and better network bandwidth, transmitting vast amounts of data is now trivial. The drop in cost to procure disk storage and memory, along with the increased size of these storage mediums has provided new opportunities.

### How is the data generated?

Usually, our machine will handle data generation. If you listen to a song in a music service, this event will be recorded from the client (browser or app), and at some point will be sent to a place, called a data lake. We will explain this in more detail later. This is also referred to as ingestion and persistence.

The service can create recommendations for you through a series of similar events, such as what songs you liked. This will happen after analyzing the data and comparing them to other users’ data.

This transfer from data generation to useful recommendation is not an instant process. It can take from a few seconds to a couple of hours. However, the faster we do it, the better it is for business.

# The Hadoop Ecosystem

## A Pragmatic Introduction to Hadoop and MapReduce

### Distributed file systems

Traditional techniques might not suffice to extract meaningful information from big data datasets.

Google realized this problem and a potentially robust solution at an early stage.

### MapReduce

MapReduce is a concatenation of map, and reduce functionalities, which aptly describes its behaviour. It is an implementation of the computing model introduced by Google to process large datasets. Here, data-parallel computations are executed on clusters of unreliable machines by certain systems.

In simpler terms, think of MapReduce as similar to a divide and conquer strategy. A massive data set is divided among worker machines. Once processing is complete, the data from each machine is aggregated to present a final solution.

### Characteristics

MapReduce programming model has the following characteristics:

* Distributed: MapReduce is a distributed framework consisting of clusters of commodity hardware that run map or reduce tasks.

* Parallel: The map and reduce tasks always work in parallel.

* Fault-tolerant: If any task fails, it is rescheduled on a different node.

* Scalable: It can scale arbitrarily. As the problem becomes more extensive, we can add machines to solve the problem in a reasonable amount of time. The framework can scale horizontally rather than vertically.

### Example

We will now demonstrate this concept using a real-world example rather than a technical one.

Imagine yourself and 10 friends on a tennis court where thousands of tennis balls are spread around.

If you want to count all of the balls of different colors on the court, you need to split the responsibilities within the team:

* Some of you will act like mappers and some as reducers.

* You will divide the court into areas of search for each one of you. This is how you partition the field.

* The mappers will note down statements, such as “I just saw a green ball", "I just saw a pink ball” and so on. Based on the mappers’ reports, the reducers will count - - how many different colored balls you found.

* In the end, you will combine all the answers from all the reducers and get the numbers you want.

### Hadoop

Yahoo created Hadoop by implementing the aforementioned Google papers. The imitating file system was named Hadoop Distributed File System (HDFS), instead of Google File System.

After all these years, Hadoop has evolved into a big ecosystem with many applications. These are mostly Apache projects that were built on top of it. Hadoop is now a framework that is used to both store and process big data datasets.

It does so with a distributed file system that mimics GFS and with MapReduce algorithms.

## Deep Dive into Hadoop and MapReduce

### Hadoop architecture

* Master Node: Also called NameNode, the Master Node manages HDFS metadata, which includes mapping files to the list of blocks they contain.

Master Node has a single point of failure, which is a big downside. Besides this, the NameNode controls the read/write accesses to the files from clients, keeps track of the nodes in the cluster, the disk space of nodes, and whether or not a node is dead. It then uses this information to schedule block replications.

* Data Servers: Also known as chunk servers, they are responsible for writing data to files when a client requests the Master Node. Depending on the replica number of the file, a write pipeline would be set up between that many data nodes. A write process would be considered successful when all replicas are successfully written, which ensures data consistency. Data nodes also send periodic block reports to the Master Node, which uses them to map blocks of a file to its locations.

* Client: It talks to the Master Node and fetches the files from the data servers to run map and reduce on them. The Master Node responds with multiple locations, from which the client can read data blocks from. The client chooses the nearest data node if there is more than one to avoid burdening the network.


### Hadoop architectural traits

Some key architecture traits offered by Hadoop are:

* Scalability: Hadoop is scalable. As long as we can add machines on demand, our cluster will keep adjusting its performance.

* Fault tolerance: Hadoop can recover somewhat gracefully if a node fails. Node failure is likely to occur at least daily in a cluster of a thousand machines.

* Speed: Even though there are technologies that have been proven faster, like Apache Spark, Hadoop is relatively fast and can process terabytes of data, in minutes, given reasonable cluster size.

The Hadoop ecosystem is great for some instances, like analytics on a large dataset. As with all technology pieces, moderation and sound judgment are required when it comes to using them.

Hadoop is not applicable in every situation, and it is not wise to use it with all the data jobs that might come up.

To achieve something complex in life, we usually need to have various actors, components, and processes to work together. That is the case with Hadoop, where individual components achieve the end goal by having close collaboration.

### Resource negotiation and scheduling

In distributed systems, we have a principle called resource negotiation. This is where we want to decide things like where, and with what portion of hardware, the process will run.

In a simple example, which machine is available to run a process requiring 16GB of RAM?

This is also an example of scheduling. When the resources are approved, the process is scheduled rather than run immediately. It usually takes negligible time for human standards, but it is important to note that it is not happening simultaneously.

### YARN

Yet Another Resource Negotiator (YARN) can be thought of as similar to an operating system for a cluster. The cluster represents the collection of resources, such as compute, memory, disk space, and network bandwidth, that YARN arbitrates among jobs that run on the cluster. Similar to how an operating system presides over the machine’s resources and distributes them among competing processes, YARN allocates cluster resources among competing jobs.

YARN majorly have the following responsibilities:

* It allocates the resources to the jobs that wait to run on HDFS. That is answering questions like “Which job will run first?” or “How much memory should be assigned to the job X”.

* It schedules and monitors jobs.

* It allows other processing frameworks than MapReduce,like Spark, to run on HDFS.

### When to avoid Hadoop

* When we have a small dataset, which will lead to performance degradation as there is an overhead to boot up the workers and with the block size it employs you might underutilize it.

* When we edit the files a lot. Hadoop is very good when it comes to fast reads and appends.

* When we’re looking for a replacement for SQL or even Pandas. The query capabilities of Hadoop are fairly limited, even though tools like Presto, which work on top of Hadoop have reduced the gap.

* sIf the data can fit in one computer, bash scripts could be faster (in dev time and execution time as well). Give it a try before employing a Hadoop cluster.

# Introduction to Streaming

### Overview

Streaming data is generated and delivered continuously, in a never-ending manner, and at a variable rate. It can be of two types: inbound or outbound.

The inbound streaming data could arrive so fast and be so massive in volume that it is futile, unworthy, or infeasible to store them. It is almost impossible to regulate structure, data integrity, or control the volume and velocity of the data generated.

That means our application needs to extract knowledge from the data as soon as it arrives. In other words, speed matters the most in big data streaming, because the value of data decreases with time if not processed quickly.

### Stream processing

Stream processing is a technique used to process and analyze data in motion.

As the stream of data is potentially infinite and of any size, we cannot be sure whether it will fit the amount of memory we have. To address this issue, we use a sliding window of time technique. We always look at the data that arrived in the last N seconds or so.

Of course, we need to take precautions to ensure we do a first level of processing quickly. Usability suffers if our initial processing is slow enough that it misses 80% of the data in a sliding window. If we fail to meet this, we need to make sure we can catch up using caching techniques.

### Streaming vs. batch processing

Some people confuse streaming with batch processing. They’re both meant to get knowledge out of a significant amount of data as soon as possible.

Batch data processing methods require data to be downloaded as batches before processing, storing, or analyzing it. In contrast, streaming data flows in continuously and allows that data to be processed simultaneously, in real-time, the second it’s generated.

If you need to know the weekly sales of your organization, there is no point in running batch processing every hour or applying stream processing. Batch processing requests can be scheduled once a week, preferably on Sunday, to get results by Monday morning.

### Is it really real-time?

Real-time systems can be further divided into hard real-time and soft real-time systems.

* Hard real-time systems: These are systems that have to comply with specific time response directives. If they fail to do so, the consequences might be huge. For example, these systems are often used in medical technology, like a cardiac pacemaker, or defense systems, like an anti-missile protection system.

* Soft real-time systems: These are systems that have to react immediately to a trigger, but without restricting it to specific time windows.

This does not mean there are no SLAs, though. Violating them won’t put anyone’s life in danger, but they will likely be classified as UX or performance degradation.

SLAs can still operate as usual if they fail the deadline, meaning the only problem would be in performance degradation.

### Examples of streaming data

* Device monitoring: All the devices of an edge cloud send a heartbeat signal every few milliseconds. A receiver processes the stream and raises alerts if the heartbeats decrease in number for the last minute.

* Fraud detection: All payments that happen online, every second, are analyzed immediately against fraud checks. These systems raise alerts for any suspicious payment.

* Stock prices monitoring: A customer has put a sell order to sell a stock when it reaches a specific price. A stream analyzer watches the stream of the price fluctuations to act when the price is matched.

* Trending articles: We have a news site and a bot that tweets all articles that have the “trending flag” on them in the database. We have an algorithm applied in the stream of views, and we flag them as trending when the rate of viewers surpasses a certain threshold.

## Real-Time Streaming Platforms

### Apache Kafka

Apache Kafka is one of the most famous streaming platforms. It was created by LinkedIn initially and, after a few years, was donated to the Apache Foundation.

Kafka is a distributed streaming platform. We can use it as a real-time messaging system with a high fault tolerance capability. In other words, it means that our messages will be delivered fast, and if it fails, we can figure it out quickly. A message can be anything from a string, to a serialized object, to a blob.

Kafka is also very famous for its scalability powers. Despite its numerous capabilities, Kafka is widely used to connect heterogeneous applications in a many-to-many manner.

For example, when the system receives a new stock price, it shows in the UI, updates the database with the new value, and stores the event of a change to HDFS or any data lake we use. We can do this by having multiple consumers, also referred to as connectors, read the message and act upon it.

Kafka has various subcomponents, like Kafka Streams and KafkaSQL, each of which has its own specialization.

### Apache Flume

Flume is a distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of data. Usually, this data refers to log files. For example, imagine running a web app using multiple servers, and we want to get the logs in one place. This would be a perfect use case for Apache Flume.

It has a simple and flexible architecture based on streaming data flows. Flume is robust and fault-tolerant, with tunable reliability mechanisms, and many failovers and recovery mechanisms.

### Spark Streaming

It is part of the core Spark API and fulfills the philosophy of being the “one and only tool for your big data processing.” Spark streaming provides streaming capabilities in a high-throughput, fault-tolerant way.

It accepts input from many different source types like Kafka or HDFS and pushes the data to a persistence layer in a streaming way.

### Apache Storm

Apache Storm was initially created on Twitter to perform real-time message processing and might look similar to Kafka. However, unlike Kafka, it focuses on computation rather than on delivery.

Kafka is mostly a queue, whereas Storm can do multiple types of computations over data.

### Alternatives

These tools have a steep learning curve. Therefore, they’re not the best fit for a one-off gig or small projects.

Here are some tools that require less reading and can achieve results of a similar nature:

* The PUB-SUB functionality of the Redis database.

* RabbitMQ.

* WebSockets, to trigger some processing as a result of a new data event.


# Apache Spark

### Apache Spark

Apache Spark is a computation engine and a stack of tools for big data. It has capabilities around streaming, querying your dataset, Machine Learning (Spark MLlib), and graph processing (GraphX).

Spark is developed in Scala but has bindings for Python, Java, SQL, and R, too.

Spark relies entirely on in-memory processing, which makes it manifold times faster than the performance of respective Hadoop functionalities.

### MapReduce and Spark comparison

With the advent of Spark, the MapReduce framework took a backseat due to several reasons mentioned below:

* Iterative jobs: Certain Machine Learning algorithms make multiple passes on a dataset to compute results. Each pass can be expressed as a distinct MapReduce job. However, each job reads its input data from the disk and then dumps its output to the disk for the next job to read. When disk I/O is involved, the job execution time increases manifold when compared to the same data accessed from the main memory.

* Interactive analysis: Users can run ad-hoc SQL queries on large datasets using tools such as Hive or Pig. If the user issues multiple queries targeting the same dataset, each query may translate to a MapReduce job, read the same dataset from disk, and operate on it. Having multiple MapReduce jobs read the same dataset from the disk is inefficient, and increases query execution latency.

* Rich APIs: Spark, by offering a variety of rich APIs, can succinctly express an operation that would otherwise consist of many lines of code when expressed in MapReduce. The user and developer experience is relatively simpler when working with Spark, as compared to MapReduce.

## Popularity of Spark

### MLlib vs. Tensorflow/Pytorch

There are numerous super-popular and well-documented frameworks around Machine Learning, like Tensorflow and Pytorch. So use MLlib arise?

A big reason to use any tool from the Spark ecosystem is its distributed nature. In addition to performing in-memory computation, Spark can do it over a distributed file system.

This helps with scaling the process, and you don’t have to learn a second technology that might not be compatible with Spark.

Remember the tennis balls examples from an earlier lesson? We could write a model that predicts which color the next ball would be. Since we already have the data in HDFS, we could utilize the Spark integration with HDFS and run our Machine Learning model there.

### Spark and Hadoop MapReduce

Hadoop was a breakthrough in big data processing when it came out. Though it is still a popular tool, Spark outperforms it in many areas, such as performance and real-time needs.

Spark runs on memory, and this alone can be a game-changer.

### Applications of Spark

* Trend calculations.

* Personalized user experience.

* Business intelligence (BI).

* Summarizing a corpus using graph algorithms like TextRank with GraphX.

* Real-time detection of fraudulent payments using Spark Streaming and MLlib.

* Implement an ETL pipeline with Spark Streaming.
