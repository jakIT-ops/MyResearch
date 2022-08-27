# 1. Introduction

## Even perfectly written code entails risk

Let’s pretend that every piece of software that your organization ever writes from here on out is completely perfect. All of your developers are attentive and well trained. Your developers will never write code with a logic error, SQL injection, or cross-site scripting vulnerability. (Don’t worry if you don’t know what these vulnerabilities are yet.)

## Patching is time-critical

What’s worse, this state of ignorance is time-critical. Once a vulnerability is made public, security researchers and criminals alike start writing tools to scan for vulnerable computers.

Scanning tools allow attackers to find your vulnerable public systems even if they’d never had any reason to attack you before. The internet makes every public-facing computer equally close. Even if the technical details of a vulnerability are not made public and only a patch is made available, motivated attackers can look at what’s changed to try to find likely attack vectors.

# 2. Upgrading Third-Party Libraries and Software

## Good patching practices

When defending ourselves against the risks implicit in third-party libraries, we need to know what third-party software we use. It takes a surprisingly large amount of effort to discover this.

Once we know what’s in use, we need the ability to quickly upgrade any of the third-party libraries and any software deployed in our organization.

What’s more, we need to be able to test these upgrades so that we can be confident that the upgrade won’t break anything.

We’ll want to automate this as much as possible because we need to do it often, and we need to do it correctly. Infrequently done manual upgrades are unlikely to work when under extreme stress and at the hurried pace likely to accompany a critical, newly discovered vulnerability. Finally, we need to be able to do it on short notice because we don’t know when we’ll need to upgrade.

## Dependencies need to be current

In order to be ready to upgrade, we need to be relatively current with our dependencies. We can’t remain on old, unsupported versions of software, even if the old versions are functionally sufficient.

Being out-of-date is likely to cause trouble when a vulnerability is found. If we’re a couple of years out-of-date on a library and a vulnerability is announced in that library, we risk that the fix for that vulnerability will only be available in the latest version of the library.

# 3. A closer Look at Patching

Patching is the broccoli and spinach and push-ups of security. It’s not glamorous. You won’t get to do a talk at a prestigious conference from it. You’ll never be finished, either. But it’s one of the fundamental practices you need in place to keep the bad guys out.

Patching is the ongoing practice of the following:

1. Looking at what software you have in place

2. Researching what vulnerabilities have been discovered in that software

3. Upgrading the vulnerable software to secure versions

4. Testing to make sure that the new versions work

## Patching and the Equifax breach

One of the most widely discussed breaches of 2017 was the Equifax breach, in which hackers accessed the sensitive personal information of approximately 145.5 million Americans. We can learn a lot about the importance of patch management by looking at this breach. Equifax has shared a lot of information related to the breach in its September 15, 2017, press release, including a timeline. Equifax has determined that the cause of the breach was a vulnerability in Apache Struts. This vulnerability allowed attackers to run arbitrary commands on the vulnerable server with the privileges of the Apache process itself.

## Delay in patching

The second thing that jumps out is the delay in patching. Equifax was more than two months behind on patching at the time of the initial attack and more than four and a half months behind on patching when it finally shut down the affected site. That’s a long time to be out-of-date.

# 4. Library Inventory

## Why have an inventory?

On the other hand, if you have an accurate inventory of the software you use (or at least a well-established process for finding it), you’ll be able to start your response much sooner. If you’re lucky, you’ll know right away that you’re not impacted. If you’re less lucky, you’ll be able to jump into remediation right away rather than wasting valuable time figuring out that you’re impacte

## The inventory process

If you’re a developer, you’ll know how library dependencies are managed in your organization. If you’re not a developer, you’ll need to work with the developers in your organization to carry this out. The specifics of how to do this vary significantly based on what languages and build tools you use, but the idea is the same regardless. We need to do the following:

1. Find the supported versions of your code using source control.

2. Find the direct library dependencies your code has.

3. Find the transitive library dependencies your code has—that is, find the dependencies of your dependencies.

Getting your third-party libraries under control is likely to be a lengthy process. You may need to address it in stages. You may also have to put in a fair amount of effort to find all of the codebases your organization has.

## Source control

You’ll have to get comfortable with your source control system. At the very least, you’ll need to be able to look at the latest production version of your code. If you support multiple, older versions of your code, you’ll need to be able to look at each of the older supported versions as well.

The specifics of how to look at the relevant version of your code via source control are beyond the scope of this course. If you need more information on how to work with your source control system, excellent guides are available for CVS, Subversion, and Git online.

# 5. Dependency Management: Python

## Requirements.txt

Python has multiple ways of managing third-party dependencies. We’re going to take a look at managing dependencies using requirements.txt. <b>Requirements.txt</b> may spell out transitive dependencies, but it doesn’t have to. So we’ll start with a discussion of requirements.txt and what it can tell us. We’ll finish up with two approaches we can use if we don’t have all our transitive dependencies spelled out for us.

## Finding dependencies in an installed instance

If we investigate a Python project that doesn’t give us exact version numbers for each dependency, we don’t have a way to find out the version numbers that are used in practice just by looking at the files checked into source control. We’ll have to look at a deployed instance instead. The specifics of this will depend on the deployment environment and the install process used.

One option for investigating the deployed libraries is to use pip. If pip is installed, running the command pip freeze (pip3 freeze if you are using python3):

```py
pip3 freeze
```

# 6. Dependency Management: JavaScript

There are many different ways to track JavaScript dependencies. We’ll cover npm because it’s one of the most popular package managers. As was the case with Python dependency management, you’ll need to talk to your developers to find out how they’re managing dependencies if you’re not a JavaScript developer yourself.

## Package.json

Package.json is npm’s configuration file. It specifies dependencies in addition to many other facets of a package. It’s similar to Python’s requirements.txt in that it lists direct dependencies but does not list transitive dependencies.

In order to find transitive dependencies, you need to use npm. As was the case with Python, you’ll need to install your software in order to find transitive dependencies. They aren’t listed in your package’s package.json; they are calculated by looking at the package.json for each package listed in your package.json. Your best bet will be to work with your developers to install your package and then use npm list to show a tree of the dependencies. You can expect output like the following from npm list:

```json
├─┬ my-app@1.0.0
│ ├─┬ my-dependency1@2.7.4
│ │ ├── thing2@1.2.3
│ │ ├── otherthing@2.3.4
│ │ ├── thing3@3.4.5
│ ├─┬ my-dependency2@4.5.6
│ │ └─┬ andanotherthing@5.6.7
│ │   ├── thing2@6.7.8
```

That’s useful, but we still need to go find which of those libraries have known vulnerabilities. Fortunately, npm gives us a way to do that—npm audit. Running npm audit produces output like this:

```json
                       === npm audit security report ===
# Run  npm install express@4.16.4  to resolve 2 vulnerabilities
SEMVER WARNING: Recommended action is a potentially breaking change
│ Moderate       | No Charset in Content-Type Header     |
│ Package        | express                               |
│ Dependency of  | express                               |
│ Path           | express                               |
│ More info      |  https://nodesecurity.io/advisories/8 |

│ Low            | methodOverride Middleware Reflected Cross-Site Scripting  |
│ Package        | connect                                                   |
│ Dependency of  | express                                                   |
│ Path           | express > connect                                         |
│ More info      | https://nodesecurity.io/advisories/3                      |
found 2 vulnerabilities (1 low, 1 moderate) in 4 scanned packages
  2 vulnerabilities require semver-major dependency updates.
```

# 7. Automating Vulnerability Detection

## OWASP Dependency-Check

OWASP has a free, open-source tool called Dependency-Check that can help automate the detection of vulnerable third-party libraries. This tool supports Java and .NET, with experimental support for Ruby, Node.js, Python, and C/C++ codebases. One of the nice features of this tool is that it can parse project files that you probably already use for managing your builds, such as pom.xml files in Java codebases and .nuspec files in .NET codebases. So it leverages the work you have already done in order to figure out your dependencies: you do not have to map out your dependencies specifically for the tool. Once it has parsed out the dependencies, it queries the CVE database (which we discuss in What Is a CVE?) to see if any of the libraries you use have published vulnerabilities. This tool is meant to run during your build process. That way, you can fail builds that use vulnerable libraries and stop vulnerable libraries from even making it into your test environments.

## Detecting vulnerable libraries in your source repository

There are also commercial solutions that integrate more closely with your source control and build artefact repositories. For some organizations, this may be an easier point at which to automate library vulnerability detection.

# 8. Network Inventory

## Introduction

Now that we know all of the libraries we’re dependent on in our codebase, we need to take an inventory of all the networked software that’s running on our network. All the reasons we had for needing a library inventory apply here. Ideally, every server and piece of networked software on your network is already inventoried and automatically patched. It is likely, however, that the team responsible for this (maybe you!) is overworked and doesn’t keep an updated list of everything that’s been deployed.

## Tools

A lot of tools can help you with this task. Some of these tools are commercial and some are open source. The important thing isn’t the exact tool(s) that you use for this job. The important thing is that you find tools that you’re comfortable with and that you can bring into your workflow. In the interest of accessibility—and to keep the examples within everyone’s budget—we’ll look at an open-source tool.

There’s a second reason we start with an open-source–scanning tool. If you don’t have a diligent patching program in place already, you don’t need to spend big money on a commercial scanning tool. Instead, you can put a Post-it on your mirror that reads, “You are vulnerable because your software is out-of-date,” send me a check for $10,000, and pocket the difference. Jokes aside, those scanning tools have their place; but if you don’t have a patching process in place, rest assured that you have vulnerabilities everywhere.

# 9. Nmap

We’ll start our discussion of network inventorying with Nmap. This is the simplest, easiest-to-install option we have. Nmap is a versatile open-source network-scanning tool. We’ll just cover the basics of using it for putting together a network inventory.

Nmap can be installed on Linux or Mac by using the standard package managers. The Nmap maintainers also provide Windows binaries. The Nmap website provides detailed installation and usage instructions, and it tells you where you can buy the printed Nmap book.

Nmap uses unauthenticated scans to give us a coarse-grained picture of what’s on our network. We’ll use Nmap to detect three things about our network:

1. What machines are on our network

2. What ports are open on those machines

3. What operating systems are running on those machines

The first two are fairly obvious. If a computer is on our network, it will generally respond to pings and the like. If a machine is listening on a given port, it will respond to SYN packets.

Detecting the operating system is less straightforward. Nmap can make some guesses about what operating system is running on another computer based on how that computer responds to specially crafted, nonstandard network traffic. It’s only a guess, not a guarantee. But even guesses can be useful while we’re trying to put together a network inventory.

##Getting familiar with normal traffic

Another benefit of this kind of scan is that it will help us develop an intuition for what kinds of machines and what kinds of traffic are normal for our network. Going back to our example of scanning our accounting department’s subnet, if we see an HTTP server running on an accountant’s workstation, that should grab our attention. Accountants generally aren’t interested in installing web servers. If one is running on an accountant’s workstation, that could be a sign of malware, so talk to the person who uses that workstation and find out if it’s supposed to be there. If it is supposed to be there, congratulations! You have a new piece of software to add to your network inventory. If this web server is not supposed to be there, however, congratulations! You found something that shouldn’t be there. You’ll need to decide how to respond to this incident.

##Application

Now that we have Nmap installed and know what we hope to learn from running it, let’s see how to use it. Nmap is a command-line tool, so we’ll run it from a shell such as bash. Let’s start by running nmap --help to make sure we’ve installed it correctly. Nmap’s help output is pretty verbose. You should see something like the following:

```bash
$ nmap --help
Nmap 7.60 ( https://nmap.org )
Usage: nmap [Scan Type(s)] [Options] {target specification} TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
SEE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
```

# 10. OpenVAS

## Introduction

Another open-source tool you can use to create an inventory of the software installed on the computers in your network is OpenVAS. OpenVAS will scan your network, store the results of the scan in a database, and make the results available via a web interface. The OpenVAS install is slightly more involved than the Nmap install, but it has a UI and can persist data so that you can see how your network has changed between scans.

To start building your inventory of the software running on your network, use OpenVAS in unauthenticated mode. In this mode, OpenVAS is just another program on a computer on your network. It doesn’t have credentials that allow it to log into computers on your network to find what’s installed. It just scans all the IP addresses you tell it to scan. When it finds a computer, it checks for open ports and tries to discover as much as it can about the services running on those ports. Because it runs without any special privileges or credentials, it’s not finding anything an attacker on your network could not find. 

## Limitations

It’s important to note the limitations of banner grabbing. We’re entirely reliant on the server to opt in to accurately disclose what software and version it’s running. The server doesn’t have to disclose this information at all, so we may wind up with limited information when banner grabbing.

Additionally, banner grabbing will only provide coarse-grained information about what’s installed on a server. In the case of the Apache server earlier, we learn the version of Apache that’s installed, but we don’t learn versions of any of the other software or operating system patches that are installed.

Because of these limitations, sometimes authenticated scans are more appropriate. In an authenticated scan, you provide credentials for OpenVAS to use to log in to each server and perform a more detailed scan. With this elevated level of access, OpenVAS will be able to report on misconfigurations and known vulnerabilities in all the software installed on each machine, not just the software that’s listening for incoming network connections. The downside to this is that the OpenVAS server will have privileged access to all of your servers. If the OpenVAS server is ever compromised, then the attackers will have privileged access to every computer on your network. You won’t want to use authenticated scans until you have solid monitoring and service account password rotation practices in place, at a minimum.

## Shodan and Censys

It’s surprisingly easy to accidentally leave computers exposed to the internet. The rise of cloud-hosting services like AWS, Azure, and Google Cloud Platform make this even easier. So be sure to use the administrative interface of any cloud services you use to add to the inventory of machines you need to scan. Additionally, use a service like Shodan or Censys to scan for machines or services you may have overlooked. Both Shodan and Censys scan the full IP4 address space of the internet on a regular basis to record what services are running. They then let you search through that data. Experiment to see what you can find about your organization.

# 11. Patching Windows

## Windows software update services

Since Windows is so prevalent, let’s look at Microsoft’s patching solution. Microsoft has a service called the Windows Software Update Services, or WSUS for short, that helps administrators manage the patching process for all the computers in a domain. With WSUS, you can push updates for Microsoft software to all the workstations in your domain.

## Automatic deployment

You should have an automatic deployment of patches enforced at the Windows domain level.

## Testing

You’ll want some level of testing of patches. Ideally, this would take the form of an automated test environment, where Windows computers go through the motions of simulating commonly performed actions. More realistically, this would take the form of delaying most patches a week or two in the hopes that this will give Microsoft more time to shake out any problems in the patching. Then, patches would be deployed in waves so that even if a patch breaks something, it will only impact a portion of your fleet, instead of every Windows computer in your organization.

# 12. Testing Your Patches

The answer is going to be a little different for every organization. You’ll have to decide how comfortable you are with a given vendor’s track record of providing stable patches. The answer will also depend on the criticality of the system to be patched, the severity of the vulnerability, and the availability of workarounds for the vulnerability. These variables are outside of your control. The only thing that you can do to speed up the deployment of a patch is to have a set of tests ready to give you a quick yes or no on the question of whether the patch will break things.

## Creating comprehensive tests

A set of tests that covers every piece of software in your organization will always be a work in progress. There is so much third-party software, and there are so many demands on our time other than patching. But even partial test coverage is valuable. If dedicated tests for each piece of third-party code aren’t an option right now, you can still get value from integration tests that run against a fully running instance of your program. You may be able to test multiple libraries as well as your own code in a single integration test. Integration tests are coarser-grained than unit tests. This is nice because you can cover more at once. But this is also problematic because when a test breaks you’ll have more places to look to find the culprit.

## Manual testing for time crunches

If time is really tight, you may be stuck with manual tests. There’s nothing wrong with manual tests. Just make sure that the tests are documented so that anyone on your team can perform the test. Just like we saw with searching for patches, there’s great value in spreading the knowledge around the team, breaking down knowledge silos, and gaining multiple perspectives into this work. You may find that tests “mature” from manual to automated over time. It’s entirely reasonable to start with manual testing and only automate if a software product needs to be updated often.






















