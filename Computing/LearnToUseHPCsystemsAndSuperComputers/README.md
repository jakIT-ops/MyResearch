- Intro to HPC Systems and Supercomputers

- HPC system's basic components

- HPC software stack

- HPC job schedulers and batch systems (PBS and Slurm with demos)

- Introduction to parallel programming (Open MP, MPI and GPU coding)

# Supercomputers and HPC clusters

## A Little bit of Supercomputing history

Supercomputers play an important role in today’s research world. They aid us to solve compute-intensive problems such as physical simulation, climate research, molecular modeling and so on. Before we get into how to operate on a supercomputer, let’s revisit its history a bit.

### History of Supercomputing

The history of supercomputing started in 1960s! with the Atlasat the University of Manchester and a series of computers at `Control Data Corporation (CDC)`, originally designed by Seymour Cray (pictured below).

The Cray-2 released in 1985 was an 8 processor liquid cooled computer and Fluorinert was pumped through it as it operated. It performed at 1.9 gigaflops and was the world’s second fastest after M-13 supercomputer in Moscow.

While the supercomputers of the 1980s used only a few processors, in the 1990s, machines with thousands of processors began to appear in Japan and the United States, setting new computational performance records. For example, the Intel’s Paragon had 1,000-4,000 Intel i860 processors in various configurations, and was ranked the fastest in the world in 1993. The Paragon was a MIMD machine which connected processors via a high speed two dimensional mesh, allowing processes to execute on separate nodes, communicating via the Message Passing Interface or `MPI` (details to be discussed later).

If you want to know more about the supercomputing and its glorious past feel free to visit this [website](https://history-computer.com/cray-history/) in relation to history of computers.

## Supercomputing examples

### 1 Supercomputer in the world

The Sunway TaihuLight is a Chinese supercomputer which, as of November 2016, is ranked #1 in the TOP500 list (The TOP500 project ranks and details the 500 most powerful non-distributed computer systems in the world), as the fastest supercomputer in the world, with a LINPACK benchmark rating of 93 petaflops. Let’s first watch a documentary video on this system:

https://www.youtube.com/watch?v=KEdsrT1mFAU&t=21s

It was designed by the National Research Center of Parallel Computer Engineering & Technology and is located at the National Supercomputing Center in Wuxi in the city of Wuxi, in Jiangsu province, China. This cluster operates using a Linux variant called Sunwat RaiseOS. It has a total of 40,960 manycore 64-bit RISC processor nodes.Each processor chip contains 256 processing cores, and an additional four auxiliary cores for system management for a total of 10,649,600 CPU cores across the entire system. It has a total of 1.31 PB of internal memory and requires 15,371.00 kW of power to operate.

### Future Supercomputers - 150-300 PFlops

The Summit is a supercomputer being developed by IBM for use at Oak Ridge National Laboratory. The system will be powered by IBM’s POWER9 CPUs and Nvidia Volta GPUs. The system is targeting 150 - 300 PFLOPS of performance at 10 MW of power. The computer will be finished in 2017, and moved to Oak Ridge in 2018 where it will replace its current Titan supercomputer. It will have ~4600 compute nodes, with 2 x IBM Power9 CPUs, 6 x Nvidia Volta GPUs and 512 GB internal memory pre node. Finanly, the whole cluster will have a total 10 PB of memory.

### Top supercomputing facilities at renowned Universities around the world

Let’s now know about some more examples of supercomputers that are readily available for the researchers at universities (`know more`[https://www.highereddive.com/news/these-7-supercomputers-are-the-fastest-at-us-universities/271816/])

# HPC cluster computers

The term cluster computing is used to denote nothing but two or more computers that are networked together to provide solutions as required. However, this idea should not be confused with a more general client-server model of computing as the idea behind clusters is quite unique.

A cluster of computers joins computational powers of the compute nodes to provide a more combined computational power. Therefore, as in the client-server model, rather than a simple client making requests of one or more servers, cluster computing utilize multiple machines to provide a more powerful computing environment perhaps through a single operating system.

In its simplest structure, HPC clusters are intended to utilize parallel computing to apply more processor force for the arrangement (solution) of a problem. HPC clusters typically have a large number of computers (often called ‘nodes’) and, in general, most of these nodes would be configured identically. Though from the out side the cluster may look like a single system, the internal workings to make this happen can be quite complex.

Computer clusters emerged as a result of convergence of a number of computing trends including the availability of low-cost microprocessors, high speed networks, and software for high-performance distributed computing. They have a wide range of applicability and deployment, ranging from small business clusters with a handful of nodes to some of the fastest supercomputers in the world!

## Supercomputers vs. HPC clusters

According to [Jan Christian Meyer’s](https://www.quora.com/What-is-the-difference-between-a-supercomputer-and-a-computer-cluster) Quora response: "Supercomputer isn’t a name for one particular type of computer, it’s a term that refers to computers used to solve problems which require processing capabilities nearly as big as anyone can build at a given time. The types of systems that people call supercomputers change over time, supercomputers of yesteryear aren’t that super any more.

Cluster computers are loosely coupled parallel computers where the computing nodes have individual memory and instances of the operating system, but typically share a file system, and use an explicitly programmed high-speed network for communication. The term loosely refers to the technicalities of how such machines are constructed."

> “clusters” and “high-performance computing” are synonymous.

All the ideas that went into the design of supercomputers are now part of your everyday personal computer. So there is no real distinction anymore between personal computers and super computers: a supercomputer is just a cluster with a large number of ordinary processors. So the super prefix comes from the days when high performance computing was only done on very special machines called supercomputers. Those days are largely gone. Only NEC still makes processors that are descendants of the old supers, but even they put them in a cluster. Now-a-days, every “super” computer these days is a cluster.


# Benefits of using cluster computing

HPC systems derive their computational power by exploiting parallelism. Programs for HPC systems must be splitted up into many smaller sub-programs which can be executed in parallel on different processors. HPC systems can offer parallelism at a much larger scale, with 100’s or 1000’s, or even millions of tasks running concurrently.However, writing parallel software can be challenging, and many existing software packages do not already support parallelism & may require development.

https://www.youtube.com/watch?v=NsCD7Xd1-Q8&feature=emb_title

Therefore, HPCs are userful when you have:

* A program that can be recompiled or reconfigured to use optimized numerical libraries that are available on HPC systems but not on your own system;

* You have a parallel problem, e.g. you have a single application that needs to be rerun many times with different parameters;

* You have an application that has already been designed with parallelism;

* To make use of the large memory available;

* problem solutions require backups for future use. HPC facilities are reliable and regularly backed up.

## When not to use HPC systems?

* You have a single threaded job which will only run one job at a time (typical of MatLab users);

* You rely on DBMS/ databases;

* You have a lot of data to transfer between your local machine and the HPC on a continuous basis (e.g. per job);

* You need to have a GUI to interact with your program.
