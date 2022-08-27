## Servers

Think of them as computers that are responsible for the storage of data, computation (where your application lives and provides some value), perform some networking functions. Inside a server, you will find a processor, motherboard, RAM, a networking card, a hard disk, and a power supply.

Servers are expensive and they require a lot of power and people to keep them operational. They are normally procured by the IT team and are kept running as long as possible so that the organization gets the maximum return on its investment. The hardware on the servers fail more often than you think and requires maintenance.

Physical servers are great because they can be configured however you want. But, physical servers lead to waste because it is difficult to run multiple applications on the same server. Software conflicts, network routing, and user access all become more complicated when a server is maximally utilized with multiple applications. Hardware virtualization solves some of these problems.

## Virtualization

Virtualization emulates a physical server’s hardware in software. A Virtual Machine (VM) can be created on-demand, is entirely programmable in software. Hypervisors increase these benefits because you can run multiple virtual machines (VMs) on a physical server.

## Hypervisors

Hypervisors allow applications to be portable because you can move a VM from one physical server to another. One problem with running your own virtualization platform is that VMs still require hardware to run. Companies still need to have all the people and approvals required to run physical servers, but now capacity planning becomes harder because they have to account for VM overhead too.

## What is a Data Center?

A data center is a physical facility that is used to house all the hardware that is needed for applications to function.

### Data Center Components

Data centers are often referred to as a singular thing, but in actuality, they are composed of a number of technical elements such as routers, switches, security devices, storage systems, servers, application delivery controllers, and more. These are the components that are needed to store, run and manage applications. Due to the needs of the application and the decreasing life of the hardware managing a data center is a time-consuming task.

### Data Center Infrastructure

In addition to technical equipment, a data center also requires a significant amount of facilities infrastructure to keep the hardware and software up and running. This includes power subsystems, uninterruptible power supplies (UPS), ventilation and cooling systems, backup generators, and cabling to connect to external network operators i.e a connection to the internet where applicable.

### Data Center Architecture

Any company of significant size will likely have multiple data centers possibly in multiple regions. This gives the organization flexibility in how it backs up its information and protects against natural and manmade disasters like floods, storms, earthquakes etc. How the data center is architected can be some of the most difficult decisions because there are almost unlimited options.

## Reasons To Move To The Cloud

Capital Expense vs Variable Expense!

Instead of having to invest heavily in building data centers and acquiring servers before you know how you are going to use them, you pay only when you consume resources.

### Benefit from massive economies of scale:

By using cloud computing, you can achieve a lower variable cost than you can get on your own. Because usage from hundreds of thousands of customers is aggregated in the cloud, providers like AWS, Azure, Oracle can achieve higher economies of scale, which translates into lower pay-as-you-go prices for the end IaaS customers.

### Stop guessing about capacity:

Eliminate guessing on your infrastructure capacity needs. When you make a capacity decision prior to deploying an application, you often end up either sitting on expensive idle resources or dealing with limited capacity. With cloud computing, these problems are negated. You can access as much or as little capacity as you need, and scale up and down as required.

### Increase speed and agility:

In a cloud computing environment, new IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. This results in a dramatic increase in agility for the organization since the cost and time it takes to experiment and develop is significantly lower.

### Stop spending money on running and maintaining data centers:

Focus on projects that differentiate your business, not the infrastructure. Cloud computing lets you focus on your own customers, rather than on the heavy lifting of racking, stacking, powering, and maintaining your servers.

### Go global in minutes

Easily deploy your application in multiple regions around the world with just a few clicks. This means you can provide lower latency and a better experience for your customers at a minimal cost.

### Almost zero upfront infrastructure investment:

If you have to build a large-scale system it may cost a fortune to invest in real estate, physical security, hardware (racks, servers, routers, backup power supplies), hardware management (power management, cooling), and operations personnel. Because of the high upfront costs, the project would typically require several rounds of approvals before the project could even get started. Now, with utility-style cloud computing, there are no fixed or startup costs.

### Just-in-time Infrastructure:

In the past, if your application became popular and your systems or your infrastructure did not scale you became a victim of your own success. Conversely, if you invested heavily and the app did not get popular, your investment in infrastructure is lost. By deploying applications in the cloud with just-in-time self-provisioning, you do not have to worry about pre-procuring capacity for large-scale systems. This increases agility, lowers risk, and lowers operational cost because you scale only as you grow and only pay for what you use.

### More efficient resource utilization:

System administrators usually worry about procuring hardware (when they run out of capacity) and higher infrastructure utilization (when they have excess and idle capacity). With the cloud, they can manage resources more effectively and efficiently by having the applications request and relinquish resources on demand.

### Usage-based costing:

With utility-style pricing, you are billed only for the infrastructure that is being used. You are not paying for allocated or unused infrastructure. This adds a new dimension to cost savings. You can see immediate cost savings (sometimes as early as your next month’s bill) when you deploy an optimization patch to update your cloud application.

Moreover, if you are building and selling a platform on the top of the cloud, you can pass on the same flexible, variable usage-based cost structure to your own customers.

### Reduced time to market:

Parallelization is one of the great ways to speed up processing. If one compute-intensive or data-intensive job that can be run in parallel takes 500 hours to process on one machine, with cloud architectures, it would be possible to spawn and launch 500 instances and process the same job in 1 hour. Having available an elastic infrastructure provides the application with the ability to exploit parallelization in a cost-effective manner reducing time to market.

## Technical Benefits of Cloud Computing

Some of the technical benefits of cloud computing include:

### Automation“Scriptable infrastructure”:

You can create repeatable build and deployment systems by leveraging programmable (API-driven) infrastructure. This comes back to the point of deploying in a new geographical region in less than 10 minutes. You are not hunting for data centers or buying hardware. You simply run your cloud formation script to create your entire fleet of servers along with all your network configurations.

### Auto-scaling:

You can scale your applications up and down to match your unexpected demand without any human intervention. Auto-scaling encourages automation and drives more efficiency.

### Proactive Scaling:

Scale your application up and down to meet your anticipated demand with proper planning understanding of your traffic patterns so that you keep your costs low while scaling.

### Efficient Development lifecycle:

Production systems may be easily cloned for use as a development and test environment. Staging environments may be easily promoted to production.

### Improved Testability:

Never run out of hardware for testing. Spin-up and spin-down testing environments as and when you need them. Whether you want to run automation tests, load tests, longevity tests you can use the infrastructure and return it when you are done with them.

### Disaster Recovery and Business Continuity:

The cloud provides a lower-cost option for maintaining a fleet of DR servers and data storage. With the cloud, you can take advantage of geo-distribution and replicate the environment in other locations within minutes.

### “Overflow” the traffic to the cloud:

With a few clicks and effective load balancing tactics, you can create a complete overflow-proof application by routing excess traffic to the cloud from your existing on-prem infrastructure.


# 1. Understanding Amazon Web Services (AWS)

## Compute / VMs

Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. You can bundle the operating system, application software, and associated configuration settings into an Amazon Machine Image (AMI).

## On-Demand & Reserved Instances

You can then use these AMIs to provision multiple virtualized instances as well as decommission them using simple web service calls to scale capacity up and down quickly, as your capacity requirement changes. You can purchase On-Demand Instances in which you pay for the instances by the hour or Reserved Instances in which you pay a low, one-time payment and receive a lower usage rate to run the instance than with an On-Demand Instance or Spot Instances where you can bid for unused capacity and further reduce your cost. Instances can be launched in one or more geographical regions.

## Reliability / Fault Tolerance

Each region has multiple Availability Zones. Availability Zones are distinct locations that are engineered to be insulated from failures in other Availability Zones and provide inexpensive, low latency network connectivity to other Availability Zones in the same region.

## Elastic IP

Elastic IP addresses allow you to allocate a static IP address and programmatically assign it to an instance.

## Monitoring

You can enable monitoring on an Amazon EC2 instance using Amazon CloudWatch in order to gain visibility into resource utilization, operational performance, and overall demand patterns (including metrics such as CPU utilization, disk reads and writes, and network traffic).

## Auto-scaling

You can create an auto-scaling group using the Auto-scaling features to automatically scale your capacity on certain conditions based on metrics that Amazon CloudWatch collects.

## Load Balancing

You can also distribute incoming traffic by creating an elastic load balancer using the Elastic Load Balancing service.

## Storage

Amazon Elastic Block Storage (EBS) volumes provide network-attached persistent storage to Amazon EC2 instances. Point-in-time consistent snapshots of EBS volumes can be created and stored on Amazon Simple Storage Service (Amazon S3).

Amazon S3 is a highly durable and distributed data store. With a simple web services interface, you can store and retrieve large amounts of data as objects in buckets (containers) at any time, from anywhere on the web using standard HTTP verbs.

Amazon SimpleDB is a web service that provides the core functionality of a database- real-time lookup and simple querying of structured data - without operational complexity. You can organize the dataset into domains and can run queries across all of the data stored in a particular domain. Domains are collections of items that are described by attribute-value pairs.

## Content Delivery Network (CDN)

Copies of objects can be distributed and cached at 14 edge locations around the world by creating a distribution using Amazon CloudFront service – a web service for content delivery (static or streaming content).

## Simple Notification Service

Amazon SNS is a fully managed pub/sub messaging service that makes it easy to decouple and scale microservices, distributed systems, and serverless applications. With SNS, you can use topics to decouple message publishers from subscribers, fan-out messages to multiple recipients at once, and eliminate polling in your applications.

## Amazon Simple Queue Service (SQS)

SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message-oriented middleware.

# 2. Introduction to Cloud Native Principles

## Cloud-Native Principles

A cloud-native application is engineered to run on a platform and is designed for resiliency, agility, operability, and observability.

1. Resiliency embraces failures instead of trying to prevent them; it takes advantage of the dynamic nature of running on a platform.

2. Agility allows for fast deployments and quick iterations.

3. Operability adds control of application life cycles from inside the application instead of relying on external processes and monitors.

4. Observability provides information to answer questions about the application state. Think to monitor.

The Cloud Native Computing Foundation (CNCF) has defined cloud-native as:

1. Micro-services based Architecture

2. Containerized

3. Distributed Management and Orchestration

## What is a container?

Container in short is a lightweight Virtual Machine. Containers are a way to package all that is needed for your application to work, be it the operating system, libraries, config files, or other applications all into one bundle.

There are 2 concepts in containers, Images & Running Containers.

1. Image containers have images of the OS or the application itself, they are static.

2. Running containers on the other hand are containers on a single host without visibility into each others’ processes, files, network

## Virtual Machines

VMs virtualize the hardware aspect of a computer whereas containers virtualize at the operating system level. VMs need a Guest OS on top of Hypervisor, a virtualization software.

## Hypervisors

The hypervisor manages the allocation of the Hardware’s processor, memory & resources to the VMs. On the flip side, Containers share the OS’s compute, memory & resources and at the same time achieve the isolation provided by the VM architecture. Simply put, by eliminating the guest OS from a VM would give us Containers, which in itself reduces a lot of overhead that comes along with VMs.

## Containers

What are we trying to achieve using containers? Isolation, Co-existence of applications, virtualization of software, replication in diff environments.

Containerization is an OS feature where Kernel allows the existence of multiple, isolated user spaces known as Containers. These containers may appear as real computers to programs running in them as they have access to all the resources a real computer provides, like connected devices including network devices, computing power, memory, hard disk. However, a container is isolated from other containers & resources allocated to them.

If you need to replicate your application in multiple environments, you can package the application and all of its dependencies into a container image, and all your developer, test, production & support teams will have the same image to start with. And once you have the container image, you can bring up the container in a matter of minutes or less.

Imagine a scenario in which a customer has an issue on the field and support folks try to replicate it in their own environments. How many times have they struggled with setting up the environments and not being able to reproduce them? A similar case repeats itself with developer & QA environments.

Now, just imagine a situation where the support folks are able to whip up a container and have exactly the same environment as is in the field with the customer. Similarly, developers and test/QA personnel. I am sure you would have come across such inconsistencies in a lot of scenarios starting from developing a product to testing. This is just one of the issues that containers tackle.

## What are docker containers?

Docker is a platform for developing, shipping, running applications using container virtualization technology. Docker aids in separating your application from your infrastructure and helps in treating your Infrastructure like the way you would treat any managed application. Docker is one of the most commonly used Containerization tools.

Docker containers have demonstrated that containerization can drive the scalability and portability of applications. Developers and IT operations are turning to containers for packaging code and dependencies written in a variety of languages. Containers are also playing a crucial role in DevOps processes. They have become an integral part of build automation and continuous integration and continuous deployment (CI/CD) pipelines.

Docker aims to provide a lightweight way to create containers to manage and deploy your applications with isolation and security where you can get more out of your hardware.

## Kubernetes

Kubernetes is an open-source container orchestration tool designed to automate deploying, scaling, and operating containerized applications. Why is this here? It is here because “Distributed Management and Orchestration” is an integral part of making your application Cloud Native.

Kubernetes was born from Google’s 15-year experience running production workloads. It is designed to grow from tens, thousands, or even millions of containers. Kubernetes is container runtime agnostic.
