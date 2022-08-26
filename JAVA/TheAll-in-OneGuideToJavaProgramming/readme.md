# Java Syntax and Conventions

## Java 5

<b>The following new features have been added to Java 5:</b>

* Generics

* Annotations

* More concise for loops

* Static imports

* Autoboxing/unboxing

* Enumerations

* Varargs

* Concurrency utilities in package `java.util.concurrent`

## Java 6 

### Changes in Java 6

Java 6 did not have as many big changes as Java 5, but it did add the following:

* `Web Services:` First-class support for writing XML web services.

* `Scripting:` The ability to plug in scripting engines (JavaScript, Ruby, and Groovy for example).

* `Java DB` (Apache Derby): It is co-bundled in the JRE.

* `JDBC 4.0:` It adds many feature additions like special support for XML as an SQL data type and better integration of Binary Large OBjects (BLOBs) and Character Large OBjects (CLOBs).

* More Desktop APIs: SwingWorker, JTable, and more

* Monitoring and Management: Jhat for forensic explorations of core dumps.

* Compiler Access: The compiler API opens up programmatic access to javac for in-process compilation of dynamically generated Java code.

* Override interface methods: The @Override annotation can be used to declare we’re overriding an interface method.

# Java 7 

The following features have been added to the Java language:

* Diamond operator

* Strings in switch

* Automatic resource management

* Improved exception handling

* Numbers with underscores

### Diamond operator

The Diamond operator simplifies the declaration of generic classes. The generic types are inferred from the definition of the field or variable.

```java
Map<String, List<Double>> nums = new HashMap<String, List<Double>> ();
```

For example, the above code can also be written in Java 7 as:

```
Map<String, List<Double>> nums = new HashMap <> ();
```

## JVM Benefits 

### New features in JVM

Java 7 adds some new features to the JVM, the language, and the runtime libraries.

The JVM has the following new features:

* `Serviceability features` (JRockit/hotspot convergence):

	* Java Mission Control (monitor, manage, profile)

	* Java Flight Recorder (profiling, problem analysis, debugging) (in progress)

* jdk introspection:

	* jcmd: The list running java processes.

	* jcmd <pid> GC.class_histogram: The size of classes.

Better garbage collection


### Performance benefits

Some of the performance benefits in the JVM and runtime libraries are as follows:

* Runtime compiler improvements.

* Sockets Direct Protocol (SDP)

* Java Class Libraries:

	* Avoid contention in Date: Changed from HashTable to ConcurrentHashMap.

	* BigDecimal improvements (CR 7013110).

* Crypto config. files updates, CR 7036252:

	* User land crypto for SPARC T4

	* Adler32 & CRC32 on T-series

* String(byte[], string) and String.getBytes(String) 2-3x performance.

* HotSpot JVM:

	* Updated native compilers: -XX:+UseNUMA on Java 7 (Linux kernel 2.6.19 or later; glibc 2.6.1).

	* Partial PermGen removal (full removal in JDK 8): Interned String moved to Java heap.

	* Default Hashtable table size is 1,009 increase size if needed -XX:StringTableSize = n.

	* Distinct class names:XX:+UnlockExperimentalVMOptions-XX:PredictedClassLoadCount=#.

* Client library updates (Nimbus Look&Feel; JLayer; translucent windows, Optimized 2d render- ing)

* JDBC 4.1 updates (allow Connection, ResultSet, and Statement objects be used in try-with-resources statement)

* JAXP 1.4.5 (Parsing) (bug fixes, conformance, security, performance)

* JAXB 2.2.3 (Binding)

* Asynchronous I/O in java.io for both sockes and files (uses native platform when available).

* x86 (intel) improved 14x over 5 processor releases (jdk5 jdk 6).

* JDK 7u4 faster than Java6 and JRockit.

# Idiomatic Java 8: Lambdas, Streams, and Dates

### What’s included?

As of publication, Java 8 is the de-facto standard version of Java. It is already being used in many production systems. So if we are currently using an older version of Java, it’s time to upgrade. Java 8 includes the following:

* Lambda expressions

* Method references

* Default Methods (Defender methods)

* A new Stream API

* Optional

* A new Date/Time API

* Nashorn, the new JavaScript engine

* Removal of the Permanent Generation

And more…

# Java 8 Miscellaneous

Java 8 has tons of new features. Here are some of them:

* java.util.Base64

* Cryptography upgrades (lots)

* JDBC 4.2

* Repeatable Annotations

* Annotations on types


# Advantages of Java 9

### Overview

Java 9 is the newest release of Java and includes Project Jigsaw, which represents a huge restructuring of the core JDK (Java Development Kit) as well as a new and improved way of defining code dependencies. This provides compile-time errors when dependencies are missing as opposed to runtime errors, which is a vast improvement for software development efficiency.

Java 9 includes the following key features:

* Language updates

* Support for Reactive Streams

* Modularity (Project Jigsaw)

* Java REPL (jshell)

As well as some additional lesser-known features:

* HTTP 2.0 support

* Unified JVM Logging

* UTF-8 Property Files

* TIFF Image I/O

* Unicode 8.0 support

### Language updates

Some small but important changes to the Java language are implemented in Java 9:

* `@SafeVargs` is now allowed on private methods.

* Effectively final variables can be used in try-with-resources.

* Diamond syntax allows for Anonymous classes in some cases.

* Underscore is no longer allowed as a variable name.

* Interfaces can now have private methods.

### Concurrency

Support for Reactive Streams has been added to the JDK. Several interfaces have been added in the java.util.concurrent.Flow class:

* Publisher<T>: A producer of items (and related control messages) received by Subscribers.

* Subscriber<T>: A receiver of messages.

* Processor<T,R>: A component that acts as both a Subscriber and Publisher.

* Subscription: Message control linking a Publisher and Subscriber.

No actual implementation is included in the JDK; however, several implementations already exist. Current notable implementations of this specification on the JVM and Reactive Streams are Project Reactor (which is integrated in Spring 5), Akka Streams, and RxJava.

## JShell 

### What is JShell?

JShell is a command-line read–eval–print loop (REPL) included in Java 9 that can be used to experiment and run small snippets of code.

To start JShell, simply type `jshell` at the command line.

It allows us to define variables and methods, and we can even reference methods that don’t exist yet and define them later.

# Java 10 - 17 

### A little history

Java 10 was released on March 20, 2018. Java 11 was released in September 2018. As Java 11 is the long-term service release (LTS), many developers may move directly from Java 8.

## Java 12 - 17: Features

### History

`Java 12` was released in March of 2019. The main new feature that was released in Java 12 was switch expressions (for example, the preview feature).

`Java 13` was released in September of 2019 and introduced multiline Strings as a preview.

`Java 14` was released in March of 2020 and includes record, pattern matching instanceof, and text blocks (as preview features).

`Java 15` was released in September of 2020 made text blocks enabled by default as a feature. It also includes sealed classes as a preview feature.

`Java 16` was released in March of 2021 and includes record and pattern matching for instanceof as included features.

`Java 17` is not yet released at the time of writing. Java 17 is the next LTS (Long Term Service) release of Java.

A preview feature means it must be enabled when starting the Java application at the java command using --enable-preview.

# Java EcoSystem

### Tools and libraries

This part covers tools and libraries that have been essential for Java development. It covers the use of Maven for building, Junit for testing, and some libraries, such as Logback, Hibernate, and Guava. Then it covers different ways to do concurrency in Java.

A huge part of the allure of Java is the vast wealth of open-source libraries and frameworks available in the language. There are multiple build tools, testing frameworks, and libraries to choose from.

Although we can’t cover all of them, this course will highlight some important ones that are essential to understanding the Java ecosystem. In addition, there are other languages built on top of the JVM since it is such a reliable, robust, and performant virtual machine. The course will also cover Groovy and Scala in a later section.

## Continuous Development and Testing

> “The purpose of automated testing is to enable change. Verifying correctness is just a nice side effect.” - Jeremy Norris

`Continuous software development` (also called Agile or Iterative development) is extremely popular nowadays and for a good reason. Automated tests (tests that run after every commit or every night) are a very important part of practising continuous software development. Generally, as a programmer, we should write tests to verify that our code is correct.

Testing is a huge subject. However, here, we will just give a short summary of modern testing in a Java/JVM environment.

### Definitions

The following are important terms and acronyms in software development:

`
Unit Test
`

Testing a single API call or some isolated code.

`
Integration Tests
`

Testing higher order code that requires a test harness, mocking, etc.

`Continuous Integration` Continuous Integration (CI) involves having a SCM, centralized build-system, continuous building , and many tests .
`
TDD
`
Test Driven Development (TDD) means writing tests before you start and while we write functional code.
`
BDD
`
Behavior-Driven Development (BDD) aims to help focus development on the delivery of prioritized, verifiable business value by providing a common vocabulary that spans the divide between business and technology.

## Testing and Frameworks

### Types of testing

The following are types of tests you should write:

* Acceptance tests: High-level tests that match the business requirements.

* Compatibility: Making sure things work together.

* Functional: Making sure codes work.

* Black box: Testing without knowing/thinking about what’s going on in the code.

* White box: Writing tests while keeping the code that’s being tested in mind.

* Gray box: This is a hybrid of black and white.

* Regression: Creating a test after finding a bug to make sure the bug does not reappear.

* Smoke: This involves a huge sampling of data.

* Load/Stress/Performance: Seeing how the system handles the load.

### Test frameworks

There are many different test frameworks for composing and running tests. The following are some of the best testing frameworks available for Java/JVM testing:

* JUnit: A programmer-oriented testing framework for Java.

* TestNG : A testing framework inspired from JUnit.

* Spock : A testing and specification framework for Java and Groovy applications.

* JBehave : A framework for BDD in Java

* easyb: Another framework for BDD with a Groovy DSL

* Arquillian : A component model for integration testing.

When evaluating test frameworks, the following features should be kept in mind:

* Tests should be portable to any supported container.

* Tests should be executable from both IDE and build tools.

* Tests should be easy to read and understand.

Mocking interfaces and classes go hand-in-hand with writing tests, but there are different frameworks available for mocking. The following are some great mocking frameworks:

* EasyMock

* Mockito

* JMock

# RxJava

RxJava is the open-source library for reactive programming in Java that is part of the ReactiveX project. In short, RxJava is an asynchronous framework for handling data using callbacks, including callbacks for errors and completion.


ReactiveX is based on reactive streams and includes implementations in several languages, including rxjs, RxRuby, RxSwift, RxPHP, RxGroovy, and many more. Reactive Streams provide an abstraction for highly concurrent, asynchronous applications with support for asynchronous handling of backpressure.

RxJava 2 was rebuilt to be compatible with the Reactive Streams specification and is preferable to RxJava 1.x since it is scheduled for end-of-life. There were many changes from version 1 to 2 that could be confusing. To avoid confusion, we will focus on RxJava 2.


### Parallel computing in Java#

If we tie a Flowable to one Scheduler as in the previous lesson, it will run in succession, but not in parallel. To run each calculation in parallel, we could use flatMap to break out each calculation into a separate Flowable as follows:

```java
public static List doParallelSquares() {
      List squares = new ArrayList();
      Flowable.range(1, 64)
         .flatMap(v -> //1
           Flowable.just(v)
              .subscribeOn(Schedulers.computation())
              .map(w -> w * w)
          )
          .doOnError(ex -> ex.printStackTrace()) //2
          .doOnComplete(() -> System.out.println("Completed")) //3
          .blockingSubscribe(squares::add);

     return squares;
}
```


1. Call flatMap with a lambda expression that takes in a value and returns another Flowable.
2. Call doOnError to handle errors that occur.
3. Call doOnComplete to execute something after a Flowable has been completed. This is only possible for flowable that have clear endings, such as Ranges.

We can write a test to verify our results using JUnit and Java 8+ in the following way:

```java
@Test
public void testDoParallelSquares() {
       List<Integer> result = demo.doParallelSquares()
            .stream().sorted().collect(Collectors.toList());

       assertArrayEquals(squares.toArray(), result.toArray());
}
```

# Other JVM Languages 

## Why Use Non-Java Languages?

Since the JVM runs Java byte-code and not actual Java-code, it is possible to compile different languages into byte-code to be run on the JVM. Also, some languages can be interpreted at runtime on top of the JVM.

There are many different reasons to use other languages on the JVM. We’re able to quickly change code in production or development and not have to recompile our codebase. This can make development faster and more flexible. Also, other languages have features that Java does not have that can increase developer productivity and make new things possible, such as closures, mixins, and meta-programming. Although these languages are completely different from Java, they still run on the JVM and can interoperate with Java-based libraries.

The trade-off when using these other languages tends to be performance. However, the value of developer time gained is generally much more than the cost of the performance lost. In addition, Java 7 has added some features to the JVM to enhance the performance of dynamic languages (invokedynamic).

### Java vs. JVM

Here’s a table of some popular JVM languages compared with features of Java:

| | Java | Groovy | Scala | Clojure | 
|:--- | ------ | ------ |-------| ------ |
|Typed? | Static | Either | Static | Dynamic |
| Closures? | No | YES | Yes | Yes |
| Mixins? | No | Yes | Yes | Yes |
| Meta-programming? | No | Yes | Yes | Yes |

# Gradle 

Gradle is a Groovy-based DSL for building projects. The Gradle website describes it as follows:

> “Gradle combines the power and flexibility of Ant with the dependency management and conventions of Maven into a more effective way to build. Powered by a Groovy DSL and packed with innovation, Gradle provides a declarative way to describe all kinds of builds through sensible defaults.” - gradle.org.

# RESTful

REST stands for Representational State Transfer. It was designed in a PhD dissertation and has gained some popularity as the new web-service standard. Many developers have praised it as a much better standard than SOAP (which we will not describe here).

## JAX-RS

### JAX-RS 1.0

JAX-RS 1.0 (the Java API for RESTful Web Services) was defined in JSR-311¹⁶⁴. It has many implementations, including the following:

* CXF: A merger between XFire and Celtix (an Open Source ESB, sponsored by IONA, and originally hosted at ObjectWeb).

* Jersey : The JAX-RS Reference Implementation from Oracle.

* RESTEasy : JBoss’s JAX-RS project.

JAX-RS defines a set of request method designators for the common HTTP methods: @GET, @POST, @PUT, @DELETE, and @HEAD.

When a resource class is instantiated, the values of fields and bean properties annotated with one of the following annotations are set according to the semantics of the annotation:

* `@MatrixParam:` Extracts the value of a URI matrix parameter.

* `@QueryParam:` Extracts the value of a URI query parameter.

* `@PathParam:` Extracts the value of a URI template parameter.

* `@CookieParam:` Extracts the value of a cookie.

* `@HeaderParam:` Extracts the value of a header.

* `@Context:` Injects an instance of a supported resource.

#### Gotcha’s

* If a subclass or implementation method has any JAX-RS annotations, then all of the annotations on the superclass or interface method are ignored.

* If you’re using Spring AOP on your web-service classes, this interferes with the ability of your JAX-RS library to get your annotations. Either all of your methods should be added to the interface or CGLIB proxies have to be explicitly enabled. Consult Spring AOP documentation for more details.

### JAX-RS 2.0

JAX-RS 2.0 adds a lot of new features to the REST API and comes with Java EE 7. It adds a client API, asynchronous processing for client and server, filters and interceptors, and some HATEOS (Hypermedia as the Engine of Application State) features.

#### Client API

JAX-RS 2.0 adds a client API to the standard. You can use the ClientFactory to Client and then a WebTarget. For example:
```java
// Default instance of client
Client client = ClientFactory.newClient();
// Create WebTarget instance base
WebTarget base = client.target("http://example.org/");
// Create new WebTarget instance hello and configure it
WebTarget hello = base.path("hello").path("{whom}");
hello.register(MyProvider.class);
```

Then, to execute on the Web Target, do the following:
```java
Response res = hello.pathParam("whom", "world").request("...").get();
This would result in a GET request on the URL http://example.org/hello/world
```

#### Asynchronous Processing

Asynchronous Processing and Asynchronous REST API calls were added as a first-class feature to JAX-RS. This allows the REST client to issue multiple requests in parallel and the server to handle such requests.

* Server API support

	* Offload I/O container threads

	* Suspendable client connection

	* Leverage Servlet 3.x async support (if available)

* Client API Support: request().async().get( callback ).

#### Filters & interceptors#

On the server-side, we have two different types of filters:

* `ContainerRequestFilter` runs before your JAX-RS resource method is invoked.

* `ContainerResponseFilter` runs after our resource method.

On the client side, we also have two types of filters: ClientRequestFilter and ClientResponseFilter. ClientRequestFilters run before our HTTP request is sent to the server. ClientResponseFilters run after a response is received, but before the response body is unmarshalled. Filters are useful for cross-cutting features, such as:

* Logging

* Security

* Compression

While filters modify request or response headers, interceptors deal with message bodies. Interceptors are executed in the same call stack as their corresponding reader or writer. There are two interceptor interfaces:

• `ReaderInterceptor` • `WriterInterceptor`


For example, Interceptors can be used to add digital signatures or “gzip” message bodies. Sometimes we want a filter or interceptor to only run for a specific resource method. We can do this with a @NameBinding annotation. Annotate a custom annotation with @NameBinding, and then apply that custom annotation to your filter and resource method.
```java
@NameBinding
public @interface MyFilterBinding {}

@MyFilterBinding
public class MyFilter implements ContainerRequestFilter {
   /* code... */
}
```

Then, in your RESTful Service:

```java
@Path
public class RestfulService {

     @GET
     @MyFilterBinding
     public String get() { /* code... */ }
```

#### HATEOS

JAX-RS 2.0 adheres more closely with REST principles and includes features of HATEOS.

It includes the following:

* ID’s and links

* (RFC-5988 Web Linking) Link types: Structural and Transitional

* Use `@Produces` to define what is returned:

```java
@GET
@Produces("text/plain", "text/html")
public Widget getWidget();
```

# MicroService and Clouds

### What are microservices?

The idea behind microservices is to break up a monolithic application into the smallest possible parts. The advantages include the ability to independently improve and deploy each service, have different technologies for each service, and reduce the number of resources we need to provision for large applications.

Although microservices have several advantages, nothing comes for free and there are some difficulties. There is overhead associated with managing multiple services, managing multiple deployments, integrating multiple versions of microservices together, and communication between the microservices. Multiple solutions exist for handling each of these difficulties. For many, the advantages outweigh the disadvantages.

### OSS

There is a lot of existing open-source software to assist with microservices. Here are some of them worth learning more about:

* Netflix OSS

* Spring Cloud

* Micronaut

## JVM Clouds

Cloud is a much-hyped term, but it boils down to the natural progression of services supporting web development. As the internet economy grows, so do the services supporting that economy. The size of the economy running on JVM-supported web development is huge and ever-expanding.

Here are just some of the best JVM PaaS (Platform as a Service) vendors (in alphabetical order):

* Amazon Web Services

* CloudFoundry

* Google Cloud Platform

* Heroku

* Jelastic

# Spark

### What is Spark?

Spark is a simple web framework for easily creating web applications in Java 8.

It has a really simple and terse syntax and is best used for quick development of simple web applications or web services.

Unlike many other web frameworks, Spark is super small and so it requires very little memory to run and has a fast startup time. At the same time, it has support for sessions, cookies, error handling, web-sockets, serving static files, gzip, and more.

It runs on an embedded Jetty web server when running standalone. Otherwise you can run it in any standard Java application web server, such as Tomcat







































