# 1. What is DevOps ? And why is it important on the Cloud ?

## Benefits of DevOps

### Speed

Move at a higher velocity so you can innovate for customers faster, adapt to changing markets better, and grow more efficiently at driving business results. DevOps enables your developers and operations teams to achieve these results. For example, microservices and continuous delivery let teams take ownership of services and then release updates to them quicker. Since speed and quick iteration is one of the key benefits of moving to the cloud DevOps is important.

### Rapid Delivery

Increase the frequency and pace of releases so you can innovate and improve your product faster. The quicker you can release new features and fix bugs, the faster you can respond to your customers’ needs and build a competitive advantage. Continuous integration & continuous delivery are practices that automate the software release process, from build to deploy.

### Reliability

Ensure the quality of application updates and infrastructure changes so you can reliably deliver at a more rapid pace while maintaining a positive experience for end-users. Use practices like continuous integration and continuous delivery to test that each change is functional and safe. Monitoring and logging practices help you stay informed of performance in real-time.

### Scale

Operate and manage your infrastructure and development processes at scale. Automation and consistency help you manage complex or changing systems efficiently and with reduced risk. For example, infrastructure as code helps you manage your development, testing, and production environments in a repeatable and more efficient manner.

### Improved Collaboration

Build more effective teams under a DevOps cultural model, which emphasizes values such as ownership and accountability. Developers and operations teams collaborate closely, share many responsibilities, and combine their workflows. This reduces inefficiencies and saves time (e.g. reduced handover periods between developers and operations, writing code that takes into account the environment in which it is run).

### Security

Move quickly while retaining control and preserving compliance. You can adopt a DevOps model without sacrificing security by using automated compliance policies, fine-grained controls, and configuration management techniques. For example, using infrastructure as code and policy as code, you can define and then track compliance at scale.

### Why DevOps Matters

Software and the Internet have transformed the world and its industries, from shopping to entertainment to banking. Software no longer merely supports a business; rather it becomes an integral component of every part of a business.

Companies interact with their customers through software delivered as online services or applications and on all sorts of devices. They also use software to increase operational efficiencies by transforming every part of the value chain, such as logistics, communications, and operations. In a similar way that physical goods companies transformed how they design, build, and deliver products using industrial automation throughout the 20th century, companies in today’s world must transform how they build and deliver software.

## How to Adopt a DevOps Model

### DevOps Cultural Philosophy

Transitioning to DevOps requires a change in culture and mindset. At its simplest, DevOps is about removing the barriers between two traditionally siloed teams, development, and operations. In some organizations, there may not even be separate development and operations teams; engineers may do both. With DevOps, the two teams work together to optimize both the productivity of developers and the reliability of operations.

They strive to communicate frequently, increase efficiencies, and improve the quality of services they provide to customers. They take full ownership for their services, often beyond where their stated roles or titles have traditionally been scoped by thinking about the end customer’s needs and how they can contribute to solving those needs.

Quality assurance and security teams may also become tightly integrated with these teams. Organizations using a DevOps model, regardless of their organizational structure, have teams that view the entire development and infrastructure lifecycle as part of their responsibilities.

### DevOps Practices

There are a few key practices that help organizations innovate faster through automating and streamlining the software development and infrastructure management processes. Most of these practices are accomplished with proper tooling.

One fundamental practice is to perform very frequent but small updates. This is how organizations innovate faster for their customers. These updates are usually more incremental in nature than the occasional updates performed under traditional release practices. Frequent but small updates make each deployment less risky. They help teams address bugs faster because teams can identify the last deployment that caused the error. Although the cadence and size of updates will vary, organizations using a DevOps model deploy updates much more often than organizations using traditional software development practices.

Organizations might also use a microservices architecture to make their applications more flexible and enable quicker innovation. The microservices architecture decouples large, complex systems into simple, independent projects. Applications are broken into many individual components (services) with each service scoped to a single purpose or function and operated independently of its peer services and the application as a whole. This architecture reduces the coordination overhead of updating applications, and when each service is paired with small, agile teams who take ownership of each service, organizations can move more quickly.

However, the combination of microservices and increased release frequency leads to significantly more deployments which can present operational challenges. Thus, DevOps practices like continuous integration and continuous delivery solve these issues and let organizations deliver rapidly in a safe and reliable manner. Infrastructure automation practices, like infrastructure as code and configuration management, help to keep computing resources elastic and responsive to frequent changes. In addition, the use of monitoring and logging helps engineers track the performance of applications and infrastructure so they can react quickly to problems.

# 2. Operational Excellence on the Cloud

## Operational Excellence

The operational excellence pillar includes the ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures.

The operational excellence pillar provides an overview of design principles, best practices, and questions

## Design Principles

There are six design principles for operational excellence in the cloud:

### Perform operations as code:

In the cloud, you can apply the same engineering discipline that you use for application code to your entire environment. You can define your entire workload (applications, infrastructure, etc.) as code and update it with code. You can script your operations procedures and automate their execution by triggering them in response to events. By performing operations as code, you limit human error and enable consistent responses to events.

### Annotate documentation:

In an on-premises environment, documentation is created by hand, used by people, and hard to keep in sync with the pace of change. In the cloud, you can automate the creation of documentation after every build (or automatically annotate hand-crafted documentation). Annotated documentation can be used by people and systems. Use annotations as an input to your operations code.

Make frequent, small, reversible changes: Design workloads to allow components to be updated regularly. Make changes in small increments that can be reversed if they fail (without affecting customers when possible).

### Refine operations procedures frequently:

As you use operations procedures, look for opportunities to improve them. As you evolve your workload, evolve your procedures appropriately. Set up regular game days to review and validate that all procedures are effective and that teams are familiar with them.

### Anticipate failure:

Perform “premortem” exercises to identify potential sources of failure so that they can be removed or mitigated.

Test your failure scenarios and validate your understanding of their impact. Test your response procedures to ensure that they are effective and that teams are familiar with their execution. Set up regular game days to test workloads and team responses to simulated events.

### Learn from all operational failures:

Drive improvement through lessons learned from all operational events and failures. Share what is learned across teams and through the entire organization.

### Definition

There are three best practice areas for operational excellence in the cloud:

1. Prepare

2. Operate

3. Evolve

Operations teams need to understand their business and customer needs so they can effectively and efficiently support business outcomes. Operations create and use procedures to respond to operational events and validate their effectiveness to support business needs. Operations collect metrics that are used to measure the achievement of desired business outcomes.

Everything continues to change—your business context, business priorities, customer needs, etc. It’s important to design operations to support evolution over time in response to change and to incorporate lessons learned through their performance.

# 3. Continuous Integration & Continuous Delivery

## Continuous Integration (CI)

With continuous integration, developers frequently integrate their code into the main branch of a common repository. Rather than building features in isolation and submitting each of them at the end of the cycle, a developer will strive to contribute software work products to the repository several times on any given day.

The big idea here is to reduce integration costs by having developers do it sooner and more frequently. In practice, a developer will often discover boundary conflicts between new and existing code at the time of integration. If it’s done early and often, the expectation is that such conflict resolutions will be easier and less costly to perform.

Of course, there are trade-offs. This process change does not provide any additional quality assurances. Indeed, many organizations find that such integration becomes more costly since they rely on manual procedures to ensure that new code doesn’t introduce new bugs, and doesn’t break existing code. To reduce friction during integration tasks, continuous integration relies on test suites and automated test execution. It’s important, however, to realize that automated testing is quite different from continuous testing.

The goal of CI is to refine integration into a simple, easily-repeatable everyday development task that will serve to reduce overall build costs and reveal defects early in the cycle. Success in CI will depend on changes to the culture of the development team so that there are incentives for readiness, frequent and iterative builds, and eagerness to deal with bugs when they are found much earlier.

## Continuous Delivery (CD)

Continuous delivery is actually an extension of CI, in which the software delivery process is automated further to enable easily and confident deployments into production at any time. A mature continuous delivery process exhibits a codebase that is always deployable on the spot. With CD, software release becomes a routine event without emotion or urgency. Teams proceed with daily development tasks in the confidence that they can build a production-grade release any old time they please without elaborate orchestration.

CD depends centrally on a deployment pipeline by which the team automates the testing and deployment processes. This pipeline is an automated system that executes a progressive set of test suites against the build. CD is highly automatable and in some cloud-computing environments easily configurable.

In each segment in the pipeline, the build may fail a critical test and alert the team. Otherwise, it continues on to the next test suite, and successive test passes will result in automatic promotion to the next segment in the pipeline. The last segment in the pipeline will deploy the build to a production-equivalent environment. This is a comprehensive activity, since the build, the deployment, and the environment are all exercised and tested together. The result is a build that is deployable and verifiable in an actual production environment.

A solid exhibit of a modern CI/CD pipeline is available on the cloud with AWS. Amazon is one of the cloud-computing providers that offers an impressive CI/CD pipeline environment and provides a walk-through procedure in which you can choose from among its many development resources and link them together in a pipeline that is readily configurable and easily monitored.
