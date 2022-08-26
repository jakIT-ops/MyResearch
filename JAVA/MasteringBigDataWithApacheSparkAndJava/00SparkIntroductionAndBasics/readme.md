# 1. Spark Fundamentals 

## Why choose Spark?

As the demand to process data and generate information continues to grow, engineers and data scientists are increasingly searching for easy and flexible tools to carry out parallel data analysis. This becomes even more apparent with the dawn of cloud computing, where processing power and horizontal scaling are more available.

Spark comes into this picture as one such tool due to the following principal reasons:

Ease of use: Spark is straightforward to use in comparison to other existing tools that pre-date it, such as Hadoop with MapReduce engine. It enables developers to focus on the logic of computation while they code on high-level APIs. It can also be installed and used on a simple laptop.

Speed: Spark is incredibly fast and is continuously praised for it in the big data world.

General-purpose engine: Spark allows developers to use and combine multiple types of computations, such as SQL queries, text processing, machine learning, etc.

## What is Spark?

Spark is fundamentally a cluster-based computational platform designed to be fast and general purpose. If we attempt to define a specific purpose for Spark we’d find ourselves constrained by the many use cases this technology offers. However, Spark is usually referred to as a unified analytics engine for large-scale data processing.

-------------------

In developers’ terms, the beauty of Spark is in the fact that it is a set of libraries written in different languages, such as Scala, Java, Python, etc… Spark enriches a program with intensive processing capabilities and provides a distributed nature, which allows it to run on every machine within a cluster in a coordinated fashion.

------------------------

Because Spark runs computations in memory as much as possible, it reduces the time taken from hours to minutes while processing large datasets. It does so by primarily processing data chunks in memory, rather than relying on I/O devices such as hard disks, which introduces higher latencies in data processing and transferring in general.

--------------------------------------

Its general-purpose nature is expressed by being able to support a wide range of different features, such as imperative programming (iterative algorithms), SQL querying, stream processing, and, in this course’s case, batch processing.

--------------------------

Spark is open source and backed by the Apache Software Foundation, thus benefiting from developer’s contributions that aim to make it more efficient or include new features (naturally undergoing a review, check, and approval process by Apache.)

---------------------------------

Big tech giants such as Netflix and eBay have deployed Spark at a massive scale, and the adoption of Spark spans multiple and diverse industries as well.



## A brief history of Spark

So what are the precursors to Spark? Let’s take a look at Spark’s history, the hisotry of related technologies.

### Enter MapReduce

MapReduce was born in 2004 as a distributed processing framework originally referred to as Google propriety. It can broadly be described as a model for processing big datasets in parallel and on a cluster, mainly comprising of three operations:

* A Map procedure can be seen as a function applied to local data in different nodes of a cluster, this defines a “mapping” stage. This means that it identifies or defines IDs and their corresponding values for records.

* A Shuffle stage happens within the nodes of a cluster, usually accompanied by a Sort one, which operates on the results from the Map stage and arranges related information at a global scale. This means that it puts information together in the shape of key-value pairs, based on matching keys. It also sorts the information as it goes.

* Then, a Reduce operation is conducted on the output of the previous stage, which executes on the nodes of the cluster again, and applies some computation to aggregate the mapped information.

This model implements a “Divide and Conquer” approach, where a big problem (in this case applying an algorithm efficiently to big quantities of data) is split into smaller parts and executed in parallel. This thus uses resources more efficiently and is more time effective.

# 2. Spark and Big Data

### Big data primer

Before we describe the processing model that Spark fits into in both the context of this course and big data, it’s important to explain what big data means.

The term big data fundamentally refers to various technologies aligned with different strategies on how to process large datasets of information.

The word “large” has traditionally and implicitly included the notion that whatever dataset is being processed, it packs an amount of information that realistically cannot be processed by a single resource, such as a lone server or computer. Because available processing power and business needs are constantly changing, the word also includes the notion that the exact size of a dataset is not estimated to a specific figure.

As vague as it might seem, “big” is an appropriate word to refer to datasets that are undefined by the limits of their size while representing vast volumes of information. So, big data solutions aim to solve the problem that conventional methods face while working with them.

Another characteristic of big data scenarios is the variety of sources that the information comes from. These sources range from application systems’ logs and social networks data to physical devices’ output. In turn, this scenario introduces a variety of formats a big data solution might be expected to work with. With different sources come different formats.

Whereas traditional systems might expect input formatted or labeled data, big data systems need to deal with raw data and eventually transform it into meaningful information according to different business requirements.

Alongside the evolution of big data systems, patterns started emerging. One of those is broadly defined as the big data life cycle.

### Big data life cycle

Even if big data systems do not process data uniformly, there are commonalities that can be found in the processing strategies and the steps that they usually involve.

The following is a list of common steps (non-exhaustive) which are usually referred to as the big data life cycle:

1. `Ingestion:` This is the process of incorporating raw data into the system for further processing. The complexity of this operation varies depending on the formats, sources, and media used to ingest the information into a system.

2. `Transformation or Analysis:` This comprises different operations applied to the raw data that might transform, analyze, sort, aggregate, or filter, the bulk of the ingested data. Labeling and Validation of the data might also take place in this step. Traditionally this step is referred to as the “computing step”, and its primary goal is to produce information.

3. `Storage:` Whether it is in the same or a different source, the information produced in the previous step is stored or persisted in a durable media.

4. `Visualization:` In the step that provides perhaps the most value to stakeholders, the stored information is displayed or visualized with the aid of tools. This provides meaningful data insights and detect trends or patterns of how data changes over time.

Spark and the batch data processing model#
Even though Spark can process data in several ways, depending on the Spark component used that targets a specific data processing model, this course focuses on the batch processing model.

To get a frame of reference, let’s quickly explain the terms relevant to batch processing.

This course’s batch processing model, which Spark allows us to construct, can be circumscribed in the broader Big data life cycle described previously. This version includes stages such as ingesting, filtering, applying transformations, and ultimately produces valuable information.

Batch processing is a method of computing information over large datasets. It involves splitting the data into smaller pieces or chunks, which are scheduled and sent to different processing units (or individual machines) for the actual computation to take place.

This computation, however, might involve shuffling information around, collecting intermediate results, and ultimately putting the pieces back together to form a final result.






























