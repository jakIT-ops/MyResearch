package io.datajek.unittesting;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

class ArrayMethodsTest {

	private ArrayMethods arrayMethods;

	@Test
	public void testfindIndex_numberInArray() {
		System.out.println("Test1");
	    int result = arrayMethods.findIndex(new int[]{8,4,5}, 4);
	    assertEquals(1, result);
	}

	@Test
	public void testfindIndex_numberNotInArray() {
		System.out.println("Test2");
	    assertEquals(-1, arrayMethods.findIndex(new int[]{8,4,5}, 1));
	}

	@Test
	public void testfindIndex_emptyArray() {
		System.out.println("Test3");
	    assertEquals(-1, arrayMethods.findIndex(new int[]{}, 1));
	}

	@Test
	@Disabled
	public void testSortArray() {
		fail("unimplemented method");
	}

	@BeforeEach
	void init(){
		//Initialize the object here
		System.out.println("Initializing before test");
		arrayMethods = new ArrayMethods();
	}

	@AfterEach
	void afterEachTest(){
		System.out.println("Clean up after test");
	}
	
	@BeforeAll
	static void beforeAllTests() {
		System.out.println("Run this code before all tests");
	}
	
	@AfterAll
	static void afterAllTests() {
		System.out.println("Run this code after all tests");
	}
}
