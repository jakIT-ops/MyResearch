### What is the core problem that the Spring Framework solves?

> The most important feature of the Spring Framework is Dependency Injection. At the core of all Spring Modules is Dependency Injection, or IOC Inversion of Control.

Why is this important? Because, when DI or IOC is used properly, we can develop loosely coupled applications. And loosely coupled applications can be easily unit tested.

<b>Example without Dependency Injection</b>

Consider the example below: WelcomeController depends on WelcomeService to get the welcome message. What is it doing to get an instance of WelcomeService? `WelcomeService service = new WelcomeService();`. It’s creating an instance of it. And that means they are tightly coupled. For example, If I create a mock for WelcomeService in a unit test for WelcomeController, how do I make WelcomeController use the mock? Not easy!

```java
@RestController
public class WelcomeController {

    private WelcomeService service = new WelcomeService();

	@RequestMapping("/welcome")
	public String welcome() {
		return service.retrieveWelcomeMessage();
	}
}
```

<b>Same Example with Dependency Injection</b>

The world looks much easier with dependency injection. You let the spring framework do the hard work. We just use two simple annotations: `@Service` and `@Autowired`.

* Using `@Service`, we tell the Spring Framework: “Hey there, this is a bean that you need to manage.”

* Using `@Autowired`, we tell Spring Framework: Hey, find the correct match for this specific type and autowire it in.

In the example below, the Spring framework would create a bean for WelcomeService and autowire it into WelcomeController

In a unit test, I can ask the Spring framework to auto-wire the mock of WelcomeService into WelcomeController. Spring Boot makes it easy to do this with `@MockBean`. But, that’s a different story altogether.

```java
@Service
public class WelcomeService {
    //Bla Bla Bla
}

@RestController
public class WelcomeController {

    @Autowired
    private WelcomeService service;

	@RequestMapping("/welcome")
	public String welcome() {
		return service.retrieveWelcomeMessage();
	}
}
```

### What else does the Spring Framework solve?

<b>Problem 1: Duplication/Plumbing Code</b>

Does the Spring Framework stop with Dependency Injection? No It builds on the core concept of dependency injection with a number of spring modules.

* Spring JDBC

* Spring MVC

* Spring AOP

* Spring ORM

* Spring JMS

* Spring Test

Consider Spring JMS and Spring JDBC for a moment.

Do these modules bring in any new functionality? No We can do all this with J2EE or JEE. So, what do these bring in? They bring in simple abstractions. The aim of these abstractions is to

* Reduce Boilerplate Code/Reduce Duplication.

* Promoting Decoupling/Increasing Unit Testablity

For example, you need much less code to use a JDBCTemplate or a JMSTemplate compared to traditional JDBC or JMS.

<b>Problem 2: Good Integration with Other Frameworks</b>

The great thing about the Spring Framework is that it does not try to solve problems which are already solved. All that it does is provide a great integration with frameworks that provide great solutions.

* Hibernate for ORM

* iBatis for Object Mapping

* JUnit & Mockito for Unit Testing

### What is the core problem that the Spring MVC Framework solves?

> The Spring MVC Framework provides a decoupled way of developing web applications. With simple concepts like Dispatcher Servlet, ModelAndView, and View Resolver, it makes it easy to develop web applications.

### Why do we need Spring Boot?

Spring-based applications have a lot of configuration.

When we use Spring MVC, we need to configure component scanning, dispatcher servlet, a view resolver, and web jars (for delivering static content), among other things.

```xml
<bean
        class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix">
            <value>/WEB-INF/views/</value>
        </property>
        <property name="suffix">
            <value>.jsp</value>
        </property>
  </bean>
  
  <mvc:resources mapping="/webjars/**" location="/webjars/"/>
```

The below code snippet shows the typical configuration of a dispatcher servlet in a web application.

```xml
<servlet>
        <servlet-name>dispatcher</servlet-name>
        <servlet-class>
            org.springframework.web.servlet.DispatcherServlet
        </servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/todo-servlet.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <servlet-mapping>
        <servlet-name>dispatcher</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
```

When we use Hibernate/JPA, we would need to configure a datasource, an entity manager factory, and a transaction manager, among a host of other things.

```xml
 <bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource"
        destroy-method="close">
        <property name="driverClass" value="${db.driver}" />
        <property name="jdbcUrl" value="${db.url}" />
        <property name="user" value="${db.username}" />
        <property name="password" value="${db.password}" />
    </bean>

    <jdbc:initialize-database data-source="dataSource">
        <jdbc:script location="classpath:config/schema.sql" />
        <jdbc:script location="classpath:config/data.sql" />
    </jdbc:initialize-database>

    <bean
        class="org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean"
        id="entityManagerFactory">
        <property name="persistenceUnitName" value="hsql_pu" />
        <property name="dataSource" ref="dataSource" />
    </bean>

    <bean id="transactionManager" class="org.springframework.orm.jpa.JpaTransactionManager">
        <property name="entityManagerFactory" ref="entityManagerFactory" />
        <property name="dataSource" ref="dataSource" />
    </bean>

    <tx:annotation-driven transaction-manager="transactionManager"/>
```

<b>Problem # 1: Spring Boot Auto Configuration: Can we think differently?</b>

The Spring Boot brings in a new thought process around this.

> Can we bring more intelligence into this? When a spring mvc jar is added into an application, can we auto configure some beans automatically?

* How about auto configuring a Data Source if Hibernate jar is on the classpath?

* How about auto configuring a Dispatcher Servlet if a Spring MVC jar is on the classpath?

There would be provisions to override the default auto configuration.

> Spring Boot looks at: a) Frameworks available on the CLASSPATH b) Existing configuration for the application. Based on these, Spring Boot provides the basic configuration needed to configure the application with these frameworks. This is called `Auto Configuration.`

### Other Goals of Spring Boot

There are a few starters for technical stuff as well.

* spring-boot-starter-actuator - To use advanced features like monitoring & tracing to your application out of the box

* spring-boot-starter-undertow, spring-boot-starter-jetty, spring-boot-starter-tomcat - To pick your specific choice of embedded servlet container,

* spring-boot-starter-logging - For Logging using logback

* spring-boot-starter-log4j2 - Logging using Log4j2

Spring Boot aims to enable production-ready applications in quick time.

* Actuator : It enables advanced monitoring and tracing of applications.

* Embedded Server Integrations - Since the server is integrated into the application, I would not need to have a separate application server installed on the server.

* Default Error Handling

