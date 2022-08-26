# Crating a SOAP Web Service with SPring Boot Starter Web Services

### Types of Web Services

Not really types but a broad classification

* SOAP

* REST

These are not really mutually exclusive. Some SOAP services can actually be RESTful.

### SOAP

* SOAP was earlier an abbreviation for Simple Object Access Protocol. In SOAP, the request and response are in XML format. However, not all types of XML are valid SOAP Requests.

* SOAP defines a standard XML format. We will use WSDL (Web Service Definition Language) to define the format of request xml and the response xml.

Now lets say Facebook wants to know how to call the TODO Service? What should I give to the Facebook developer?


### REST vs SOAP

REST vs SOAP are not really comparable. REST is an architectural style. SOAP is a message exchange format.

Let’s compare the popular implementations of REST and SOAP styles.

* RESTful Sample Implementation : JSON over HTTP
* SOAP Sample Implementation : XML over SOAP over HTTP

Following are the important things to consider:

* REST is built over simple HTTP protocol. SOAP services are more complex to implement and more complex to consume.

* REST has better performance and scalability. REST reads can be cached, SOAP based reads cannot be cached.

* REST permits many different data formats (JSON is the most popular choice) where as SOAP only permits XML.

* SOAP services have well defined structure and interface (WSDL) and has a set of well defined standards (WS-Security, WS-AtomicTransaction and WS-ReliableMessaging). Documentation standards with REST are evolving(We will use Swagger in this course).

### More SOAP Methods

You can enhance the endpoint to expose more operations. The steps would be

* Define the structure for Request and Response in XSD

* Enhance the Endpoint to process the Request

Go ahead and test it.

Other thing you can work on is to remove the hardcoding and add business logic and persistence stuff using JPA.






