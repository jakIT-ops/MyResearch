# Introduction to Slurm

The Slurm Workload Manager (formerly known as Simple Linux Utility for Resource Management or SLURM), is a free and open-source job scheduler for Linux and Unix-like kernels, used by many of the world’s supercomputers and computer clusters. It provides three key functions.

* First, it allocates exclusive and/or non-exclusive access to resources (computer nodes) to users for some duration of time so they can perform work.

* Second, it provides a framework for starting, executing, and monitoring work (typically a parallel job such as MPI) on a set of allocated nodes.
Slurm is the workload manager on about 60% of the TOP500 supercomputers, including Tianhe-2 that, until 2016, was the world’s fastest computer.

* Finally, it arbitrates contention for resources by managing a queue of pending jobs.

## History

Slurm began development as a collaborative effort primarily by Lawrence Livermore National Laboratory, SchedMD, Linux NetworX, Hewlett-Packard, and Groupe Bull as a Free Software resource manager in the 2010s. It was inspired by the closed source Quadrics RMS and shares a similar syntax. The name is a reference to the soda in Futurama!

https://www.youtube.com/watch?v=jEliv9pflwA&feature=emb_title

## Slurm commands

* sacct is used to report job or job step accounting information about active or completed jobs.

* salloc is used to allocate resources for a job in real time.

* sattach is used to attach standard input, output, and error plus signal capabilities to a currently running job or job step.

* sbatch is used to submit a job script for later execution. The script will typically contain one or more srun commands to launch parallel tasks.

* sbcast is used to transfer a file from local disk to local disk on the nodes allocated to a job.

* scancel is used to cancel a pending or running job or job step. It can also be used to send an arbitrary signal to all processes associated with a running job or job step.

* scontrol is the administrative tool used to view and/or modify Slurm state. Many scontrol commands can only be executed as user root.

* sinfo reports the state of partitions and nodes managed by Slurm. It has a wide variety of filtering, sorting, and formatting options.

* smap reports state information for jobs, partitions, and nodes managed by Slurm, but graphically displays the information to reflect network topology.

* squeue reports the state of jobs or job steps. It has a wide variety of filtering, sorting, and formatting options. By default, it reports the running jobs in priority order and then the pending jobs in priority order.

* srun is used to submit a job for execution or initiate job steps in real time.

* strigger is used to set, get or view event triggers. Event triggers include things such as nodes going down or jobs approaching their time limit.

* sview is a graphical user interface to get and update state information for jobs, partitions, and nodes managed by Slurm.
