# About the API and WebServices

### Simple Simulation

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import static org.hamcrest.Matchers.equalTo;
import org.testng.annotations.Test;
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertTrue;

import io.restassured.response.Response;
import io.restassured.RestAssured;

public class GETRequestTest {

	private static Logger LOG = LoggerFactory.getLogger(GETRequestTest.class);

	@Test
	public void testGetAllStudentRecords() {

	    String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
		
		/**
		 * Example 1 - GET all the existing student's record
		 */
	     LOG.info("Step - 1 : Send GET Request");
		 Response response = RestAssured.given().get(url).andReturn();
		 
		 LOG.info("Step - 2 : Print the JSON response body");
		 response.getBody().prettyPrint();
		 
		 LOG.info("Step - 3 : Assert StatusCode = 200");
		 assertEquals(response.getStatusCode(), 200, "http status code");
		
		 LOG.info("Step - 4 : Verify that the response contains id = 101");
		 LOG.info("list of Student's Id " +response.getBody().jsonPath().getList("id"));
		 assertTrue(response.getBody().jsonPath().getList("id").contains(101));
	}	
}
// Out:
/*
10:03:45.470 [main] INFO TestExecutionListener - *************************** test 'testGetAllStudentRecords' starting ***************************
10:03:45.475 [main] INFO GETRequestTest - Step - 1 : Send GET Request
10:03:46.924 [main] INFO GETRequestTest - Step - 2 : Print the JSON response body
[
    {
        "id": 100,
        "first_name": "John",
        "last_name": "Doe",
        "gender": "male"
    },
    {
        "id": 101,
        "first_name": "Kelly",
        "last_name": "Flower",
        "gender": "female"
    },
    {
        "id": 102,
        "first_name": "Json",
        "last_name": "Ray",
        "gender": "male"
    }
]
10:03:46.980 [main] INFO GETRequestTest - Step - 3 : Assert StatusCode = 200
10:03:46.982 [main] INFO GETRequestTest - Step - 4 : Verify that the response contains id = 101
10:03:47.482 [main] INFO GETRequestTest - list of Student's Id [100, 101, 102]
10:03:47.548 [main] INFO TestExecutionListener - *************************** test 'testGetAllStudentRecords' succeeded ***************************

===============================================
Command line suite
Total tests run: 1, Passes: 1, Failures: 0, Skips: 0
===============================================

*/
```

# About API and Web Services

### Types of web services

There are two main types of web services:

* SOAP web services – SOAP which stands for Simple Object Access Protocol, is a specification that enables applications to communicate with other applications. It uses an XML-based protocol to access web services over HTTP.

* RESTful web services – REST which stands for Representational State Transfer, is a service developed on the REST architecture and is often called a RESTful service. They are lightweight, maintainable, and scalable in nature. The underlying protocol for REST is HTTP.


### API vs web services

| API	 | Web Services |
| :----- | -----------: |
| Not all APIs are web services | All web services are APIs |
| APIs can use any style for communication	| A web service can use SOAP, REST, and XML-RPC for communication |
| APIs can also be used to invoke functions within a software, so it does not always need a network for its operation |	A web service will always need a network for its operation |

# Introduction to REST API

### Benefits of using REST

By following the principles of REST, we can benefit from the loose coupling between the server and the client, reliability, scalability, and better performance of the application. Few of the benefits of REST are listed below:

* Simplicity – REST web services are easy and simple to develop compared to SOAP web services

* Light-weight – REST advocates simple communication with the server over HTTP that supports plain XML, JSON formats in comparison to SOAP which supports only XML

* Architecture is similar to Web --the architecture of REST is very similar to how the web is designed. So, developers who understand the web can easily understand and develop RESTful web services

* Scalability – the REST architecture advocates refraining from the conversational state that allows us to easily add multiple instances of the components or application behind load balancers

## Guiding principles of REST

A RESTful service needs to comply with the following 6 guiding constraints:

* Client–Server – the main principle behind this is the separation of concerns, i.e, separating the user interface concern from the data storage concerns. By following this principle, we can improve the:

	* portability of the user interface across platforms

	* scalability by simplifying the server component

* Stateless – each request from the client must be sent to the server with all the necessary information to understand the request and the request cannot take advantage of any stored context on the server. The session state is therefore maintained entirely on the client.

* Cacheable – cache constraints require that the data within a response to a request be implicitly or explicitly denoted as cacheable or non-cacheable to prevent clients from giving stale information. If a response is cacheable, then a client cache is given the right to reuse that response data for later, equivalent requests. This allows us to minimize the network calls made to the server.

* Uniform Interface – this is the fundamental principle of the RESTful system. It simplifies and decouples the architecture of the system, allows us to independently scale the components, and improve the interactions between components and other systems. The four architectural constraints that RESTful system should follow in order to a uniform interface are:

	* resource identification

	* manipulation of resources through representations

	* self-descriptive messages

	* hypermedia as the engine of application state (HATEOS)

* Layered System – the layered system style allows an architecture to be divided into a number of hierarchical layers or tiers by constraining each of the layer’s behavior such that each layer cannot access beyond the immediate layer with which they are interacting with. This allows us to independently scale the layers.

* Code on-demand – this principle is an optional one. REST allows client functionality to be extended by downloading executable scripts that can be executed on client-side like Java applets or Javascript.

An extract of the information is taken from https://restfulapi.net.























































