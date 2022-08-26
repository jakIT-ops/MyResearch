# What is SOAP?

`SOAP` (Simple Object Access Protocol) is an XML-based protocol for accessing web services over HTTP and few other protocols. It has some specifications which can be used across all applications and platforms.

`SOAP` follows a strict messaging structure, a set of encoding rules, and a convention for providing rendering requests and responses.

### Advantages

SOAP communicates over HTTP, HTTPS, TCP, SMTP, FTP, XMPP, and more, unlike REST which communicates over HTTP and HTTPS only.

SOAP can have its own implementation of security SOAP WS-Security that allows it to encrypt messages and have authentication data in the message header.

SOAP is ACID-compliant (Atomicity, Consistency, Isolation, and Durability).

# Creating a SOAP client Project

### Creating the Java project

Macintosh/Linux users, please run the following commands to create the basic folder structure of the test project.

```java
mkdir -p soap-client/src/{main,test}/{resources,java}
```

### Creating a build file

Inside the folder, we need to create build files containing the dependencies and plugin tasks. Here, we are going to use spring-boot, spring-boot-starter-web-services and wsdl4j libraries for creating a SOAP client.

### Gradle

Create a file build.gradle and copy the content below into that:

```java
plugins {
    id 'org.springframework.boot' version '2.2.2.RELEASE'
    id 'io.spring.dependency-management' version '1.0.8.RELEASE'
    id 'java'
    id 'eclipse'
    id 'idea'
}

group = 'io.educative'
jar.baseName = 'soap-client'
version = '1.0.0-SNAPSHOT'

bootJar {
    mainClassName = ''
}

sourceCompatibility = '1.8'
targetCompatibility = '1.8'

repositories {
    mavenCentral()
}

configurations {
    developmentOnly
    runtimeClasspath {
        extendsFrom developmentOnly
    }
    jaxb
}

task genJaxb {
    ext.sourcesDir = "${buildDir}/generated-sources/jaxb"
    ext.classesDir = "${buildDir}/classes/jaxb"
    ext.schema = "src/main/resources/students.wsdl"

    outputs.dir classesDir

    doLast() {
        project.ant {
            taskdef name: "xjc", classname: "com.sun.tools.xjc.XJCTask",
                    classpath: configurations.jaxb.asPath
            mkdir(dir: sourcesDir)
            mkdir(dir: classesDir)

            xjc(destdir: sourcesDir, schema: schema) {
                arg(value: "-wsdl")
                produces(dir: sourcesDir, includes: "**/*.java")
            }

            javac(destdir: classesDir, source: 1.8, target: 1.8, debug: true,
                    debugLevel: "lines,vars,source", includeantruntime: false,
                    classpath: configurations.jaxb.asPath) {
                src(path: sourcesDir)
                include(name: "**/*.java")
                include(name: "*.java")
            }

            copy(todir: classesDir) {
                fileset(dir: sourcesDir, erroronmissingdir: false) {
                    exclude(name: "**/*.java")
                }
            }
        }
    }
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web-services'
    implementation 'wsdl4j:wsdl4j:1.6.1'
    jaxb("org.glassfish.jaxb:jaxb-xjc:2.2.11")
    compile(files(genJaxb.classesDir).builtBy(genJaxb))
    compile 'org.testng:testng:7.1.0'
    compile 'org.apache.commons:commons-lang3:3.9'
}

```

### Maven 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.2.2.RELEASE</version>
        <relativePath /> 
    </parent>
    <groupId>io.educative</groupId>
    <artifactId>soap-client</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web-services</artifactId>
        </dependency>
        <dependency>
            <groupId>wsdl4j</groupId>
            <artifactId>wsdl4j</artifactId>
        </dependency>
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-lang3</artifactId>
            <version>3.9</version>
        </dependency>
        <dependency>
            <groupId>org.testng</groupId>
            <artifactId>testng</artifactId>
            <version>7.1.0</version>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>jaxb2-maven-plugin</artifactId>
                <version>2.5.0</version>
                <executions>
                    <execution>
                        <id>xjc</id>
                        <goals>
                            <goal>xjc</goal>
                        </goals>
                    </execution>
                </executions>
                <configuration>
                    <sourceType>wsdl</sourceType>
                    <sources>
                        <source>${project.basedir}/src/main/resources/students.wsdl</source>
                    </sources>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

# SOAP Client for Making Web Service Calls


### Creating SOAP client

Create a package io.educative.soap under src/main/java, create WebServiceClient.java under io.educative.soap and copy the following contents into it.

```java
package io.educative.soap;

import javax.annotation.PostConstruct;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.oxm.jaxb.Jaxb2Marshaller;
import org.springframework.util.ClassUtils;
import org.springframework.ws.client.core.WebServiceTemplate;

import io.educative.soap_automation.GetStudentsRequest;

@Configuration
public class WebServiceClient {

    private Jaxb2Marshaller marshaller = new Jaxb2Marshaller();

    @PostConstruct
    public void init() throws Exception {
        marshaller.setPackagesToScan(ClassUtils.getPackageName(GetStudentsRequest.class));
        marshaller.afterPropertiesSet();
    }

    @Bean
    public WebServiceTemplate getWebServiceTemplate() {
        return new WebServiceTemplate(marshaller);
    }

}
```

# Sending Requests using SOAP Client

### Creating BaseTest class
Since we use the Spring framework and Annotations for defining beans, we need to load them before doing anything. Here, we will use the TestNG annotation @BeforeSuite to load the beans using AnnotationConfigApplicationContext which reads all the Spring annotated classes like @Configuration, @Service, etc.

In our case, we have annotated the WebServiceClient class with @Configuration for the bean that needs to be loaded.

We will create BaseTest which will be extended by all the test classes so that we need not duplicate the @BeforeSuite method that contains loading of beans. This will be executed once per test suite and initializing the WebServiceTemplate in @BeforeClass will be executed for every test class that is extending BaseTest. We will mark BaseTest as abstract to disallow the explicit initialization of the class.

It also has the SERVICE_URL that holds the location where the web service is hosted.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.ws.client.core.WebServiceTemplate;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeSuite;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;

public abstract class BaseTest {

    protected static ApplicationContext CONTEXT;

    protected WebServiceTemplate webServiceTemplate;

    protected static final String SERVICE_URL = "http://ezifyautomationlabs.com:6566/educative-soap/ws";

    protected static final Logger LOG = LoggerFactory.getLogger(BaseTest.class);

    @BeforeSuite
    public void init() {
        if (CONTEXT == null) {
            CONTEXT = new AnnotationConfigApplicationContext(io.educative.soap.WebServiceClient.class);
        }
    }

    @BeforeClass
    public void initTemplate() {
        webServiceTemplate = CONTEXT.getBean(WebServiceTemplate.class);
    }

    protected void printResponse(Object response) {
        try {
            LOG.info("printing response '{}' => \n{}", response.getClass().getName(),
                    new XmlMapper().writerWithDefaultPrettyPrinter().writeValueAsString(response));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Creating TestClass

Here, we are creating a test class to test the GetStudents API. All the initialization code is already contained in BaseTest and marked with TestNG configuration annotations. Now, we have the required things to make the web service call.

To make the web service call, we need to know the service URL (where the web service is hosted), the request format (or class), and the response format (or class). All these information can be found in students.wsdl.

After building the test project, all the request and response formats (or classes) mentioned in students.wsdl will be generated and available for us to use.

```java
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotNull;
import static org.testng.Assert.assertTrue;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.ws.client.core.WebServiceTemplate;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.Test;

import com.fasterxml.jackson.dataformat.xml.XmlMapper;

import io.educative.soap_automation.GetStudentsRequest;
import io.educative.soap_automation.GetStudentsResponse;

public class TestSOAP extends BaseTest {

	@Test
	public void testGetStudents() {

		GetStudentsRequest request = new GetStudentsRequest();
		request.setGender("male");

		GetStudentsResponse response = (GetStudentsResponse) webServiceTemplate.marshalSendAndReceive(SERVICE_URL,
				request);

		assertNotNull(response, "GetStudentsResponse is null");

		assertTrue(!response.getStudents().isEmpty(), "students list is empty");

		assertTrue(response.getStudents().get(0).getGender().equalsIgnoreCase(request.getGender()),
				"students must be having the same gender as sent in request - " + request.getGender() + " but found "
						+ response.getStudents().get(0).getGender());

		printResponse(response);
	}

}

abstract class BaseTest {

	protected static ApplicationContext CONTEXT;

	protected WebServiceTemplate webServiceTemplate;

	protected static final String SERVICE_URL = "http://ezifyautomationlabs.com:6566/educative-soap/ws";

	protected static final Logger LOG = LoggerFactory.getLogger(BaseTest.class);

	@BeforeSuite
	public void init() {
		if (CONTEXT == null) {
			CONTEXT = new AnnotationConfigApplicationContext(io.educative.soap.WebServiceClient.class);
		}
	}

	@BeforeClass
	public void initTemplate() {
		webServiceTemplate = CONTEXT.getBean(WebServiceTemplate.class);
	}

	protected void printResponse(Object response) {
		try {
			LOG.info("printing response '{}' => \n{}", response.getClass().getName(),
					new XmlMapper().writerWithDefaultPrettyPrinter().writeValueAsString(response));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
```

The web service is hosted at http://ezifyautomationlabs.com:6566/educative-soap/ws and saved as SERVICE_URL in BaseTest as shown in line 49.

In the code above:

* We have created a TestNG test method testGetStudents as shown in line 22. This method contains code for creating the request object GetStudentsRequest as shown in lines 24 & 25.

* Using WebServiceTemplate's marshalSendAndReceive method that internally transforms the Java object to XML structure that the SOAP web service understands, we make the web service call and get the transformed xml to GetStudentsResponse object in response from the server as shown in line 27.

* We are asserting or validating whether the response is not null, the students list in response is not empty and contains the same gender as sent in the request as shown in lines 30, 32 & 34 respectively.


# Proxy Server Settings

### What is a proxy server?

A proxy server is an intermediary server that is virtually located between the client and the server. All the service requests are sent to the actual server via proxy servers.

### Adding a proxy setting to WebServiceTemplate

We have already learned in the Sending requests using SOAP client lesson how to create a WebServiceTemplate that can be used to make web service calls.

This lesson is an extension of that part and here, we will add proxy settings to the created WebServiceTemplate with the following code:

```java
import javax.annotation.PostConstruct;

import org.apache.http.HttpHost;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.oxm.jaxb.Jaxb2Marshaller;
import org.springframework.util.ClassUtils;
import org.springframework.ws.client.core.WebServiceTemplate;
import org.springframework.ws.transport.WebServiceMessageSender;
import org.springframework.ws.transport.http.HttpComponentsMessageSender;

import io.educative.soap_automation.GetStudentsRequest;

@Configuration
public class WebServiceClient {

    private final Jaxb2Marshaller marshaller = new Jaxb2Marshaller();

    private final static String PROXY_SERVER = "proxyhost";

    @PostConstruct
    public void init() throws Exception {
        marshaller.setPackagesToScan(ClassUtils.getPackageName(GetStudentsRequest.class));
        marshaller.afterPropertiesSet();
    }

    @Bean
    public WebServiceTemplate getWebServiceTemplate() {
        WebServiceTemplate webServiceTemplate = new WebServiceTemplate(marshaller);
        webServiceTemplate.setMessageSender(getMessageSender());
        return webServiceTemplate;
    }

    private WebServiceMessageSender getMessageSender() {
        RequestConfig config = RequestConfig
                .custom()
                .setProxy(new HttpHost(PROXY_SERVER))
                .build();

        CloseableHttpClient client = HttpClients
                .custom()
                .setDefaultRequestConfig(config)
                .build();

        return new HttpComponentsMessageSender(client);

    }
}
```


