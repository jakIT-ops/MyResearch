# What is integration testing 

This is a testing technique where individual components are tested in a sequence or as a group.

In a complex software system, there are multiple microservices interacting with each other. Each of them is developed to solve a specific use case and allows multiple interfaces to interact with each other.


# Integration Test - REST

### Integration scenario

In this scenario, we are simulating and automating the integration flow for a single service.

We will use our demo REST API to automate the below integration flow as follows:

1. Create a new Student
2. Verify that Student is created
3. Search the newly-created Student by id
4. Verify the search result
5. Delete the created Student
6. Verify the Student has been deleted


```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.testng.annotations.Test;
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertTrue;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.restassured.RestAssured;
import io.restassured.response.ResponseOptions;

public class StudentIntegrationTest {

   private static Logger LOG = LoggerFactory.getLogger(StudentIntegrationTest.class);

	@Test
	public void testIntegrationFlow() {
	
	    //Target resource
        String url = "http://ezifyautomationlabs.com:6565/educative-rest/students";
        // Message body object.
        Student body = new Student("David", "Paul", "Male");

	    //Step 1 - Create a new Student 
        ResponseOptions<?> create = RestAssured.given()
                .header("accept", "application/json")
                .header("content-type", "application/json")
                .body(body)
                .post(url)
				.andReturn();
        
        //print response message body in JSON format
        LOG.info("Server response for created Student record : " +create.getBody().prettyPrint());
        	
		//Step -2 Assert that request was successful
        assertTrue(create.statusCode() == 201); 
		long createdStudentId = create.getBody().jsonPath().getLong("id");

		//Step 3 - fetch the newly created Student details 	     
        ResponseOptions<?> fetch = RestAssured.given()
        		.get(url + "/" + createdStudentId)
				.andReturn();
        
        //print response message body in JSON format
        LOG.info("fetch newly created Student's record with id "+createdStudentId+  ":" +fetch.getBody().prettyPrint());
		
		//Step -4 parse the response data and verify and assert fetch Student details
        assertTrue(fetch.statusCode() == 200);
		long studentID = fetch.getBody().jsonPath().getLong("id");
		assertEquals(createdStudentId,studentID); 
		
		//Step 5 - Delete the newly created Student Object 	 
		 LOG.info("Delete Student with id "+studentID+"'s record");
		 ResponseOptions<?> delete = RestAssured.given()
	        		.delete(url + "/" + studentID);
		//Assert request was successful
	    assertTrue(delete.statusCode() == 204);
		
		// Step 6 - Try getting Deleted  Student's record
        ResponseOptions<?> deletedStudent = RestAssured.given()
        		.get(url + "/" + createdStudentId)
				.andReturn();

        //Assert record is deleted - NO record found
        LOG.info("HTTP GET response statusLine of deleted record "+deletedStudent.getStatusLine());
	    assertTrue(deletedStudent.statusCode() == 404); 
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

# Integration Test - SOAP

### Integration scenario

In this scenario, we are simulating and automating the integration flow of a single service.

We will use our demo SOAP web services to automate the below integration flow as follows:

1. Create a new Student
2. Verify Student is created
3. Search the newly-created Student by id
4. Update the created Student with new information
5. Verify the search result
6. Delete the created Student
7. Verify the Student is deleted


```java
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotNull;
import static org.testng.Assert.assertTrue;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.ws.client.core.WebServiceTemplate;
import org.springframework.ws.soap.client.SoapFaultClientException;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.Test;

import com.fasterxml.jackson.dataformat.xml.XmlMapper;

import io.educative.soap_automation.CreateStudentRequest;
import io.educative.soap_automation.CreateStudentResponse;
import io.educative.soap_automation.DeleteStudentRequest;
import io.educative.soap_automation.DeleteStudentResponse;
import io.educative.soap_automation.GetStudentsRequest;
import io.educative.soap_automation.GetStudentsResponse;
import io.educative.soap_automation.UpdateStudentRequest;
import io.educative.soap_automation.UpdateStudentResponse;

public class TestSOAP extends BaseTest {

	@Test
	public void testCreateUpdateDeleteStudent() {

		// Creating Student with following details
		CreateStudentRequest createStudentRequest = new CreateStudentRequest();
		createStudentRequest.setGender("Female");
		createStudentRequest.setFirstName("Sam");
		createStudentRequest.setLastName("Bailey");

		// Making Create Student web service call
		CreateStudentResponse createStudentResponse = (CreateStudentResponse) webServiceTemplate.marshalSendAndReceive(
				SERVICE_URL, createStudentRequest);

		// Validating response is not null
		assertNotNull(createStudentResponse, "CreateStudentResponse is null");

		// Printing the response XML
		printResponse(createStudentResponse);

		// Created Student ID
		long id = createStudentResponse.getStudent().getId();
		GetStudentsRequest getStudentsRequest = new GetStudentsRequest();
		getStudentsRequest.setId(id);

		// Fetching the created Student response
		GetStudentsResponse getStudentsResponse = (GetStudentsResponse) webServiceTemplate.marshalSendAndReceive(
				SERVICE_URL, getStudentsRequest);

		// Validating response is not null and contains more than one object
		assertNotNull(getStudentsResponse, "GetStudentsResponse is null");
		assertTrue(!getStudentsResponse.getStudents().isEmpty(), "students list is empty");
		assertEquals(getStudentsResponse.getStudents().get(0).getFirstName(), "Sam", "first name");

        // Printing the response XML
		printResponse(getStudentsResponse);

		// Update the Student with information
		UpdateStudentRequest updateStudentRequest = new UpdateStudentRequest();
		updateStudentRequest.setId(id);
		updateStudentRequest.setGender("Male");
		updateStudentRequest.setFirstName("Johnny");
		updateStudentRequest.setLastName("Doe");

		// Making UpdateStudent web service call
		UpdateStudentResponse updateStudentResponse = (UpdateStudentResponse) webServiceTemplate.marshalSendAndReceive(
				SERVICE_URL, updateStudentRequest);

		// Validating response not null and the first name as given in the request
		assertNotNull(updateStudentResponse, "UpdateStudentResponse is null");
		assertEquals(updateStudentResponse.getStudent().getFirstName(), "Johnny");

        // Printing the response XML
		printResponse(updateStudentResponse);

		// Fetching the created Student response
		GetStudentsResponse getStudentsResponseAfterUpdate = (GetStudentsResponse) webServiceTemplate
				.marshalSendAndReceive(SERVICE_URL, getStudentsRequest);

		assertNotNull(getStudentsResponseAfterUpdate, "GetStudentsResponse is null");
		assertTrue(!getStudentsResponseAfterUpdate.getStudents().isEmpty(), "students list is empty");

		// Printing the response XML
		printResponse(getStudentsResponseAfterUpdate);

		// Deleting the Student
		DeleteStudentRequest deleteStudentRequest = new DeleteStudentRequest();
		deleteStudentRequest.setId(id);

		// Making DeleteStudent web service call
		DeleteStudentResponse deleteStudentResponse = (DeleteStudentResponse) webServiceTemplate.marshalSendAndReceive(
				SERVICE_URL, deleteStudentRequest);

		// Validating response is not null and isDeleted() true on successful delete
		assertNotNull(deleteStudentResponse, "DeleteStudentResponse is null");
		assertTrue(deleteStudentResponse.isDeleted(), "Student not deleted");

		// Printing the response XML
		printResponse(deleteStudentResponse);

		// Fetching the deleted Student and expecting SoapFaultClientException
		try {
			webServiceTemplate.marshalSendAndReceive(SERVICE_URL, getStudentsRequest);
		} catch (SoapFaultClientException e) {
			assertEquals(e.getMessage(), String.format("student with id '%s' not found", id));
		}
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

	// Initializing WebServiceTemplate
	@BeforeClass
	public void initTemplate() {
		webServiceTemplate = CONTEXT.getBean(WebServiceTemplate.class);
	}

	// Printing XML Response
	protected void printResponse(Object response) {
		try {
			LOG.info("printing response '{}' => \n{}", response.getClass().getName(),
					new XmlMapper().writerWithDefaultPrettyPrinter().writeValueAsString(response));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	// An utility to create student
	protected long createStudent() {
		CreateStudentRequest request = new CreateStudentRequest();
		request.setGender("Male");
		request.setFirstName("John");
		request.setLastName("Doe");

		CreateStudentResponse response = (CreateStudentResponse) webServiceTemplate.marshalSendAndReceive(SERVICE_URL,
				request);

		assertNotNull(response, "CreateStudentResponse is null");

		return response.getStudent().getId();
	}
}
```



