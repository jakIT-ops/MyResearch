## An analogy to explain vulnerabilities

Let’s start with a knock-knock joke as an example.

ROMAN: Knock knock.
COMPUTER: Who’s there?
ROMAN: I’ll give Roman $1,000,000.
COMPUTER: I’ll give Roman $1,000,000 w—
ROMAN: Ha! You said you’ll give me $1,000,000! Pay up!
COMPUTER: Pays Roman $1,000,000

This may not be the funniest joke you’ll ever hear, but it’s a useful model for thinking about software vulnerabilities. In a regular knock-knock joke, the teller of the joke gives a name that the listener must then repeat, followed by the word “who?” So when I, the joke teller, make up a name that’s actually a declaration of intention to pay me $1,000,000 and then interrupt the listener before that person can say “who?” it sounds like the listener has agreed to pay me $1,000,000. Where the listener thinks they are just working with a template to be filled in with whatever name I give, I’ve thought of a name that is a complete statement all by itself. Since I, the joke teller, or more accurately, the attacker, control that statement, I can control what the listener, or victim, will say.

This model is at the center of a large class of software vulnerabilities called injection attacks. The author of the victim software has a mental model of where the attacker-provided input will fit into a template. The attacker discovers a way for their input into the system to be treated as its own statement instead of just a piece of a predefined statement.


# 1. Additional Defenses as a Mitigation Againsst Future Mistakes

## Prepared statements do not cover it all

Proper use of prepared statements is our primary defense against SQL injection. Prepared statements are great, but we have to remember to use them every time we write code that touches SQL; we’re never “done” with applying this defense. And if we’re building complex, dynamic SQL statements with user input in parts of the SQL that aren’t parameterizable, we need to exercise a great deal of caution in many places in the codebase. If we’re sloppy in just one of those places, we can wind up leaving the door open to future SQL injection.

## Access control

It would be great if we could complete a one-time task that would protect us throughout future development. Unfortunately, we don’t have anything quite that powerful, but proper use of database permissions can get us part of the way there. In theory, we could have a single database user for each table that we want to work with. In practice, this is unlikely to be effective except in very small applications. There are likely to be a large number of tables in an application. And some interactions involve using multiple tables in a single statement. If the number of tables doesn’t get you, the number of combinations of tables will.

## Dedicated databases

While it isn’t worthwhile to introduce a dedicated database account for every table, it can be worthwhile to introduce them for particularly sensitive tables, such as audit tables or tables that contain passwords. It would be unfortunate if SQL injection in some random part of your application allowed an attacker to change admin passwords or cover their tracks by deleting audit records.

# 2. Introduction to Cross-Site Scripting (XSS)

## Introduction

We’ve seen the knock-knock joke principle applied to SQL (SQL injection). Let’s take a look at attacks using that same principle when applied to the HTML and JavaScript in a web page. We call this attack cross-site scripting (or XSS for short) if the attack injects JavaScript. We call it DOM injection if it injects regular HTML.

# 3. Defenses against XSS

## HTML encoding as defense

Now that we see how HTML encoding works, we can see how we can use this as a defense against HTML injection and XSS. Whenever we’re building up HTML as part of our response to a web browser, if we ever concatenate in user-controlled data, we need to HTML-encode it first. That way, even if an attacker tries to sneak JavaScript into one of our responses, we’ll encode it first and the browser will just display JavaScript source code to the user instead of executing attacker-controlled JavaScript.


## Handling attacker-controlled data in other contexts

Sometimes XSS payloads don’t look much like textbook XSS payloads if they’re built on top of JavaScript frameworks like AngularJS. For more details on Angular-specific attacks, see the excellent article “XSS without HTML: Client-Side Template Injection with AngularJS” by Gareth Heyes.

XSS by way of AngularJS expression injection doesn’t need < or >, so traditional web framework escaping doesn’t help. In general, you shouldn’t need to allow dynamic content inside of a dom element that’s decorated with the ng-app attribute. But if for some strange reason you do, be sure to encode the {{ and }} so that attackers can’t inject an AngularJS expression.

In summary, the way to prevent XSS is to restrict user-controlled data in as few kinds of places as possible in a web page. Keep user-controlled input out of dom elements decorated with the ng-app attribute that marks the start of an Angular JS application. And keep user-controlled data out of JavaScript. If you can do this and keep user-controlled data between HTML tags, then you can definitely prevent XSS by making sure to HTML-encode all user-controlled data.

# 4. Misconfiguration

Attackers are opportunistic. They won’t bother with a sophisticated attack where a simple one will do, and seeking out and exploiting misconfigured systems is one of the simplest attacks there is.

We need to develop the capabilities for ongoing monitoring of our systems to make sure we haven’t made the kinds of configuration mistakes that will open the door for easy attacks. The specifics of how you do this will vary significantly depending on the exact technologies you use in your organization. We’ll take a look at some of the most common misconfigurations and some tools to detect them. Even if you don’t use these specific tools, these examples should give you an idea of the kinds of mistakes you’ll want to be able to find

## Open S3 buckets

Amazon offers a popular storage service called Simple Storage Service, or S3 for short. S3 is a large-scale key-value storage service that lets users store file-like “objects” inside of “buckets.” A bucket can hold an arbitrary number of objects, and an object can range in size up to 5TB. Behind the scenes, S3 is a highly durable storage service that automatically distributes data across multiple physical facilities. Amazon offers a lot of tools as well, including tools for big data analysis that integrate natively with S3.

It’s really neat. It also seems to be really easy to misconfigure.

A quick Google search for “S3 breach” will show many high-profile instances of misconfigured S3 buckets that left sensitive data open for the world to see. No need for fancy attacks or cryptographic breakthroughs if the data isn’t protected in the first place.

One particularly easy S3 mistake to make involves something called the Authenticated Users group. AWS permissions are based on group membership. So, when setting up permissions, an administrator will typically create groups that represent the organization and assign permissions to those groups. The Authenticated Users group is a predefined group in AWS. It would be easy to look at the name and think that it describes the group of people that are authenticated users of one’s own organization. That is not what that group means, however. Anyone who is logged into AWS as a part of any organization is automatically a member of the Authenticated Users group. If we look at the relevant documentation we’ll see this:

# 5. Default Passwords & Credentials

## Default passwords

Default passwords are another kind of misconfiguration that saves attackers a lot of time and effort. They’re easy to exploit and easy to detect—just the kind of thing that attackers love. So we need to find them first. We can leverage the network inventory work we did in chapter 1 to give us a starting point for where to look. We’ll also want to include network infrastructure like switches. We’ll want to pay particular attention to anything that’s exposed to the internet.

As was the case with defenses against SQL injection, our defense against this kind of misconfiguration can be layered. The first layer of the defense is to add to our provisioning checklist to make sure to not use default passwords when provisioning new services.

Beyond that, we can look into scanning our network for default passwords. This second layer is highly specific to your network. You won’t have time to exhaustively scan everything on your network. You’ll need to use your judgment on where to focus your efforts. You may get a good return on looking into crusty old infrastructure that doesn’t have clear ownership. And don’t overlook networked printers. Networked printers can have capabilities like emailing or connecting to an Active Directory server. If you can get administrative access to a printer by using default credentials, you may be able to see the email or Active Directory credentials that enable those capabilities.

## Keep credentials out of source control

Checking credentials into a public GitHub repo is a common mistake. In the eyes of an attacker, leaked credentials are just as good as default credentials.

Even if we only use private source control servers, we still don’t want to check credentials into source control. We don’t want to have to do a build in order to change credentials. Also, putting credentials into source control makes it hard to introduce tiers of access. For instance, you may not want junior team members or third-party contractors to be able to see or change production credentials. Some organizational models call for a separation between those who write code and those who have access to run or deploy that code in production.

# 6. Jenkins & Public-Facing Servers

## Jenkins

But Jenkins has a common misconfiguration that merits special mention. Jenkins instances are often started with insecure settings that allow for unauthenticated execution of commands in a scripting language called Groovy. Groovy scripts can execute arbitrary shell commands. So a common attack is to scan the network for misconfigured Jenkins servers, use the Groovy Scripting Console to dump passwords from the Jenkins server, then use those passwords to compromise other servers on the network.

## Public-facing servers

We’re going to look at one last source of vulnerabilities in this chapter—long-forgotten public-facing servers. It’s easy to forget to shut down public-facing servers that aren’t used anymore. This mistake is even easier to make if you use a cloud hosting service. We’ll address the problem of forgotten or unpatched servers exposed to the internet similar to the way we’ve addressed other vulnerabilities in this chapter.

First, we’ll do a one-time cleanup effort. Once we’ve addressed the problems of today, we’ll add automation to make sure we don’t reintroduce this problem again in the future.

Ideally, before you kick off a one-time cleanup effort, you already know exactly what servers you have exposed to the internet. Whether that’s the case or not, it’s worthwhile to examine your organization using a public tool. This can either serve as a first census or a double-check on your existing practices around maintaining an up-to-date inventory of your public-facing servers.

The first time you do a check like this can be pretty eye-opening. You may be surprised to see how many public servers you actually maintain. You may also be surprised about how up-to-date the software running on those servers is. If these scans reveal version numbers of server-side software, be sure to google for CVEs for that software. We covered CVEs in What Is a CVE?.























