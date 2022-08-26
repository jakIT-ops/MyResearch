### Fork-join framework

There are new Java concurrency APIs (JSR 166y) referred to as the Fork-join framework. It is designed for tasks that can be broken down and takes advantage of multiple processors. The following are the core classes (all located in java.util.concurrent):

* ForkJoinPool: An ExecutorService for running ForkJoinTasks and managing and monitoring the tasks.

* ForkJoinTask: This represents the abstract task that runs within the ForkJoinPool.

* RecursiveTask: This is a subclass of ForkJoinTask whose compute method returns some value.

* RecursiveAction: This is a subclass of ForkJoinTask whose compute method does not return any value.
