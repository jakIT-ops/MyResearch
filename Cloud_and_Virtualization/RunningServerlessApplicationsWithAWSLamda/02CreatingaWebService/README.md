# 1. Instialising the Application


## 1.1 The SAM command-line tool

<b>SAM</b> command-line tools can generate sample projects and events so that you can get started easily.

### The `sam init` command

Let’s dive right in and create a sample web service backed by a Lambda function. You will use the `code` directory to execute the commands. To create a simple SAM project in a new subdirectory, run the following command:

```nodejs
sam init --runtime nodejs12.x --name app --app-template hello-world
```

Enter y as a response. You should get a quick confirmation about the initialisation of a new project:

```nodejs
Enter y as a response. You should get a quick confirmation about the initialisation of a new project:

Cloning app templates from https://github.com/awslabs/aws-sam-cli-app-templates.git 
-----------------------
Generating application:
-----------------------
Name: app
Runtime: nodejs12.x
Dependency Manager: npm
Application Template: hello-world
Output Directory: .
```

If this command printed an error on your local machine, there is some issue with the setup. You should look at the chapter where we have the information on how to set up SAM command-line tools and other prerequisites.

### The `--runtime` argument

The `--runtime` argument tells SAM which programming language you’ll use to write the Lambda function, or more precisely which execution environment it is intended to run in. The `--runtime` argument is important for generating the sample project. You will learn how to add more functions to the same project later, and you can even mix functions that are executed in different languages.

To speed upscaling and operations, Lambda has pre-packaged execution environments, called runtimes, for many popular languages. The `nodejs12.x` runtime tells Lambda to run your function under Node.js 12, an execution engine for JavaScript. SAM can also create example projects in other languages. For example, use `java8` for a Java function. Check out the AWS Lambda runtimes page for a complete list.

### The `--name` argument

The `--name` argument tells SAM how to call the application, or more precisely the name for the subdirectory where the application files are stored. In the previous example case, `app` was used, so SAM will create a new subdirectory called `app` and copy the sample files there.

### The `--app-template` argument

The `--app-template` argument tells SAM which template to apply when initialising the application. You can see the list of standard templates in the `aws-sam-cli-app-templates` project on GitHub. SAM can also use your templates, which might be useful for teams that often create similar Lambda functions. For example, you could create a template for message queue handling, and then quickly apply it when creating a new payment processor that connects to your payments queue. Companies can also use templates to standardise project directory layouts. To specify your own template location, use the `--location` parameter and point to a GIT repository or a local directory. 

# 2 Infrastructure as Code

## 2.1 The CloudFormation template

For deploying applications, SAM uses CloudFormation, an AWS service for managing infrastructure as code. This means that CloudFormation converts a source file describing an application infrastructure (called `template`) into a set of running, configured cloud resources (called `stack`).

## 2.2 The CloudFormation stack

You can use CloudFormation to create a whole stack of resources from the template in a single command. It is also smart enough to detect the differences between a template and a deployed stack, making it easy to update infrastructure resources in the future.

## 2.3 Benefits of CloudFormation

* You can modify the template file and CloudFormation will reconfigure or delete only the resources that actually need to change.

* If a resource update fails for whatever reason, CloudFormation will reset all the other resources to the previous configuration, managing a whole set of infrastructural components as a single unit. This makes it easy and safe for a whole team of developers to add, remove, or reconfigure the infrastructural services supporting an application.

* It also becomes trivially simple to know which version of infrastructure is compatible with which version of code. This supports infrastructure traceability and reproducible installations. (It’s not a coincidence that the template file is in the same directory as the function source; they should be committed to a version control system together).

* Another benefit of CloudFormation is that you can share templates with other teams, or even publish them online so that others can set up your application with a single click.

## 2.4 CloudFormation Template Formats

CloudFormation supports JSON and YAML template formats. In this course, you’ll use YAML because it is easier to read in print. One downside of YAML is that whitespace is important and getting the right indentation might be a bit fiddly. If you want more control over the structure of your templates, feel free to use JSON instead. YAML is actually a superset of JSON, so you can also embed JSON into YAML for sections where you want to make structure clear and avoid problems with whitespace.

### YAML CloudFormation

The following file is the `template.yaml` from the project you created in the previous lesson. Let’s discuss it in detail.

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
  app

  Sample SAM Template for app
  
# More info about Globals: https://github.com/awslabs/serverless-application-model/blob/master/docs/globals.rst
Globals:
  Function:
    Timeout: 3

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function # More info about Function Resource: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Properties:
      CodeUri: hello-world/
      Handler: app.lambdaHandler
      Runtime: nodejs12.x
      Events:
        HelloWorld:
          Type: Api # More info about API Event Source: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
          Properties:
            Path: /hello
            Method: get

Outputs:
  # ServerlessRestApi is an implicit API created out of Events key under Serverless::Function
  # Find out more about other implicit resources you can reference within SAM
  # https://github.com/awslabs/serverless-application-model/blob/master/docs/internals/generated_resources.rst#api
  HelloWorldApi:
    Description: "API Gateway endpoint URL for Prod stage for Hello World function"
    Value: !Sub "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/hello/"
  HelloWorldFunction:
    Description: "Hello World Lambda Function ARN"
    Value: !GetAtt HelloWorldFunction.Arn
  HelloWorldFunctionIamRole:
    Description: "Implicit IAM Role created for Hello World function"
    Value: !GetAtt HelloWorldFunctionRole.Arn
```

The first line tells CloudFormation which syntax version to use:

```nodejs
AWSTemplateFormatVersion: '2010-09-09'
```

### The CloudFormation transform property

The second line in the example file tells CloudFormation to transform a template before executing it:

```nodejs
Transform: AWS::Serverless-2016-10-31
```

Generally speaking, with CloudFormation this is an optional setting. The part of SAM that runs in AWS data centers actually works as a CloudFormation transformation, so pretty much all your SAM applications will list a transformation at this point.

#### Using serverless resources without SAM command line tools

In order to use SAM CloudFormation transformation, you don’t need any software locally installed. You can just add the `Transform` header into your CloudFormation templates and deploy it using standard CloudFormation tools. The transformation physically executes inside AWS CloudFormation, as part of the normal deployment pipeline, not on development machines or a continuous integration server uploading the template to AWS.

# 3. Further Sections of 'template​.yaml'

## 3.1 Description

```nodejs
Description: >
  sam-app

  Sample SAM Template for sam-app
```

The Description section contains a free-form explanation of the template. This section is useful if you want to publish the template or give it to another team, but it isn’t necessary. You can safely skip it when creating templates for small experiments.

## 3.2 Global application settings

After the description, the example SAM template contains global application settings. This is a SAM-specific extension to CloudFormation and enables you to reduce the overall template file size by listing common settings in a single place instead of repeating them for each Lambda function. The example template contains just a single function, so adding global values doesn’t make a lot of difference, but this section is useful for more complex applications. The sample template usually contains a global Timeout setting, the number of seconds the function is allowed to run in Lambda:

```nodejs
Globals:
  Function:
    Timeout: 3
```

## 3.3 Reources

Next comes the Resources section, which lists the services or resources for CloudFormation to configure:

```nodejs
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello-world/
      Handler: app.lambdaHandler
      Runtime: nodejs12.x
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```


## Outputs

```nodejs
Outputs:
  HelloWorldApi:
    Description: "API Gateway endpoint URL for Prod stage for Hello World function"
    Value: !Sub "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/hello/"
  HelloWorldFunction:
    Description: "Hello World Lambda Function ARN"
    Value: !GetAtt HelloWorldFunction.Arn
  HelloWorldFunctionIamRole:
    Description: "Implicit IAM Role created for Hello World function"
    Value: !GetAtt HelloWorldFunctionRole.Arn
```

The first web service I created with Lambda, in early 2016 before SAM was available, had less than 20 lines of code but required about 200 lines of configuration scripts to set everything up. With SAM, you can achieve the same thing in just 10-15 lines of CloudFormation templates. Not bad!

## Serverless functions or Lambda functions

CloudFormation has another resource for Lambda functions: AWS::Lambda::Function. SAM extends it with AWS::Serverless::Function. The benefit of using the SAM version is that it automatically creates IAM policies and event triggers. If you want to have more direct control over IAM and trigger invocation, you can use the lower-level resource instead. However, you will then need to create security policies yourself.

# 4. The Lambda Programming Model

## 4.1 LambdaHandler

In the sample template, the combination of CodeUri, Handler, and Runtime means that the Lambda environment will try to execute the code using Node.js version 12 by calling the function called lambdaHandler inside app.js in the hello-world directory.

```js
let response;
exports.lambdaHandler = async(event, context) => {
	try {
		response = {
			'statusCode': 200,
			'body': JSON.stringify({
				message: 'hello world',
			})
		}
	} catch (err) {
		console.log(err);
		return err;
	}
	return response;
};
```


All Lambda functions have two arguments:

* `event` represents the data sent by the client invoking the function. In this case, it will contain information about the HTTP request.

* `context` contains useful information about the runtime environment, such as the allowed execution time or logging setup.

### Lambda interfaces in strongly typed languages

In strongly typed languages, such as Java, you can set up functions with specific request types and interfaces. In languages without strong typing, such as Python or JavaScript, these objects are mostly native key-value dictionaries or hash maps.

# 5. Steps to Deploy SAM Applications

CloudFormation is amazingly powerful. It can deploy and configure almost any resource type available in the Amazon cloud, safely upgrading and downgrading entire networks of services. However, in order to achieve such flexibility, CloudFormation also needs to be very generic. It does not know about the structure of JavaScript, Python, or Java projects, and it does not understand how to interact with programming language packages or dependency managers. In order to create a Lambda function, CloudFormation expects a fully self-contained ZIP archive. That archive needs to contain all the required files for the Lambda function, including the source or compiled code, third-party dependencies, and native binary packages. It also needs to be somewhere on Amazon S3 where CloudFormation can read it.

## Steps for deployments

1. `Build`: create a clean copy of all Lambda functions, remove test and development resources, and download third-party dependencies.

2. `Package`: bundle each function into a self-contained ZIP archive, upload it to S3, and produce a copy of the source application template that points to remote resources instead of local directories.

3. `Deploy`: upload the packaged template to CloudFormation, and execute the changes to create a running infrastructure.

<br>
<div align="center">
	<img src="img/steps.png">
	<br>
	<code>Deploying with SAM: ‘sam build’ creates a local self-contained copy, the ‘sam package’ function packages to S3, and ‘sam deploy’ creates a stack using CloudFormation.</code>
</div>
<br>


# 6. Inspecting a Stack

## Inspecting a stack from the AWS Web Console

Our first SAM function is live and ready to receive traffic. You just need to find out where SAM actually put it. For that, you’ll need to look at the stack outputs. The easiest way to inspect a stack is with the AWS Web Console. Here is how to find information about a stack:

1. Sign in to the AWS Web Console, at https://aws.amazon.com/.

2. Find the CloudFormation service.

3. Make sure that the region selector in the top-right corner is showing the region where you deployed the stack. For us-east-1, the region name is US East (N. Virginia).

4. In the list of stacks, click on sam-test-1 (or whatever you called the stack).

5. The console will show information about your stack, divided into several tabs.

## Inspecting a stack from the command line#

The web console is a nice interface for discovering new information, but if you know what you are looking for, it’s much faster to find it using the AWS command line tools. Instead of pointing and clicking, run the following command line:

```nodejs
aws cloudformation describe-stacks --stack-name sam-test-1 
```





































































