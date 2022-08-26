# 1. Spring Interview Questions

https://www.springboottutorial.com/spring-interview-questions

# 2. Spring Boot Interview Questions

https://www.springboottutorial.com/spring-boot-interview-questions


### Q : What is the need for a Component Scan?

> If you understand component scan, you understand Spring.

The first step of defining Spring Beans is by adding the right annotation - @Component or @Service or @Repository.

However, Spring does not know about the bean unless it knows where to search for it. This part of “telling Spring where to search” is called a Component Scan. You define the packages that have to be scanned.

Once you define a Component Scan for a package, Spring would search the package and all its sub packages for components.

### Q : How do you define a Component Scan with Spring Boot?

Consider the class below:

```java
package com.in28minutes.springboot.basics.springbootin10steps;

@SpringBootApplication
public class SpringbootIn10StepsApplication {

	public static void main(String[] args) {
		ApplicationContext applicationContext = 
				SpringApplication.run(SpringbootIn10StepsApplication.class, args);
```

`@SpringBootApplication` is defined on `SpringbootIn10StepsApplication class` which is package `com.in28minutes.springboot.basics.springbootin10steps.`

`@SpringBootApplication` defines an automatic component scan on `package com.in28minutes.springboot.basics.springbootin10steps.`

You are fine if all your components are defined in the above package or a sub-package.

However, let’s say one of the components is defined in a package `com.in28minutes.springboot.somethingelse`

In this case, you would need add the new package into component scan.

Two Options

* Define @ComponentScan(“com.in28minutes.springboot”) - This would scan the entire parent tree of com.in28minutes.springboot.

* Or Define two specific Component Scans by using an array.

	* @ComponentScan({“com.in28minutes.springboot.basics.springbootin10steps”,”com.in28minutes.springboot.somethingelse”})

### Q : What is the difference between @Component and @ComponentScan?

@Component and @ComponentScan are for different purposes.

* @Component indicates that a class might be a candidate for creating a bean. Its like putting a hand up.

* @ComponentScan is searching packages for Components. Trying to find out who all put their hands up.

### Q : What is the use of an @Bean annotation?

Within a Spring Configuration Class , @Bean is used to define beans with custom configuration. You define the beans to be created!

### Q : What is the difference between @Bean and @Component?

Here’s a quick fire answer

* @Bean is used in Spring Configuration Files and Classes. It is used to directly instantiate or configure spring beans.

* @Component is used with everything that you want Spring to manage. When Spring sees @Component, it creates a bean for you!

### Q : What is the difference between @Component, @Service and @Repository annotations?

At the core, all of these define spring beans. However, you can further classify them based on the layer you are using them.

* @Component - Generic Component

* @Repository - encapsulating storage, retrieval, and search behavior typically from a relational database

* @Service - Business Service Facade

* @Controller - Controller in MVC pattern

In addition, these can be used at later point to add additional behaviour using AOP, for example.

* For example, in case of @Repository, Spring automatically wires in JDBC Exception translation features.
By using a specific annotation, you are giving more information to the framework about your intentions.

By using a specific annotation, you are giving more information to the framework about your intentions.

## Q : Can we use @Component annotation instead of @Service for Business Services?

Heres an extract from spring documentation. Since we were creating a business layer service, we used @Service.

> “@Component serves as a generic stereotype for any Spring-managed component; whereas, @Repository, @Service, and @Controller serve as specializations of @Component for more specific use cases (e.g., in the persistence, service, and presentation layers, respectively). What this means is that you can annotate your component classes with @Component, but by annotating them with @Repository, @Service, or @Controller instead, your classes are more properly suited for processing by tools or associating with aspects. For example, these stereotype annotations make ideal targets for pointcuts. Of course, it is also possible that @Repository, @Service, and @Controller may carry additional semantics in future releases of the Spring Framework. Thus, if you are making a decision between using @Component or @Service for your service layer, @Service is clearly the better choice. Similarly, as stated above, @Repository is already supported as a marker for automatic exception translation in your persistence layer.”

### Q : What is the difference between web.xml and the Spring Context - servlet.xml?

Short Answer:

* web.xml - Java EE Web application Standard. Meta data and configuration of any Java EE compliant web application is stored in web.xml.

* todo-servlet.xml - Spring Configuration file. Specific to Spring Framework.

### Q : Should we use XML or Annotation based wiring?

Which is better depends on a) context b) preference of the team.

If the configuration is specific to a bean, that is part of the current project code base - for example @Service, @Component, @Autowired - I prefer annotations.

However, when it comes to some application related configuration or a common configuration example @ComponentScan, I do not really have a preference. I would leave it to the team. However, I would definitely want the entire team to discuss and agree what they prefer.

### Q : Can we do autowiring with Non Setter and Non Constructor Methods?

Yes you can.

@Autowired annotation can be used with constructor, setter method or just any other method. Whenever Spring finds @Autowired annotation it will try to find beans matching to method parameters and will invoke that method. If multiple methods (setter or non-setter) have @Autowiredannotation, all will be invoked by Spring after bean instantiation.

Whenever you use an @Autowired on a method in the bean, it will be called after bean instantiation. So, this method would be called and Spring would auto wire the matching objects from the Spring Context.

Here’s a recommended reading:

* http://stackoverflow.com/questions/30188262/spring-autowired-for-setter-methods-vs-non-setter-methods

### Q : Where should we use Checked Exceptions?

I’ve a simple philosophy!

If you can do something about an Exception other than showing an error page to the user, then consider Checked Exceptions. You want the consumer of the method to do something about that exception!

In all other scenarios where there is nothing a programmer can do - other than showing an error page - use Unchecked exceptions.

I love keeping exception handling code to a bare minimum!

That’s what Spring enables by converting most Checked exceptions into Runtime (also called Unchecked) exceptions.

### Q : What is the difference between Cross Cutting Concerns and AOP?

A quick fire answer

* Cross Cutting Concerns are features or functionality that you would need in multiple layers - logging, performance management, security etc.

* AOP is one of the preferred approaches to implement Cross Cutting Concerns.

### Q : What is difference between IOC and Application Context?

IOC is a concept - Inversion of Control. Instead of the programmer injecting dependencies, the framework takes the responsibility of auto wiring.

ApplicationContext is the Spring implementation of IOC.

Bean Factory is the basic version of IOC Container.

Application Context adds in all the features that are typically needed by enterprise applications.

### Q : When @Around aspect is introduced the value returned by@AfterReturning is lost. Why is this happening?

The around method should return an Object - value returned by joinpoint.proceed().

```xml
@Around("com.in28minutes.spring.aop.springaop.aspect.CommonJoinPointConfig.trackTimeAnnotation()")
public Object around(ProceedingJoinPoint joinPoint) throws Throwable{
    long startTime = System.currentTimeMillis();
 
    Object retVal = joinPoint.proceed();
 
    long timeTaken = System.currentTimeMillis() - startTime;
    logger.info("Time taken by {} is equal to {}",joinPoint, timeTaken);
 
    return retVal;
}
```

### Q : How do you decide which autowiring type to use when there are multiple matching beans - @Primary or @Qualifier?

If there is a default bean (a bean you prefer over all others) that you want to use most of the times, then go for @Primary and use @Qualifier for non-default scenarios.

If all of the beans have same priority, we would go with @Qualifier always.

If you want to select a bean at runtime, thats business logic - Not auto wiring.

You would need to create a separate class for Selector which has both the sorting algorithms auto wired. It should have the business logic to choose the appropriate algorithm.

### Q : What are the New Features in Spring Framework 5.0?

I’ve recently wrote a book on Mastering Spring 5.0.

Important features in Spring 5.0 are Functional Web Framework, Kotlin and Reactive Programming support. But none of these are mainstream yet.

### Q : Compare Application Context vs IOC Container vs Web Container vs EJB Container

Do we need a Web Container to run a Spring Boot Application?

Basically spring runs anywhere where we have a JVM because that JVM will have capability to run some sort of a container or capability to run an application. Difference would be that the mechanism to load application context would be different based on where it runs. e.g. 2 high level categories - ApplicationContext for Web and Applicationcontext for standalone and again in those 2 categories we will choose “how” and “from where” we want to load that metadata for those applicationContext.

Web Container & EJB Containers are part of the application/web servers - Tomcat, Websphere, Weblogic. They run what ever application is given to them. Java EE defines a contract for web applications (web.xml etc etc) and these are the implementations of that contract.

Spring Container is part of the application you are building - the jar or the war. It can run inside a web container, EJB container or even without them :) You can launch it as a java application or you can even run it in an embedded server.

### Q : How do we inject different bean depending on the configuration in application.properties?

Consider the example

```java
interface GreetingService {
public String sayHello();
}
```
Two components
```java
@Component(value="real")
class RealGreetingService implements GreetingService {
	public String sayHello() {
		return "I'm real";
	}
}

 
@Component(value="mock")
class MockGreetingService implements GreetingService {
	public String sayHello() {
		return "I'm mock";
	}
}
```

application.properties

```java
application.greeting: real 
```

Adding @Resource with the name of the property

```java
@RestController
public class WelcomeController {
 
@Resource(name="${application.greeting}")
private GreeterService service1;
```

### Q : What is the minimum baseline Java Version for Spring Boot 2 and Spring 5?

Spring 5.0 and Spring Boot 2.0 requires Java 8 or later. Java 6 and 7 are no longer supported.

Recommended Reading

* https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.0.0-M1-Release-Notes

### Q : What is the difference between @Controller and @RestController?

@RestController = @Controller + @ResponseBody

The response from the @RestController are directly returned as a response after conversion to JSON or XML.

In Summary

* @Controller : Uses a view resolver to find the view. You are returning either the View, View Name or Model and View.

* @RestController : You are returning a bean. The bean would be converted to a JSON using a Jackson message converter.

```java
@Controller
@ResponseBody
public class MyController { }
 
@RestController
public class MyRestController { }
```

### Q : Why do we use @ResponseBody sometimes and ResponseEntity some other times?









