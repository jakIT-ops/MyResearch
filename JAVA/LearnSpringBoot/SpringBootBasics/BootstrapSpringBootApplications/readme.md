## Spring Boot Provides a wide range of starter projects. Spring Initializr supports all of them and more. Among a varied range of starter projects and options supported are:

* spring-boot-starter-web-services: For building applications exposing SOAP Web Services

* spring-boot-starter-web - Build Web Applications & Restful appplications

* spring-boot-starter-test - Write great Unit and Integration Tests

* spring-boot-starter-jdbc - Traditional JDBC Applications

* spring-boot-starter-hateoas - Make your services more RESTful by adding HATEOAS features

* spring-boot-starter-security - Authentication and Authorization using Spring Security

* spring-boot-starter-jpa - Spring Data JPA with Hibernate

* spring-boot-starter-cache - Enabling Spring Framework's caching support

* spring-boot-starter-data-rest - Expose Simple REST Services using Spring Data REST

There are a few starters for technical stuff as well

* spring-boot-starter-actuator - To use advanced features like monitoring & tracing to your application out of the box

* spring-boot-starter-undertow, spring-boot-starter-jetty, spring-boot-starter-tomcat - To pick your specific choice of Embedded Servlet Container

* spring-boot-starter-logging - For Logging using logback

* spring-boot-starter-log4j2 - Logging using Log4j2

### Launch Spring Initializr https://start.spring.io/

* application.properties - Application Configuration file.

* pom.xml - Included dependencies for Spring Boot Starter We, Actuator, DevTools. Uses Spring Boot Starter Parent as parent pom.

## Introduction to Spring Boot Starter Parent

### What is Spring Boot Starter Parent?

All Spring Boot projects typically use spring-boot-starter-parent as the parent in pom.xml

```xml
<parent>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-parent</artifactId>
	<version>3.0.3-M3</version>	
</parent>
```

Parent poms' allow you to manage the following things for multiple child projects and modules:

* Configuration - Java Version and Other Properties

* Dependency Management - Version of dependencies

* Default Plugin Configuration

### What is inside Spring Boot Starter Perent?

First of all - Spring Boot Starter Parent defines spring-boot-dependencies as the parent pom. It inherits dependency management from spring-boot-dependencies.

```xml
<parent>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-dependencies</artifactId>
	<version>3.0.0-M3</version>
	<relativePath>../../spring-boot-dependencies</relativePath>
</parent>
```

Default java version is 1.6 A project can override this by specifying a property` 17

3.1.1
` in the project pom. A few other settings related to encoding and source, target version are also set in the parent pom.

```xml
<java.version>17</java.version>
<resource.delimiter>@</resource.delimiter>
<maven.compiler.source>${java.version}</maven.compiler.source>
<maven.compiler.target>${java.version}</maven.compiler.target>
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
```

Spring Boot Starter Parent specifies the default configuration for a host of plugins including `maven-compiler-plugin`, `maven-failsafe-plugin`, `maven-jar-plugin`, `maven-war-plugin` and more .

```xml
<plugin>
	<groupId>org.apache.maven.plugins</groupId>
	<artifactId>maven-compiler-plugin</artifactId>
	<configuration>
	    <parameters>true</parameters>
	</configuration>
</plugin>
<plugin>
	<groupId>org.apache.maven.plugins</groupId>
	<artifactId>maven-failsafe-plugin</artifactId>
	<executions>
		<execution>
			<goals>
				<goal>integration-test</goal>
				<goal>verify</goal>
			</goals>
		</execution>
	</executions>
	<configuration>
	   <classesDirectory>${project.build.outputDirectory}</classesDirectory>
	</configuration>
</plugin>
<plugin>
	<groupId>org.apache.maven.plugins</groupId>
	<artifactId>maven-jar-plugin</artifactId>
	<configuration>
            <archive>
				<manifest>
					<mainClass>${start-class}</mainClass>
					<addDefaultImplementationEntries>true</addDefaultImplementationEntries>
				</manifest>
            </archive>
    </configuration>
</plugin>
<plugin>
	<groupId>org.apache.maven.plugins</groupId>
	<artifactId>maven-war-plugin</artifactId>
	<configuration>
		<archive>
			<manifest>
		    <mainClass>${start-class}</mainClass>
			<addDefaultImplementationEntries>true</addDefaultImplementationEntries>
			</manifest>
		</archive>
	</configuration>
</plugin>
```

### What does Spring Boot Starter Parent inherit from spring-boot-dependencies?

Spring Boot Dependencies defines the default dependency management for all Spring Boot projects. If we would want to use a new version of a specific dependency, we can override the version by specifying a new property in the project pom. The extract below shows some of the important dependencies that are managed by Spring Boot Dependencies parent pom. Since Spring Boot Starter Parent inherit from spring-boot-dependencies, it shares all these characteristics as well.

```xml
<properties>
	<artemis.version>2.22.0</artemis.version>
	...
	<ehcache3.version>3.10.0</ehcache3.version>
	...
	<h2.version>2.1.212</h2.version>
	<hamcrest.version>2.2</hamcrest.version>
	<hazelcast.version>5.1.1</hazelcast.version>
	<hibernate.version>5.6.9.Final</hibernate.version>
	<hibernate-validator.version>7.0.4.Final</hibernate-validator.version>
	<hikaricp.version>5.0.1</hikaricp.version>
	<hsqldb.version>2.6.1</hsqldb.version>
	<htmlunit.version>2.61.0</htmlunit.version>
	<httpasyncclient.version>4.1.5</httpasyncclient.version>
	<httpclient.version>4.5.13</httpclient.version>
	<httpclient5.version>5.1.3</httpclient5.version>
	<httpcore.version>4.4.15</httpcore.version>
	<httpcore5.version>5.1.3</httpcore5.version>
	<influxdb-java.version>2.22</influxdb-java.version>
	<jackson-bom.version>2.13.3</jackson-bom.version>
	<jakarta-activation.version>2.0.1</jakarta-activation.version>
    <jakarta-annotation.version>2.0.0</jakarta-annotation.version>
	....
	<jetty.version>11.0.9</jetty.version>
	<junit-jupiter.version>5.8.2</junit-jupiter.version>
    <kafka.version>3.2.0</kafka.version>
    <kotlin.version>1.6.21</kotlin.version>
	...
	<log4j2.version>2.17.2</log4j2.version>
    <logback.version>1.2.11</logback.version>
    <lombok.version>1.18.24</lombok.version>
	<maven-antrun-plugin.version>3.1.0</maven-antrun-plugin.version>
    <maven-assembly-plugin.version>3.3.0</maven-assembly-plugin.version>
    <maven-clean-plugin.version>3.2.0</maven-clean-plugin.version>
    <maven-compiler-plugin.version>3.10.1</maven-compiler-plugin.version>
    <maven-dependency-plugin.version>3.3.0</maven-dependency-plugin.version>
    <maven-deploy-plugin.version>2.8.2</maven-deploy-plugin.version>
    <maven-enforcer-plugin.version>3.0.0</maven-enforcer-plugin.version>
    <maven-failsafe-plugin.version>2.22.2</maven-failsafe-plugin.version>
    <maven-help-plugin.version>3.2.0</maven-help-plugin.version>
    <maven-install-plugin.version>2.5.2</maven-install-plugin.version>
    <maven-invoker-plugin.version>3.2.2</maven-invoker-plugin.version>
    <maven-jar-plugin.version>3.2.2</maven-jar-plugin.version>
    <maven-javadoc-plugin.version>3.4.0</maven-javadoc-plugin.version>
    <maven-resources-plugin.version>3.2.0</maven-resources-plugin.version>
    <maven-shade-plugin.version>3.3.0</maven-shade-plugin.version>
	<spring-security.version>6.0.0-M5</spring-security.version>
	<tomcat.version>10.0.21</tomcat.version>
	<undertow.version>2.2.17.Final</undertow.version>
	<webjars-locator.version>0.50</webjars-locator.version>
	<wsdl4j.version>1.6.3</wsdl4j.version>
	<xml-maven-plugin.version>1.0.2</xml-maven-plugin.version>
    <xmlunit2.version>2.9.0</xmlunit2.version>
	<zipkin.version>2.16.3</zipkin.version>
</properties>
```

Defines Maven 3.2.1 as the minimum version needed.

```xml
<prerequisites>
	<maven>3.2.1</maven>
</prerequisites>
```

### Spring Boot Starter Web

Spring Boot Starter Web brings in 2 important features

* Compatible Dependencies that are needed to develop web applications

* Auto Configuration

Dependencies can be classified into:

* Spring - core, beans, context, aop

* Web MVC - (Spring MVC)

* Jackson - for JSON Binding

* Validation - Hibernate Validator, Validation API

* Embedded Servlet Container - Tomcat

* Logging - logback, slf4j

Any typical web application would use all these dependencies. Spring Boot Starter Web comes pre packaged with these. As a developer, I would not need to worry about either these dependencies or their compatible versions.

#### Auto Configuration

Spring Boot Starter Web auto configures the basic things that are needed. To understand the features Spring Boot Starter Web brings in, lets run StudentServicesApplication.java as a Java Application and review the log.

```xml
Mapping servlet: 'dispatcherServlet' to [/]

Mapped "{[/error]}" onto public org.springframework.http.ResponseEntity<java.util.Map<java.lang.String, java.lang.Object>> org.springframework.boot.autoconfigure.web.BasicErrorController.error(javax.servlet.http.HttpServletRequest)

Mapped URL path [/webjars/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
```

Spring Boot Starter Web auto-configures

* Dispatcher Servlet

* Error Page

* Web Jars to manage your static dependencies

* Embedded Servlet Container - Tomcat is the default




