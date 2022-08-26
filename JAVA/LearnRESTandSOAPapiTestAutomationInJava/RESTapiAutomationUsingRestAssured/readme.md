### Demo class for REST

We have a student class, with the following fields and types:

| Access Specifier | Type    |	Field        |
| :--------------- | ------- | ------------: |
| private	   | Long    |	id	     |
| private	   | String  | firstName     |
| private	   | String  | lastName      |
| private	   | String  |	gender       |

### What is REST Assured?

REST Assured is a Java Domain Specific Language (DSL) API used for writing automated tests for RESTful APIs. It is used to invoke REST web services for POST, GET, PUT, DELETE, OPTIONS, PATCH, and HEAD requests and validate the response.


# What is a Rest Assured Library?

* It provides a lot of helper methods and abstraction layers that remove the need for writing a lot of boilerplate code for connections, sending a request, and parsing a response.

* The DSL provided by it, increases the readability of the code.

* Since it’s a Java library, there is a seamless integration with testing frameworks like Junit or TestNG and other continuous integration tools. 

dependency 

```xml
<dependency>
    <groupId>io.rest-assured</groupId>
    <artifactId>rest-assured</artifactId>
    <version>4.3.0</version>
</dependency>
```

# Given/When/Then

`given()`

It is used in building the DSL expression request with any additional information like headers, params, message body, authentication, etc., before making any HTTP Request like POST, GET, PUT, DELETE using given() method.

Example 1:

```java
RestAssured.given()
        .header("header1","value1")
        .header("header2", "value2")
        .param("param1","paramValue")
        .body(body)
        .post(url);
```


`when()`

Using when(), you can start building the DSL expression by sending a request without any parameters, headers or body etc.

when() can be used with given() or independently in the DSL expression.

Example 1:

RestAssured.given()
        .param("firstName", "John")
        .param("lastName", "Doe")
        .when()
        .get("/greet");




`then()`

It is always used with either given(), when(), or with both methods in the DSL expression. It returns a validatable response.

Example:

RestAssured.given().
        .param("firstName", "John")
        .param("lastName", "Doe")
        .when()
        .get("/greet")
        .then()
        .body("greeting", equalTo("John Doe"));

# Get Request

## Example 1 – Fetch all student records#

* HTTP Method: GET
* Target URL: http://ezifyautomationlabs.com:6565/
* Resource path: /educative-rest/students
* Take a look at the code below:

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
```

Let’s understand the example code above.

The code above uses the TestNG and RestAssured libraries for automating HTTP GET request.

* Step 1 – makes a GET request and returns a Response object
```java
Response response = RestAssured.given().get(url).andReturn();
```

* Step 2 – prints the response body in the JSON format

```java
response.getBody().prettyPrint();
```

* Step 3 – asserts the response status code as 200

```java
assertTrue(response.getStatusCode()==200);
```

* Step 4 – gets the list of all Student Ids from the response body and assert that one of the Id is 101

```java
LOG.info("list of Student's Id " +response.getBody().jsonPath().getList("id"));
assertTrue(response.getBody().jsonPath().getList("id").contains(101));
```

### Example 2 – Fetch a specific student’s record

* HTTP Method: GET

* Target URL: http://ezifyautomationlabs.com:6565

* Resource path for making GET request with path param: /educative-rest/students/{id}

* Resource path for making GET request with query params: /educative-rest/students?first_name={x}&last_name={y}

* Take a look at the code below:

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
	public void testAStudentRecord() {

         String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";

		 LOG.info("Step - 1 Get a Student's record with a specific Id.");
		 String url1 = url + "/" + "101";  
		 Response response1 = RestAssured.given()
		     .get(url1)
			 .andReturn();

		 LOG.info(response1.getStatusLine());
		 assertTrue(response1.getStatusCode()==200);
		 Long id = response1.getBody().jsonPath().getLong("id");
		 assertTrue(id==101);
		 
		 LOG.info("Step - 2 Get a Students record using matching gender");
		 Response response = RestAssured
		     .given()
		     .queryParam("gender", "male")
		     .get(url)
			 .andReturn();
		 response.getBody().prettyPrint();
	}	
}
```

# POST request 

### Example 1 – POST with a string body

* HTTP Method: POST

* Target URL: http://ezifyautomationlabs.com:6565

* Resource path: /educative-rest/students

* Message body: As a String Object

* Take a look at the code below:


```java

import static org.testng.Assert.assertTrue;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;


public class POSTRequestTest {

	private static Logger LOG = LoggerFactory.getLogger(POSTRequestTest.class);
		
	@Test
	public void testPOSTStringBody() {
      
        String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";

        LOG.info("Step - 1 : Target resource ( server ) : " + url);
        
        String body = "{\"first_name\": \"Jack\", \"last_name\": \"Preacher\", \"gender\": \"Male\" }";
        LOG.info("Step - 2 : Message body: " + body);
        
        LOG.info("Step - 3 : Send a POST Request");
        Response response = RestAssured.given()
                .header("accept", "application/json")
                .header("content-type", "application/json")
                .body(body)
                .post(url)
                .andReturn();
        
        LOG.info("Step - 4 : Print the response message and assert the status response code is 201 - Created");
        response.getBody().prettyPrint();	
		assertTrue(response.getStatusCode() == 201);
	        
	}
}
```


Let’s understand the example code above.

The code above uses the TestNG and Rest Assured libraries for automating the HTTP POST request and sends a string message for creating a new resource.

* Step 1 – the target URL
```java
String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
```

* Step 2 – the request message body as a String

```java
String body = "{\"first_name\": \"Jack\", \"last_name\": \"Preacher\", \"gender\": \"Male\" }";
```

* Step 3 – makes a POST Request with accept and content-type headers along with a message body and returns a Response object

```java
Response response = RestAssured.given()
                .header("accept", "application/json")
                .header("content-type", "application/json")
                .body(body)
                .post(url)
                .andReturn();
```

* Step 4 – logs the response body in JSON format and assert response status code as 201

```java
response.getBody().prettyPrint();               
assertTrue(response.getStatusCode()==201);
```

### Example 2 – POST request using POJO class

* HTTP Method: POST

* Target URL: http://ezifyautomationlabs.com:6565

* Resource path: /educative-rest/students

* Message Body: As a Java Object

* Take a look at the code below:

```java
import static org.testng.Assert.assertTrue;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;

import com.fasterxml.jackson.annotation.JsonProperty;

public class POSTRequestTest {

	private static Logger LOG = LoggerFactory.getLogger(POSTRequestTest.class);
		
	@Test
	public void testPOSTusingPOJO() {
              
        String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
        
        LOG.info("Step - 1 : Target resource ( server ) : " + url);
        
        Student body = new Student("Katherine", "AK", "Female");
        LOG.info("Step - 2 : Message body: " + body);
        
        LOG.info("Step - 3 : Send a POST Request");
        Response response = RestAssured.given()
                .header("accept", "application/json")
                .header("content-type", "application/json")
                .body(body)
                .post(url)
                .andReturn();
        
        LOG.info("Step - 4 : Print the response message and assert the status response code is 201 - Created");
        response.getBody().prettyPrint();	
		assertTrue(response.getStatusCode() == 201);
	        
	}
}

class Student {

    public Student(String firstName, String lastName, String gender) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.gender = gender;
    }

    @JsonProperty("id")
    Long id;

    @JsonProperty("first_name")
    String firstName;

    @JsonProperty("last_name")
    String lastName;

    @JsonProperty("gender")
    String gender;
}
```

# PUT request

### Example 1 – PUT request using POJO class

* HTTP Method: PUT

* Target URL: http://ezifyautomationlabs.com:6565

* Resource path: /educative-rest/students

* Message body: As a Java object

* Take a look at the code below:


```java
import static org.testng.Assert.assertTrue;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;

import com.fasterxml.jackson.annotation.JsonProperty;

public class PUTRequestTest {

	private static Logger LOG = LoggerFactory.getLogger(PUTRequestTest.class);
		
	@Test
	public void testPUTusingPOJO() {

	    String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
        
        LOG.info("Step - 1 : Create a new Student [POST]");

		Student body = new Student("Ryan", "Jackson", "Male");
		Response response = RestAssured.given()
				.header("accept", "application/json")
				.header("content-type", "application/json")
				.body(body)
				.post(url)
				.andReturn();
		
		LOG.info("Created Student Record");
		response.getBody().prettyPrint();
					
		String id = response.getBody().jsonPath().getString("id");
		LOG.info("Get the created Student ID: " + id);
      
		LOG.info("Step - 2 : Update Student's record [PUT]");
        Student bodyUpdate = new Student("John", "LP", "Male");
        bodyUpdate.id = Long.parseLong(id);
        String url1 = url + "/" + id;
        Response response1 = RestAssured.given()
                .header("accept", "application/json")
                .header("content-type", "application/json")
                .body(bodyUpdate)
                .put(url1)
                .andReturn();
        
        LOG.info("Step - 3 : Print the response message and assert the status");
        response1.getBody().prettyPrint();	
        LOG.info("Status " + response.getStatusCode());
		assertTrue(response.getStatusCode() == 201);
	       
	}
}

class Student {

    public Student(String firstName, String lastName, String gender) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.gender = gender;
    }

    @JsonProperty("id")
    Long id;

    @JsonProperty("first_name")
    String firstName;

    @JsonProperty("last_name")
    String lastName;

    @JsonProperty("gender")
    String gender;
}
```


# Delete Request 

### Example 1 – DELETE request for a particular id

* HTTP Method: DELETE

* Target URL: http://ezifyautomationlabs.com:6565

* Resource path: /educative-rest/students/{id}

* Take a look at the code below:


```java
import static org.testng.Assert.assertTrue;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;

import com.fasterxml.jackson.annotation.JsonProperty;

public class DELETERequestTest {

	private static Logger LOG = LoggerFactory.getLogger(DELETERequestTest.class);

	@Test
	public void testDelete() {

        String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";

		LOG.info("Step - 1 : Create a new Student [POST]");
		Student body = new Student("NewUser1", "DeleteUser", "Female");
		Response response = RestAssured.given().header("accept", "application/json")
				.header("content-type", "application/json").body(body).post(url).andReturn();

		LOG.info("Created Student Record");
		response.getBody().prettyPrint();

		String id = response.getBody().jsonPath().getString("id");
		LOG.info("Get the created Student ID: " + id);

		LOG.info("Step - 2 : Delete the created record. [DELETE ]");
		String url1 = url + "/" + id;
		Response response1 = RestAssured.given().delete(url1).andReturn();

		LOG.info("Step - 3 : Print the response message and assert the status");
		LOG.info("Response Status Code: " + response1.getStatusCode());
		assertTrue(response1.getBody().prettyPrint().isEmpty());
		assertTrue(response1.getStatusCode()==204);
		LOG.info("Student with id: " +id+ " is deleted");
	}

}
	 // This POJO class will be used for serialization and deserialzation of the data
	class Student {

		public Student(String firstName, String lastName, String gender) {
			this.firstName = firstName;
			this.lastName = lastName;
			this.gender = gender;
		}

		@JsonProperty("id")
		Long id;

		@JsonProperty("first_name")
		String firstName;

		@JsonProperty("last_name")
		String lastName;

		@JsonProperty("gender")
		String gender;
	}


```

### Example 2 – DELETE request for a non-existing Student id

* HTTP Method: DELETE

* Target URL: http://ezifyautomationlabs.com:6565

* Resource path: /educative-rest/students/{id}

* Take a look at the code below:

```java
import static org.testng.Assert.assertTrue;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;

import com.fasterxml.jackson.annotation.JsonProperty;

public class DELETERequestTest {

	private static Logger LOG = LoggerFactory.getLogger(DELETERequestTest.class);

	@Test
	public void testDeleteNonExistingStudentId() {

        String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
        String id = "48";
		LOG.info("Step - 2 : Delete the created record. [DELETE ]");
		String url1 = url + "/" + id;
		Response response1 = RestAssured.given().delete(url1).andReturn();

		LOG.info("Step - 3 : Print the response message and assert the status");
		LOG.info("Response Status Code: " + response1.getStatusCode());
		assertTrue(response1.getBody().prettyPrint().contains("Student does not exist"));
		assertTrue(response1.getStatusCode()==404);
	}

}
	
```

# JSONPath Library

JSONPath is a query language that helps us in parsing the JSON data, which can be used for validation or assertions in a test.

```xml
<dependency>
    <groupId>com.jayway.jsonpath</groupId>
    <artifactId>json-path</artifactId>
    <version>2.4.0</version>
</dependency>
```

## `JSONPath` Operators 

| Operator	| Description |
| :------------ | ----------: |
| ＄	| This is the root element and starting point for all path expressions. |
| @ |	This is a filter predicate for the current node. |
| *	 |This is a wildcard operator. It will return all objects regardless of their names or indexes. |
| ..	| This searches for the specified name recursively. | 
| .<name>	 | This is used for denoting the child element of the current element by name or index using dots .. | 
| ['<name>' (, '<name>')]	 |This is used for denoting the child element of the current element by name or index using brackets [ ]. |
| [<number> (, <number>)]	| This is used for denoting the array index of the element. | 
|[start:end]	| This is used for slicing the array based on start and end indexes. |
|[?(<expression>)]	| This is a filter expression and must evaluate to a boolean value. |


### Parsing a JSON file in the java

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import static org.hamcrest.Matchers.equalTo;
import org.testng.annotations.Test;
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertTrue;

import io.restassured.response.Response;
import io.restassured.RestAssured;
import java.util.List;
import io.restassured.path.json.JsonPath;

public class GETRequestTest {

	private static Logger LOG = LoggerFactory.getLogger(GETRequestTest.class);

	@Test
	public void testGetAllStudentRecords() {

    	String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
	
	    LOG.info("Step - 1 : Send GET Request");
		Response response = RestAssured.given().get(url).andReturn();
		 
		LOG.info("Step - 2 : Print the JSON response body");
		response.getBody().prettyPrint();
		 
		LOG.info("Step - 3 : Assert StatusCode = 200");
		assertTrue(response.getStatusCode()==200);
		
		LOG.info("Step - 4 :Create a JSONPath object");
		JsonPath jpath = response.jsonPath();
		 
		LOG.info("Step - 5 :Use JsonPath to get the list of all Student's first_name");
		// In java code you DO NOT have to write expression starting with `$`
		List<String> firstNames = jpath.get("first_name");
		LOG.info("List of all Student's first name: " +firstNames.toString());

	    LOG.info("Step - 6 :Use JsonPath to get the first_name of the first Student record");
		String firstName = jpath.get("first_name[0]");
		LOG.info("Print the first name of the first Student record: " +firstName.toString());

	}	
}
```


# Hamcrest Library

`Hamcrest` is a framework that comes with a library of useful matchers for writing match rules using matcher objects.

The matchers are most commonly used for:

1. Writing test assertions

2. Data validation

3. Filtering

> Note: In Java, we use the Matcher class to search for the regular expression in a particular piece of text.


### Example 

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.anyOf;
import static org.hamcrest.Matchers.anything;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.equalToIgnoringCase;
import static org.hamcrest.Matchers.greaterThan;
import static org.hamcrest.Matchers.greaterThanOrEqualTo;
import static org.hamcrest.Matchers.hasEntry;
import static org.hamcrest.Matchers.hasItem;
import static org.hamcrest.Matchers.hasItemInArray;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.nullValue;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.testng.annotations.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class APIDemo {
	
	private static Logger LOG = LoggerFactory.getLogger(APIDemo.class);
	
  /**
   *  anything() : Creates a matcher that always matches, regardless of the examined object.
   */
  @Test
  public void test_anything() {
	  
	     LOG.info("Test for anything()");
       String name = "xyz";
       assertThat(name, is(anything()));
       
	  
  }
  
  /**
   * hasEntry() :  Creates a matcher for Maps, matching when the examined
   * 			   Map contains at least one entry whose key equals the specified key 
   * 			   and whose value equals the specified value.
   */
  @Test
  public void test_hasEntry() throws Exception {
	  
	    LOG.info("Test for hasEntry()");
      Integer id = 1;
      String val = "one";
      
      Map<Integer, String> testMap = new HashMap<>();
      testMap.put(id, val);

      assertThat(testMap, hasEntry(1, "one"));
      
  }

 
 /**
  * anyOf() : Creates a matcher that matches if the examined object matches ANY of the specified matchers. 
  *           For example: assertThat("myValue", anyOf(startsWith("foo"), containsString("Val")))
  */
  
  @Test
  public void test_anyOf() throws Exception {
	  
	    LOG.info("Test for anyOf()");
      String check = "It's a great day today!";
      assertThat(check, anyOf(containsString("great"), containsString("bad")));
      
  }
  
  /**
   * instanceOf() : Creates a matcher that matches when the examined object is an instance of the specified type.
   */
  @Test
  public void test_instanceOf() throws Exception {
	  
	  LOG.info("Test for instanceOf()");
    Object string = "hello!";
    assertThat(string, instanceOf(String.class));
    
  }
  
  
  /**
   * nullValue() :Creates a matcher that matches if examined object is null. 
				  For example: assertThat(cheese, is(nullValue())
   */
  @Test
  public void test_nullValue() throws Exception {

	  LOG.info("Test for nullValue()");
    String nullString = null;
    assertThat(nullString, nullValue());
    
  }
  
  
  /**
   * hasItem() : Creates a matcher that matches the item in the Iterable.
   */
  @Test
  public void test_hasItem() throws Exception {
	  
	    LOG.info("Test for hasItem()");
      List<String> testList = Arrays.asList("one","two","three","four");
      assertThat(testList, hasItem("two"));
  }
  
  /**
   * hasItemInArray() : A shortcut to the frequently used hasItemInArray(equalTo(x)).
   */
  @Test
  public void test_hasItemInArray() throws Exception {
	  
	    LOG.info("Test for hasItemInArray()");
      Integer[] check = {1,2,3,4,5,6};
      assertThat(check, hasItemInArray(2));
  }
  
  /**
   *  greaterThan(), greaterThanOrEqual() : Creates a matcher for comparison.
   */
  @Test
  public void test_greaterThan() throws Exception {
	  
	    LOG.info("Test for greaterThan() and greaterThanOrEqual()");
      int testValue = 5;
      assertThat(testValue, is(greaterThan(3)));
      assertThat(testValue, is(greaterThanOrEqualTo(5)));
  }
  
  /**
   * equalToIgnoringCase() : Creates a matcher of String that matches when the examined 
   * 						 string is equal to the specified expectedString, ignoring case.
   */
  @Test
  public void test_equalToIgnoringCase() throws Exception {
	  
	    LOG.info("Test for equalToIgnoringCase()");
      String check = "hello";
      assertThat(check, equalToIgnoringCase("heLLO"));
      
  }
  
}

```

# Serialization and Deserialization

### What is serialization?

Serialization is the process of converting objects into a stream of data.

### What is deserialization?

Deserialization is the process of converting a stream of data into objects.

The main purpose of serialization and deserialization is to persist the data and recreate it whenever needed.

We have considered the Rest Assured library for making REST API calls. We will keep the scope within those capabilities of Rest Assured and the libraries it depends on.

As we keep learning about REST API automation and the data that is exchanged between client and server is of JSON format, we will learn how to serialize objects into a stream of JSON data and deserialize stream of data to objects that are exchanged between the REST web service.

Rest Assured can use the Jackson 2 library, GSON library or Jackson library for serialization and deserialization. The internal behavior of io.restassured.mapper.ObjectMapper is dependent on the library in the classpath.

### How to serialize an object?

Now, we will see how to set Java objects to request the body of an API so that Rest Assured can serialize the object into a stream of JSON data before making the API call.

```java
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotNull;

import java.io.IOException;
import java.lang.reflect.Type;
import java.util.Arrays;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.Test;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.ObjectMapper;

import io.restassured.RestAssured;
import io.restassured.response.Response;

public class APIDemo {

	private static final Logger LOG = LoggerFactory.getLogger(APIDemo.class);

	private static final ObjectMapper MAPPER = new ObjectMapper();

	private Integer id;

	@Test
	public void serializationTest() throws IOException {

		// creating `Student` object
		Student student = new Student("Sam", "Bailey", "Female");

		// converting `Student` object to JSON string using `ObjectMapper` 
		byte[] data = MAPPER.writeValueAsBytes(student);
		String json = MAPPER.writeValueAsString(student);

		LOG.info("serialization of `Student` class into JSON string using `ObjectMapper` => {}", new String(data));
		LOG.info("serialization of `Student` class into JSON string using `ObjectMapper` => {}", json);

		// using `Student` object in body of `CreateStudent` API
		String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
		Response response = RestAssured.given()
				.contentType("application/json")
				.log().all(true)
				.accept("application/json")
				.body(student)
				.post(url)
				.andReturn();
		
		// validating the HTTP status code
		assertEquals(response.getStatusCode(), 201, "http status");

		// saving the `id` of the created `Student` to delete the same in cleanup method
		id = response.path("id");

		// validating whether the created `Student` id not null
		assertNotNull(id, "created student id is null");

		LOG.info("created student id => {}", id);
	}

	@AfterMethod
	public void deleteUser() {
		if (id != null) {
			String url = "http://ezifyautomationlabs.com:6565/educative-rest/students/{id}";
			Response response = RestAssured.given()
			        .contentType("application/json")
					.accept("application/json")
					.pathParam("id", id)
					.delete(url);
			assertEquals(response.getStatusCode(), 204, "http status");
		}
	}

}

class Student {

	public Student() {
	}

	public Student(String firstName, String lastName, String gender) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.gender = gender;
	}

	Long id;

	@JsonProperty("first_name")
	String firstName;

	@JsonProperty("last_name")
	String lastName;
	
	String gender;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	@Override
	public String toString() {
		return String.format("Student [id=%s, firstName=%s, lastName=%s, gender=%s]", id, firstName, lastName, gender);
	}

}

```

In the code above, we see the body of the POST API is the Student object. Based on content-type header, the body content is serialized. In our case, the Student object is serialized into a stream of JSON string data.

If the content-type is not set, we get the 415 Unsupported Media Type HTTP status code, as the server won’t be able to understand the request body format.

If we are setting the body with JSON string directly instead of the Student object, then it is inferred that the content-type is JSON and we won’t get the 415 Unsupported Media Type HTTP status code error.

### How to deserialize into the object?

```java
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.Arrays;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import io.restassured.RestAssured;

public class APIDemo {

	private static final Logger LOG = LoggerFactory.getLogger(APIDemo.class);

	private static final ObjectMapper MAPPER = new ObjectMapper();

	@Test
	public void deserializationTest() throws IOException {

		String json = "{\"id\":100,\"gender\":\"Female\",\"first_name\":\"Sam\",\"last_name\":\"Bailey\"}";

        Student student = MAPPER.readValue(json, Student.class);
		LOG.info("deserialization of JSON string into `Student` class => {}", student);

		String url = "http://ezifyautomationlabs.com:6565/educative-rest/students/{id}";
		Student studentA = RestAssured
		        .given()
				.pathParam("id", "100")
				.get(url)
				.as(Student.class);
		LOG.info("deserialization of JSON string into class `Student` => {}", studentA);

		url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
		Student[] studentsArray = RestAssured
				.get(url)
				.as(Student[].class);
		LOG.info("deserialization of JSON string into `Student[]` => {}", Arrays.deepToString(studentsArray));

        Type type = new TypeReference<List<Student>>() {}.getType();

		List<Student> students = RestAssured
				.get(url)
				.as(type);
		LOG.info("deserialization of JSON string into class with type parameter `List<Student>` => {}", students);

	}

}

class Student {

	Long id;

	@JsonProperty("first_name")
	String firstName;

	@JsonProperty("last_name")
	String lastName;
	String gender;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	@Override
	public String toString() {
		return String.format("Student [id=%s, firstName=%s, lastName=%s, gender=%s]", id, firstName, lastName, gender);
	}

}

```

In the code above sample, we can see how to:

* deserialize a JSON string into the Student object using ObjectMapper.

* deserialize response from the API into the Student object

* deserialize response from the API into the Student[] object

* deserialize response from the API into the List<Student> object. Since List<T> is a class with a type parameter, we need to use the following code, where we need to pass the class type:

```java
Type type = new TypeReference<List<Student>>() {}.getType();
List<Student> students = RestAssured
            .get(url)
            .as(type);
```
Otherwise, we can simply put Student.class in place of type.

# Specification Builder

In order to avoid duplicate request parameters and/or response expectations for multiple tests, we can create specification objects which are reusable.

There are two types of specification builder Java classes as mentioned below:

* RequestSpecBuilder
* ResponseSpecBuilder


### RequestSpecification

This is used when a few common parameters are needed for multiple and/or different tests while creating a request.

```java
import static org.hamcrest.Matchers.anything;
import static org.hamcrest.Matchers.is;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;
import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.ResponseSpecification;

public class APIDemo {
	
	private static Logger LOG = LoggerFactory.getLogger(APIDemo.class);
       	   
	@Test
	public void test_RequestSpecificationWithQueryParam() {
		
		LOG.info("Step - 2 : Make a get() call using RequestSpecification to fetch John's record");
		Response response = RestAssured
							.given()
							.spec(getRequestSpecification())
							.queryParam("first_name", "John")
							.when()
							.get();
				 			
		LOG.info("Step - 3 : Print the JSON response body");
		response.getBody().prettyPrint();
	
	}
	
	@Test
	public void test_RequestSpecification() {
		
		LOG.info("Step - 4 : Make a get() call using RequestSpecification to fetch all Student's record");
		Response response = RestAssured
							.given()
							.spec(getRequestSpecification())
							.when()
							.get();
				 			
		LOG.info("Step -5 : Print the JSON response body");
		response.getBody().prettyPrint();
	
	}



	// Helper method   
    public RequestSpecification getRequestSpecification() {
		
		LOG.info("Step - 1 : Create RequestSpecification using  RequestSpecBuilder ");
		RequestSpecBuilder builder = new RequestSpecBuilder();

		builder.setBaseUri ("http://ezifyautomationlabs.com:6565");
		builder.setBasePath ("/educative-rest/students");

		RequestSpecification requestSpec = builder.build();
		return requestSpec;
	}
	
}

```

### ResponseSpecification

This is used to validate a common response or a response needed for multiple tests from the body. We can also merge additional body expectations must all be fulfilled for the test to pass.

Let’s get a better understanding of how this works with the example code for creating a ResponseSpecification using [ResponseSpecBuilder](https://www.javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/builder/ResponseSpecBuilder.html).

```java
import static org.hamcrest.Matchers.anything;
import static org.hamcrest.Matchers.is;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;
import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.ResponseSpecification;

public class APIDemo {
	
	private static Logger LOG = LoggerFactory.getLogger(APIDemo.class);
       
   @Test
	public void test_ResponseSpecification1() {
		
		String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
		
		LOG.info("Step - 2 : Make a get() call using ResponseSpecification and validate status 200 ");
		RestAssured
		.when()
		.get(url)
		.then()
		.spec(getResponseSpecification());
	}
	
	
	@Test
	public void test_ResponseSpecification2() {
		
		String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
		
		LOG.info("Step - 3 : Make a get() call using ResponseSpecification and validate status code and Student's first name is John ");
		RestAssured
		.when()
		.get(url)
		.then()
		.spec(getResponseSpecification())
		.body("John", is(anything()));
	}
	
	// Helper method
	public ResponseSpecification getResponseSpecification() {
		
		LOG.info("Step - 1 : Create ResponseSpecification using ResponseSpecBuilder ");
		ResponseSpecBuilder builder = new ResponseSpecBuilder();
		builder.expectStatusCode(200);		

		ResponseSpecification responseSpec = builder.build();
		return responseSpec;
	}
}

```

### RequestSpecification and ResponseSpecification combined

```java
import static org.hamcrest.Matchers.anything;
import static org.hamcrest.Matchers.is;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;
import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.ResponseSpecification;

public class APIDemo {
	
	private static Logger LOG = LoggerFactory.getLogger(APIDemo.class);
       
   @Test
	public void test_combineRequestResponseSpecification() {
				
		LOG.info("Step - 1 : Make a get() call using ResponseSpecification and ResponseSpecification ");
		RestAssured
		.given()
		.spec(getRequestSpecification())
		.when()
		.get()
		.then()
		.spec(getResponseSpecification());	
	}

    /**
	* Helper methods for creating RequestSpecification and ResponseSpecification
	**/
	public RequestSpecification getRequestSpecification() {
		
		LOG.info("Step - 2 : Create RequestSpecification using  RequestSpecBuilder ");
		RequestSpecBuilder builder = new RequestSpecBuilder();

		builder.setBaseUri ("http://ezifyautomationlabs.com:6565");
		builder.setBasePath ("/educative-rest/students");
		builder.addQueryParam("gender", "male");	

		RequestSpecification requestSpec = builder.build();
		return requestSpec;
	}

	public ResponseSpecification getResponseSpecification() {
		
		LOG.info("Step - 3 : Create ResponseSpecification using ResponseSpecBuilder ");
		ResponseSpecBuilder builder = new ResponseSpecBuilder();
		builder.expectStatusCode(200);		

		ResponseSpecification responseSpec = builder.build();
		return responseSpec;
	}
}

```


# File Uploads

### Example: Upload a JSON file to create a list of studentm

* HTTP Method: POST
* Target URL: http://ezifyautomationlabs.com:6565
* Resource path: /educative-rest/students/upload
* Message body: multipart/form-data


```java
import static org.testng.Assert.assertEquals;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;

public class APIDemo {

	private static final Logger LOG = LoggerFactory.getLogger(APIDemo.class);

	@Test
	public void fileUpload() throws IOException {

		String url = "http://ezifyautomationlabs.com:6565/educative-rest/students/upload";

        // creating JSON content to write to file
		String json = "[{\"first_name\":\"Sam\",\"last_name\":\"Bailey\",\"gender\":\"Female\"},{\"first_name\":\"Sam\",\"last_name\":\"Hudson\",\"gender\":\"Male\"}]";

        // write the JSON string to File
		File file = new File("students.json");
		Files.write(file.toPath(), json.getBytes());

        // make api call to create list of `Student`
		Response response = RestAssured.given()
				.multiPart("file", file)
				.log().all()
				.post(url)
				.thenReturn();

		// validate the http status code of the response
		assertEquals(response.getStatusCode(), 201, "http status code");

		LOG.info("response body => {}", response.getBody().prettyPrint());
	}
}
```

# File Downloads 

### Example: Download JSON file

* HTTP method: GET
* Target URL: http://ezifyautomationlabs.com:6565
* Resource path: /educative-rest/students

```java
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertTrue;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;

public class APIDemo {

	private static final Logger LOG = LoggerFactory.getLogger(APIDemo.class);

	@Test
	public void testDownload() throws IOException {

		String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";

        // making API call
		Response response = RestAssured.given()
				.log().all(true)
				.get(url)
				.andReturn();

        // validating http status code
		assertEquals(response.getStatusCode(), 200, "http status code");

        // reading the response boody as byte[]
		byte[] bytes = response.getBody().asByteArray();
        // validating that the response content length > 0
		assertTrue(bytes.length > 0, "response content length is 0");

        // writing the byte[] to file
		File file = new File("students.json");
		Files.write(file.toPath(), bytes);

        // validating the existence and size of file
		assertTrue(file.exists(), "file " + file + " does not exist");
		assertTrue(file.length() > 0, "file size is 0");
        assertEquals(bytes.length, file.length(), "file size and response content");

		String content = new String(Files.readAllBytes(file.toPath()));
		LOG.info("printing content of the file => {}", content);
	}

}
```

# Basic Authentication

### Example

Let’s understand basic authentication better with an example code snippet:

* HTTP method: GET
* Target URL: http://ezifyautomationlabs.com:6565
* Resource path: /educative-rest/auth/students
* Authentication type: Basic



```java
import static org.testng.Assert.assertTrue;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;

public class APIDemo {

	private static Logger LOG = LoggerFactory.getLogger(APIDemo.class);

    /**
     * Basic authentication using Valid username and password
     */
	@Test
	public void test_authentication_ValidCredentials() {
		String url = "http://ezifyautomationlabs.com:6565/educative-rest/auth/students";
		
        String valid_userName = "testuser";
        String valid_password = "testpass";      
        
        Response response =  RestAssured
        					.given()
        					.auth().basic(valid_userName, valid_password)
        		        	.when()
        		        	.get(url)
        		        	.thenReturn();
        
        LOG.info("It will return a valid response");
        response.getBody().prettyPrint();
        assertTrue(response.getStatusCode() == 200);   
	}
	
    /**
     * Basic authentication using In-valid username and password
     */
	@Test
	public void test_authentication_InvalidCredentials() {
		String url = "http://ezifyautomationlabs.com:6565/educative-rest/auth/students";
		
        String invalid_userName = "testuser1";
        String valid_password = "testpass";      
        
        Response response =  RestAssured
        					.given()
        					.auth().basic(invalid_userName, valid_password)
        		        	.when()
        		        	.get(url)
        		        	.thenReturn();
        
        LOG.info("It will return authorization error 401");
        response.getBody().prettyPrint();
        assertTrue(response.getStatusCode() == 401);  
	}
	
    /**
     * Basic authentication using Auth token
     */
	@Test
	public void test_authentication_AuthToken() {

		String url = "http://ezifyautomationlabs.com:6565/educative-rest/auth/students";
   
        String authCode = "Basic dGVzdHVzZXI6dGVzdHBhc3M=";
        
        Response response =  RestAssured
        					 .given()
       		        	     .header("authorization", authCode)
        		        	 .when()
        		        	 .get(url)
        		        	 .thenReturn();
        
        LOG.info("It will return a valid response");
        response.getBody().prettyPrint();
        assertTrue(response.getStatusCode() == 200); 
	}

}
```

# Async Requests


### What is an async request?

Synchronous request blocks the execution of server code until the response is received, whereas asynchronous request (async in short), does not block the execution and returns a callback to the client which can be used to receive the actual data once the execution is complete.

### Handling async requests

REST Assured does not support async requests out of the box. We can automate these use cases using a third-party open-source library.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;
import org.asynchttpclient.Dsl;
import java.util.concurrent.Future;
import org.asynchttpclient.Response;
import java.util.concurrent.TimeoutException;
import java.util.concurrent.ExecutionException;

public class APIDemo {

	private static Logger LOG = LoggerFactory.getLogger(APIDemo.class);

	static {
		// setting logger to INFO to disable unwanted http client logs
		((ch.qos.logback.classic.Logger) org.slf4j.LoggerFactory
				.getLogger(ch.qos.logback.classic.Logger.ROOT_LOGGER_NAME))
						.setLevel(ch.qos.logback.classic.Level.INFO);
	}

	@Test
	public void asyncTest() throws InterruptedException, ExecutionException, TimeoutException {

		String url = "https://reqres.in/api/users?delay=3";

		Future<Response> whenResponse = Dsl.asyncHttpClient().prepareGet(url).execute();
		
		Response response = whenResponse.get();	
		LOG.info(response.getResponseBody());
	}
}
```

# Proxy Server Settings

A proxy server is an intermediary server that is virtually located between the client and the server. All the service requests are sent to the actual server via proxy servers.




