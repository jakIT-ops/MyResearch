# 1. Safe Deployments

Although AWS Lambda technically works like a virtualised container management system, the life-cycle for Lambda functions is quite different from that of the usual container-based applications. This might be counter-intuitive to people who are used to managed container services. Luckily, AWS SAM hides most of the underlying complexity from developers. In this chapter, you will peek under the hood just enough so you can avoid subtle mistakes. Knowing how Lambda routes requests and provisions runtime environments is also critical for getting the most out of cloud functions.

## Function configurations

The core principle of serverless work is that the platform is responsible for receiving events from clients, not your code. The network socket (server) belongs to the hosting provider, not to your function. This allows the platform to decide how many instances to run and when. Lambda will not start any containers for your function until it receives events (unless you explicitly provisioned concurrency). Once related events arrive, the platform will start and maintain just enough instances to handle the workload. After a period of inactivity, if no events ask for a particular function, Lambda will remove the inactive containers. Although as a user you do not have any control over this process, it’s relatively easy to prove it: just measure request latency to spot cold starts.

That process is common for all serverless platform providers. With AWS Lambda in particular, events do not target a particular function; they target a particular version of a function, or, more precisely, events are connected to a version of the function configuration. In Lambda terminology, the function configuration describes all the properties of a runtime environment necessary to spin up a new container. That includes the following:

* The runtime type and version (so far you have used Node 12, but this could be a version of Python, Java, Ruby, and so on).

* How much memory and time the function can use.

* The URL of the function code package (SAM will set this up on S3 for you during deployment).

* The IAM role specifying what this function can access in AWS and who can call this function.

* Error recovery, logging, and environment parameters of the function.

You can see the configuration for any Lambda function by using the AWS CLI tools. First, find the actual name of the function by listing the stack resources (replace `<STACK_NAME>` with your stack name):

```nodejs
aws cloudformation list-stack-resources --stack-name <STACK_NAME>
```

# 2. Versions and Aliases

## Published versions

You can tell Lambda to keep a configured version by publishing it. Published versions are read-only copies of function configurations and they are not wiped out after a subsequent update. An event source can request that a particular published function version handles its events. That way, old deployments of the API Gateway can ask for the old Lambda code, and new deployments can ask for the new Lambda function. During an update, any events aimed at the previous version will just keep running on old containers. Once no events have requested an old version for a while, Lambda will remove those instances. When an event targets the new version, Lambda will create a new container using the newly published configuration.

## Aliases

To make deployments safe, you need to make sure that events target a particular version, not $LATEST. Each published configuration version has a unique numerical ID, assigned by Lambda incrementally with each deployment. In theory, you could manually keep track of these, ensure that event sources request a particular numerical version, and update the template before each deployment to rewire event sources, but this would be error-prone and laborious. Lambda allows you to declare configuration aliases, meaningful names pointing to a numerical version. For example, you can create an alias called live to represent a published configuration version and set up all event sources to request that alias. After an application update, you do not need to rewire event sources. You just need to point the alias to the new numerical version.

<br>
<div align="center">
	<img src="img/alias.png">
	<br>
	<code>An event source can ask for a specific alias, which points to a numerical version of a function.</code>
</div>
<br>

SAM automates the whole process of publishing numerical versions, assigning aliases, and wiring event sources to aliases. All you need to do is add the `AutoPublishAlias` property to the function properties, followed by the alias. An alias can be any Latin alphanumeric text between 1 and 128 characters.

```yaml
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello-world/
      Handler: app.lambdaHandler
      Runtime: nodejs12.x
      AutoPublishAlias: live
```



### Aliases and deployment pipelines#

Although in theory, you can set up different aliases for development, testing and production, this is not easy with CloudFormation and SAM. The more usual pattern is to just set up different stacks. That way each stack has completely separate functions, and those functions each have their own versions aliases.

The SAM AutoPublishAlias shortcut is helpful to always reassign the same alias​ but it does not help much with managing multiple versions in the same stack. Aliases with SAM are mostly useful to make deployments safer.

# 3. Gradual Deployments


## Routing configurations and AWS CodeDeploy

An alias always points to some numerical version, but it can also point to more than one version at the same time. This becomes incredibly useful for safe deployments. Lambda supports automatic load balancing between versions assigned to the same alias, using a feature called routing configuration.

Another AWS deployment product, called AWS CodeDeploy, can modify the routing configuration over time to gradually switch aliases between several versions of code and infrastructure. CodeDeploy can, for example, use the new version of an application only for 10% of the traffic and wait for a short period while monitoring for unexpected problems. If everything looks OK, CodeDeploy can expose the new version to everyone and shut down the old version. On the other hand, if the new version seems to be problematic, CodeDeploy will move all the users back to the old infrastructure and destroy the experimental version. Reassigning aliases to published configuration versions is very quick (much faster than a redeployment) making it easy and quick to recover from deployment errors.


### Modifying routing configurations manually#

SAM only manages routing configuration for deployments. If you want to play with this feature outside deployments, for example to run A/B tests in production, configure the alias routing configuration using the AWS command line tools. Use the aws lambda update-alias command. You can do this even for functions created using SAM.

## Linear and canary deployments

The Type property inside DeploymentPreference controls how the traffic moves from the old version to the new one. SAM can automate two types of deployment preferences: linear and canary.

Linear deployments work by incrementally moving traffic during a period of time. In this example, you set it to Linear10PercentEvery1Minute. This, unsurprisingly, turns on the tap slightly more every minute, so that the new version starts with only 10% of the requests and each minute gets 10% more. That is why the new message will show up more frequently as the deployment progresses.

Canary deployments work in two steps. At the start of the deployment, CodeDeploy sets up routing so that the new version gets a specific percentage of requests. If there are no problems until the end of the deployment, the alias is completely assigned to the new version. For example, Canary10Percent15Minutes would send 10% of the traffic to the new version at the start, wait 15 minutes, and then move the remaining 90% to the new version.

# 4. Adding Deployment Alerts

## CloudWatch

So far, you haven’t set up any tests o compare the old and new versions. You could manually try things out during the deployment and then roll back in case of problems from the CodeDeploy Web Console, but that’s not really efficient or sustainable. It would be better if CodeDeploy did this automatically.

Luckily, CloudWatch can look out for errors automatically. You used CloudWatch to access logs in the previous chapter, but you can also use it to inspect and monitor operational statistics about your application. CloudWatch automatically tracks lots of interesting information about AWS Lambda and API Gateway, such as latency, number of invocations, and number of errors. Here is how you can see this information:

1. Go to the AWS Web Console, https://aws.amazon.com, and sign in if necessary.

2. Select CloudWatch in the list of services.

3. Select Metrics in the left-hand menu.

4. In the list of metric namespaces, select Lambda then By Function name, and select check boxes next to errors and invocations for your function.

## Setting alarms

Monitoring changes over time might be interesting and even amusing, but you should not rely on human interaction to spot errors. CloudWatch can automatically send notifications if metrics exceed a certain threshold, using a feature called alarms. You could set up an alarm to send someone an email in case user requests start taking too long to execute, or even invoke a Lambda function when something bad happens.

To create an alarm manually, switch to the Graphed metrics tab, then click the bell icon in the Actions column next to a metric row in the bottom table on the page. You can, for example, use that to send yourself an email if a Lambda function starts throwing errors.










