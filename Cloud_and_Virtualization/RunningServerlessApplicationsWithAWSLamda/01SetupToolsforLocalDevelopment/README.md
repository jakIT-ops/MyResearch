# 1. Setting Up the Prerequisites


## 1.1 The AWS SAM

The AWS Serverless Application Model (SAM) is a set of products that simplify developing, testing, and deploying applications using AWS Lambda. One part of SAM runs on developer machines and build servers, helping to prepare for deployment. Another aspect of SAM runs in AWS data centres during the deployment process. Unfortunately, as is the case with much AWS software, these products have overlapping names. Nobody outside Amazon really cares too much about the distinction, so informally they all get called SAM. Although it is possible to use different SAM products separately, in most cases they work together, so a clean separation between them isn’t especially important. In this chapter, you’ll learn how to set up the first part of SAM, which runs on developer machines.

> This product was previously called ‘SAM-local’, and today AWS documentation calls it the SAM Command Line Interface (SAM CLI).

SAM development tools help with building and packaging projects for deployment to AWS, debugging, simulating a Lambda environment, retrieving logs, and generating sample events for testing. You can set up command-line tools so you can use them with any editor, integrated development environment, or build system. Various AWS toolkits for popular editors and development environments also include these tools, making it possible to test, simulate, and debug Lambda functions directly from a visual interface. The AWS Cloud9 cloud-based integrated development environment also supports SAM tools.

## 1.2 Installing the required tools

AWS SAM CLI depends on a set of underlying tools which will be explained below, but whose full setup instructions are out of the scope of this course. That kind of information is easy to find online once you know what to look for, and it is likely to be updated more frequently directly on the individual tool websites. If you experience any problems with installing the tools below or want to use an alternative way of managing the packages, check out the AWS SAM Developer Guide online.

### Python

The SAM command-line tools are actually a set of Python scripts so you will need the Python runtime installed on your machine. You can use Python 2 version 2.7 or later, or Python 3 version 3.6 or later. Most Linux and macOS machines already have some version of Python installed. If you are unsure about this, check whether Python is installed and which version you have by running the following command:

```bash
python --version
```

### PIP

In addition to the Python runtime, you will also need to have the pip package management tool. Most Python installations already have one. To check whether it is installed on your machine, run the following command:

```bash
pip --version
```

### AWS

The final prerequisite is the basic AWS command-line tools package. Most developers that access AWS in any way usually have those tools already installed. To check whether your system already has these tools, run the following command:

```bash
aws --version
```

### If the command prints an error, you can download the tools by running the following command:

```bash
pip install awscli
```

### Docker

SAM tools use Docker, a container management system, to simulate the Lambda execution environment for local testing and debugging. You don’t need to install the full Docker service; the free (community) Docker Desktop tools are enough for all development tasks, including working with all the examples in this course. If you do not have Docker Desktop tools already installed, get the one-click installer for your operating system directly at the Docker website. You will not need Docker to actually run the code in production.

# 2. Installing JavaScript and SAM CLI

## 2.1 Installing JavaScript tools

### Node.js

In this course, you’ll be using JavaScript with Node.js for developing Lambda functions. (You do not need Node.js to work with SAM in a different language, but you will need the appropriate tools for that language.) To try examples from the book directly, you’ll need Node.js 12 or later installed. To check whether Node.js is installed on your machine, run the following command:


```nodejs
node --version
```


## 2.2 Installing the SAM command-line-tools

### Using Homebrew or Linuxbrew

There are several ways of installing SAM command-line tools. If you use Homebrew or Linuxbrew package management tools, you can install AWS SAM CLI using the following commands:

```nodejs
brew tap aws/tap
brew install aws-sam-cli
```	

### Using pip

Alternatively, use the `pip` package manager to download `sam`. Run the following command:

```nodejs
pip install aws-sam-cli
```

To check whether the installation worked, run the following command:

```nodejs
sam --version
```

If you get a response similar to the following, the software is ready:

```nodejs
$ sam --version
SAM CLI, version 0.40.0
```

# 3 Configuring Access Credentials

### SAM Configuration

AWS SAM CLI reuses the credential configurations from AWS command-line tools. If you already have credentials set up for AWS CLI, skip this section.

To deploy software to the AWS cloud, you will need an access key ID and a secret key ID associated with your user account. If you do not have these already, here is how you can generate a set of keys:

1. Sign in to the AWS Web Console at https://aws.amazon.com/.

2. Select the Identity and Access Management (IAM) service.

3. In the left-hand IAM menu, select Users.

4. Click on the Add User button.

5. On the next screen, enter a name for the user account then, in the ‘Select AWS access type’ section, select Programmatic access.

6. Click the Next button to assign permissions, then select Attach existing policies directly.

7. In the list of policies, find the PowerUserAccess and IAMFullAccess policies and tick the checkboxes next to them.

8. You can skip the remaining wizard steps. The final page will show the access key ID and show a link to reveal the secret key as shown in the figure below. Reveal the secret key and copy both keys somewhere.

Once you have the access keys, you may run the following command to save the keys to your local machine:

```nodejs
aws configure
```

#### Verification 

Check that your credentials are correctly configured by running the following command line:

```nodejs
aws sts get-caller-identity
```

If this command prints a result similar to the following, everything works correctly in the terminal provided above:

```nodejs
$ aws sts get-caller-identity
{
    "UserId": "111111111111",
    "Account": "222222222222",
    "Arn": "arn:aws:iam:1111111111:root"
}
```

# 4 Running AWS Services with Restricted User Accounts
 
## 4.1 Restricted privileges account

If you would like to set up an account with restricted privileges, the user account will need the following policies:

* `arn:aws:iam::aws:policy/AWSLambdaFullAccess`

* `arn:aws:iam::aws:policy/AmazonAPIGatewayAdministrator`

* `arn:aws:iam::aws:policy/IAMFullAccess`

### Access to CloudFormation

In addition, the user account will need access to CloudFormation. There are no standard AWS policies for this, so you will need to create a new policy and assign it to the user account. The JSON template below provides full access to all CloudFormation resources:

```nodejs
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudformation:*",
      "Resource": "*"
    }
  ]
}
```

Some companies restrict user accounts for developers, in which case you may need to ask your administrator to assign the policies mentioned.

If full access to IAM and CloudFormation is a problem, ask the administrator to create a separate sub-account for you in your AWS account organization (the administrator can do so from the AWS Organisations console). Each sub-account has completely isolated resources, so granting full access to a subaccount does not assign any privileges to important corporate resources.

## 4.2 Using a profile

AWS command-line tools can store multiple combinations of access keys on the same system. This is a convenient way to use separate access credentials for different projects or to reduce the chance of mistakes by restricting everyday usage to read-only access. A key combination is called a profile.

If your IT administrator creates a subaccount for experiments that is different from your main AWS account, you will most likely want to record the keys in a separate profile in order to easily switch between access combinations. If your account is managed by a company and the IT security department does not want to give you the required access to try out SAM, you can register a personal account with AWS and set it up as a separate profile.

### Setting up a profile 

You can set up a profile by adding the `--profile` option to the command for configuring access keys, followed by a profile name. For example, the following command will help you create a profile called `samdevelop`:


```nodejs
aws configure --profile samdevelop
```

To use a specific profile, add the `--profile` argument to all the AWS and SAM commands. For example, execute the following command to test whether the profile `samdevelop` is set up correctly:

```nodejs
aws sts get-caller-identity --profile samdevelop
```

To keep things simple, the process of profile setting will be omitted from the rest of the course. If you would like to use a separate profile, remember to add it to all the command line examples starting with `aws` or `sam`.






























 















