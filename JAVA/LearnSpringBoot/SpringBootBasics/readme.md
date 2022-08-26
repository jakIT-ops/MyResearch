# Creating a Spring Boot Project with Eclipse and Maven

### Introduction to Maven

Q : Why Maven?
You don’t want to store all the libraries in your project!

You want to tell I need A, B, C and you would want the tool to download the libraries and make them available to you.

That’s Maven. The tool which you use to manage the libraries.

If you need a new version of the library, you can change the version and your project is ready!

Also, You don’t need to worry about what libraries your library needs to work. For example, Spring might need other libaries - logging, xml etc.

Once you declare a dependency on Spring, Maven would download

* Spring

* And all dependencies of Spring

### Big Picture of Maven

Defining what Maven does is very difficult.

Every Day Developer does a lot of things

* Manages Dependencies

	* Web Layer (Spring MVC)

	* Data Layer (JPA - Hibernate) etc.

* Build a jar or a war or an ear

* Run the application locally

	* Tomcat or Jetty

* Deploy to a T environment

* Add new dependencies to a project

* Run Unit Tests

* Generate Projects

* Create Eclipse Workspace

### Maven Build Life Cycle

When we run “mvn clean install”, we are executing the complete maven build life cycle.

Build LifeCycle is a sequence of steps

* Validate

* Compile

* Test

* Package

* Integration Test

* Verify

* Install

* Deploy

### How does Maven Work?

Maven Repository contains all the jars indexed by artifact id and group id.

Once we add a dependency to our pom.xml, maven asks the maven repository for the jar dependencies giving group id and the artifact id as the input.

* Maven repository stores all the versions of all dependencies. JUnit 4.2,4.3,4.4

The jar dependencies are stored on your machine in a folder called maven local repository. All our projects would refer to the jars from the maven local repository.

> Local Repository : a temp folder on your machine where maven stores the jar and dependency files that are downloaded from Maven Repository.

#### Important Maven Commands

* mvn –version -> Find the maven version
* mvn compile -> compiles source files
* mvn test-compile -> compiles test files - one thing to observe is this also compiles source files
* mvn clean -> deletes target directory
* mvn test -> run unit tests
* mvn package -> creates a jar for the project
* help:effective-settings -> Debug Maven Settings
* help:effective-pom -> Look at the complete pom after all inheritances from parent poms are resolved
* dependency:tree -> Look at all the dependencies and transitive dependencies
* dependency:sources -> Download source code for all dependencies
* –debug -> Debug flag. Can be used with all the above commands


